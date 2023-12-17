# Importing modules
import pygame
import pygame.event
import time
import math
import random
import sys
"""
sys.path.append("./BaseGame/Board/")
sys.path.append("./BaseGame/Hexagon Tiles/")
sys.path.append("./BaseGame/Robber/")
sys.path.append("./BaseGame/Dice/")"""
from BaseGame.Buttons.buttons import Button, Trade, trade, TradePrompt, trade_prompt
from BaseGame.Board.board import Board
from BaseGame.CardsPrompt.cards_prompt import cards_prompt, CardsPrompt
from BaseGame.Dice.dice import Dice
from BaseGame.Hexagon_Tiles.hexagon_tile import HexagonTile
from BaseGame.Player.player import Player, players
from BaseGame.Road.road import Road, roads
from BaseGame.Road.road_events import RoadEventHandler
from BaseGame.Robber.robber import Robber
from BaseGame.Settlements.settlement import Settlement
from BaseGame.Settlements.settlement_event import SettlementEventHandler
from BaseGame.Error.error import Error
from BaseGame.PopUp.pop_up import PopUp
#from BaseGame.Trade.trade import Trade, trade
from constants import *

class Game:
    @staticmethod
    def window_setup():
        pygame.init()

        window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Catan")
        icon = pygame.image.load("../Assets/icon.png")
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)

        return window

    # --- Main loop ---
    @staticmethod
    def main(window):
        print(GetSystemMetrics(0))
        print(GetSystemMetrics(1))
        # Game loop variables
        dice_first_dsp = True
        running = True
        roll = [0, 0]
        robber_pos = (-1, -1)
        ROUND_NUMBER = 0

        # --- Background ---
        window.fill(BRASS)
        """
        image = pygame.image.load(BACKGROUND_SPRITE)
        image = pygame.transform.scale_by(image, 1.6)
        window.blit(image, (0, 0))
        """
    
        HexagonTile.draw_sea_hexagon(window, SCREEN_WIDTH / 2 - HEXAGON_WIDTH / 2 - HEXAGON_WIDTH - 50, HEXAGON_Y_AXIS - 55)

        # --- Hexagon grid ---
        HexagonTile.create_hexagon_grid(window, HEXAGON_X_AXIS, HEXAGON_Y_AXIS)

        #print(HexagonTile.resourcesArray)
        #print(HexagonTile.center_points)

        # --- Robber ---
        Robber.create_robber(window)

        # --- Settlement Surfaces ---
        Settlement.prepare_board_surfaces(window, HexagonTile.distinct_vertices, HexagonTile.hexagons)
        
        # --- Buttons ---
        road_button = Button.create_road_button()
        #road_button.draw(window)
        settlement_button = Button.create_settlement_button()
        #settlement_button.draw(window)
        end_turn_button = Button.create_end_turn_button()
        #special_card_button = Button.create_special_card_button()
        #special_card_button.draw(window)

        # --- Settlement Surfaces ---
        Settlement.prepare_board_surfaces(window, HexagonTile.distinct_vertices, HexagonTile.hexagons)

        # --- Roads ---

        # --- Player ---
        current_player = players[0]  # Current player
        #for card in current_player.cards:
         #   print(card)
                

        Player.draw_players(window)

        # --- Cards prompt ---
        cards_prompt.show_cards(window, current_player)

        # --- Trade prompt ---
        trade.show_trade(window, current_player)
        trade_prompt.create_trade_prompt_buttons()

        # --- Dice ---
        dice_btn = Dice.roll_dice_btn(window)

        if dice_first_dsp:
            Dice.dices(window, [1, 1])
            dice_first_dsp = False

        END_START_ROUND = False

        while running:
            # TODO trade mechanic
            GAME_START = False  # TODO dont pass as parameter to settlement_place!

            if END_START_ROUND is False:
                for player in players:
                    if len(player.settlements) < 2 or len(player.roads) < 2:
                        GAME_START = True
                    elif len(current_player.roads) == 2 and current_player.roads[-1].is_placed is False:
                        GAME_START = True
                    elif players.index(player) == 3 and END_START_ROUND is False:
                        GAME_START = True
                        END_START_ROUND = True

             # Add buttons hover feature
            if GAME_START is False:

                # Hover over Settlement button
                pos = pygame.mouse.get_pos()
                if settlement_button.rect.collidepoint(pos):
                    PopUp.show_settlement_info(window)
                    settlement_button.hover = True
                if settlement_button.rect.collidepoint(pos) == False and settlement_button.hover == True:
                    settlement_button.hover = False
                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                    if(settlement_button.clicked_up == True):
                        Button.show_pressed_settlement_button(window)

                # Hover over Road button
                if road_button.rect.collidepoint(pos):
                    PopUp.show_road_info(window)
                    road_button.hover = True
                if road_button.rect.collidepoint(pos) == False and road_button.hover == True:
                    road_button.hover = False
                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                    if(road_button.clicked_up == True):
                        Button.show_pressed_road_button(window)

            # Round pop up
            if ROUND_NUMBER == 0:
                PopUp.starting_round_popup(window)
                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                ROUND_NUMBER = ROUND_NUMBER + 1

            # Finished placing initial settlements and roads
            if END_START_ROUND is True and GAME_START is True:
                current_player = players[0]
                GAME_START = False
                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                # Switch to first round:
                PopUp.round_number_popup(window, ROUND_NUMBER)
                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                ROUND_NUMBER = ROUND_NUMBER + 1

            elif GAME_START and len(current_player.settlements) == 2 :
                # Switch player
                if (len(current_player.roads) == 2 and current_player.roads[-1].is_placed is True):
                    current_player = players[(players.index(current_player) + 1) % len(players)]
                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

                elif (len(current_player.roads) == 3 and current_player.roads[-1].is_placed is False):
                    current_player = players[(players.index(current_player) + 1) % len(players)]
                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

            # Prepare a road if the road button is pressed down or if we are in the starting round
            if(road_button.clicked_up or GAME_START is True):
                # --- Roads ---
                if len(current_player.roads) != 0:
                    current_player.current_road = current_player.roads[-1]
                else:
                    current_player.current_road = Road()
                    current_player.roads.append(current_player.current_road)

                if current_player.current_road.is_placed is True:  # If we successfully placed a road, prepare a new one
                    current_player.roads.append(Road())

            # --- Event loop ---
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #print("running")
                    if dice_btn.collidepoint(mouse_pos) and trade_prompt.showing is False:
                        if GAME_START:
                            # << Place two settlements and two roads >> error popups
                            if(len(current_player.roads) <= 2 and len(current_player.settlements) < 2):
                                if(len(current_player.roads) == 0):
                                    Error.error_popup_place_settlements_roads(window)
                                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                                elif len(current_player.roads) != 0 and current_player.roads[-1].is_placed is False:
                                    Error.error_popup_place_settlements_roads(window)
                                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

                            elif(len(current_player.roads) <= 2):
                                if(len(current_player.roads) == 0):
                                    Error.error_popup_place_roads(window)
                                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                                elif current_player.roads[-1].is_placed is False:
                                    Error.error_popup_place_roads(window)
                                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

                            elif(len(current_player.settlements) < 2):
                                Error.error_popup_place_settlements(window)
                                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                                
                        if GAME_START is False and current_player.rolled == False:
                            roll = [Dice.dice_roll(), Dice.dice_roll()]
                            current_player.rolled = True

                            # Acquire resources
                            for player in players:
                                print('aquiring')
                                player.acquire_cards(sum(roll))
                            Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

                            if sum(roll) == 7:
                                print("Robber")
                                Dice.dices(window, roll)
                                pygame.display.update()

                                # --- Move robber ---
                                robber_pos = Robber.move_robber_event(window, running, dice_btn)

                                # --- Update board ---
                                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

                            """
                            else:

                                # Possibly switch to next round
                                if(players.index(current_player) + 1) % len(players) == 0:
                                    ROUND_NUMBER = ROUND_NUMBER + 1
                                    PopUp.round_number_popup(window, ROUND_NUMBER)
                                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                            
                                # Switch to next player
                                current_player = players[(players.index(current_player) + 1) % len(players)]
                                # time.sleep(1)
                                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                                # TODO switch to start of turn state
                                """

                    # End turn button is clicked down
                    if end_turn_button.rect.collidepoint(mouse_pos) and GAME_START is False:
                        if current_player.rolled == True:
                            end_turn_button.clicked = True
                            end_turn_button.show_pressed_end_turn_button(window)
                        else:
                            Error.error_popup_roll_dice(window)
                            Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

                    # Road button is clicked down
                    if road_button.rect.collidepoint(mouse_pos) and trade_prompt.showing is False:
                        road_button.clicked = True

                    # Settlement button is clicked down
                    if settlement_button.rect.collidepoint(mouse_pos) and trade_prompt.showing is False:
                        settlement_button.clicked = True

                    for trade_button in current_player.trade_button:
                        # Trade button is clicked down
                        if trade_button.rect.collidepoint(mouse_pos):
                            trade_button.clicked = True
                            trade_button.show_pressed_trade_button(window, trade_button.card)

                    if(trade_prompt.showing):
                        for button_name in trade_prompt.trade_2_buttons:
                            # Trade bank button is clicked down
                            if trade_prompt.trade_2_buttons[button_name].rect.collidepoint(mouse_pos):
                                if trade_prompt.current_trade_button.name != button_name:
                                    trade_prompt.trade_2_buttons[button_name].clicked = True
                                    TradePrompt.show_pressed_trade_2_button(window, button_name)


                    """
                    # Special card button is clicked down
                    if special_card_button.rect.collidepoint(mouse_pos):
                        print('buy special_card')
                        special_card_button.clicked = True
                    """

                    for center_point in HexagonTile.center_points:
                        if center_point[0] - HEXAGON_SIDE / 3 <= mouse_pos[0] <= center_point[0] + HEXAGON_SIDE / 3:
                            if center_point[1] - HEXAGON_SIDE / 3 <= mouse_pos[1] <= \
                                    center_point[1] + HEXAGON_SIDE / 3:
                                print("Trying")
                                if Robber.check_move(mouse_pos):
                                    print("Moving")
                                    Robber.move_robber(window, center_point)
                            # base.HexagonTile.create_hexagon_grid(window, c.HEXAGON_X_AXIS, c.HEXAGON_Y_AXIS, False)
                            # TODO: Move robber
                            # i moved it somewhere else

                    # Prepare settlement event
                    SettlementEventHandler.press(window)

                    # Place road event
                    RoadEventHandler.press(window, event, current_player.current_road, current_player)

                elif event.type == pygame.MOUSEBUTTONUP:

                    # Settlement button is clicked up
                    if settlement_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if(settlement_button.clicked):
                            if Settlement.placement_is_possible(current_player, GAME_START) is False:
                                Error.error_popup_resources(window)
                                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                                settlement_button.clicked = False
                            else:
                                Button.show_pressed_settlement_button(window)
                                settlement_button.clicked_up = True
                                settlement_button.clicked = False

                    # Place settlement event
                    SettlementEventHandler.place(window, robber_pos, roll, current_player, GAME_START, settlement_button)

                    # TODO: Implement special cards
                    """
                    if(special_card_button.clicked):
                        if SpecialCard.placement_is_possible(player, GAME_START) is False:
                            Error.error_popup_resources(window)
                            Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                        else:
                            special_card_button.clicked_up = True
                            special_card_button.clicked = False
                    """

                    # Road button is clicked up
                    if road_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if(road_button.clicked):
                            # Checck if you have the resources
                            if Road.placement_is_possible(current_player, GAME_START) is False:
                                Error.error_popup_resources(window)
                                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                            else:
                                Button.show_pressed_road_button(window)
                                road_button.clicked_up = True
                                road_button.clicked = False
                            
                    if(road_button.clicked_up is True or GAME_START is True):
                        # If placing the road was unsuccessful, remove it from the list
                        if RoadEventHandler.place(window, event, current_player.current_road, current_player, GAME_START, robber_pos, roll) == -1:
                            print('didnt work out')
                        else:
                            road_button.clicked_up = False
                            # If placing the road was successful, append it to the main list of roads as well
                            #roads.append(current_player.current_road)

                    # Trade button is clicked up
                    for trade_button in current_player.trade_button:
                        if trade_button.rect.collidepoint(pygame.mouse.get_pos()):
                            if(trade_button.clicked):
                                print("trade")
                                trade_prompt.current_trade_button = trade_button
                                trade_prompt.show_trade_prompt(window, current_player, trade_button)
                                trade_prompt.showing = True
                                #trade_button.clicked = False
                                
                    # Trade bank button is clicked up
                    if(trade_prompt.showing):
                        for button_name in trade_prompt.trade_2_buttons:
                            if trade_prompt.trade_2_buttons[button_name].rect.collidepoint(pygame.mouse.get_pos()):
                                if(trade_prompt.trade_2_buttons[button_name].clicked):
                                    trade_prompt.current_trade_button.clicked = False
                                    trade_prompt.trade_2_buttons[button_name].clicked = False
                                    if trade_prompt.trade_2_buttons[button_name].name != "Exit":
                                        current_player.cards[trade_prompt.current_trade_button.name] -= 3
                                        current_player.cards[trade_prompt.trade_2_buttons[button_name].name] += 1
                                        current_player.resource_cards -= 2
                                    trade_prompt.showing = False
                                    Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

                    # End turn button is clicked up
                    if end_turn_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if(end_turn_button.clicked):
                            end_turn_button.clicked = False
                            # Possibly switch to next round
                            if(players.index(current_player) + 1) % len(players) == 0:
                                ROUND_NUMBER = ROUND_NUMBER + 1
                                PopUp.round_number_popup(window, ROUND_NUMBER)
                                Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
                                
                            # Switch to next player
                            current_player = players[(players.index(current_player) + 1) % len(players)]
                            current_player.rolled = False
                            # time.sleep(1)
                            Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)

                elif event.type == pygame.MOUSEMOTION:
                    # Dragging road event
                    RoadEventHandler.drag(window, pygame.mouse.get_pos(), current_player.current_road)

                # Hover settlement event TODO
                # SettlementEventHandler.hover_settlement(window, roll)

            Dice.dices(window, roll)

            pygame.display.update()

        pygame.quit()

    # TODO: remove this after testing
    if __name__ == "__main__":
        window = window_setup()
        main(window)
        exit()