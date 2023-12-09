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
from BaseGame.Buttons.buttons import Button
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

        # Game loop variables
        dice_first_dsp = True
        running = True
        roll = [0, 0]
        robber_pos = (-1, -1)

        # --- Background ---
        window.fill(BRASS)
    
        HexagonTile.draw_sea_hexagon(window, SCREEN_WIDTH / 2 - HEXAGON_WIDTH / 2 - HEXAGON_WIDTH - 50, HEXAGON_Y_AXIS - 55)

        # --- Hexagon grid ---
        HexagonTile.create_hexagon_grid(window, HEXAGON_X_AXIS, HEXAGON_Y_AXIS)

        print(HexagonTile.resourcesArray)
        print(HexagonTile.center_points)

        # --- Robber ---
        Robber.create_robber(window)

        # --- Settlement Surfaces ---
        Settlement.prepare_board_surfaces(window, HexagonTile.distinct_vertices, HexagonTile.hexagons)
        
        # --- Buttons ---
        road_button = Button.create_road_button()
        road_button.draw(window)
        settlement_button = Button.create_settlement_button()
        settlement_button.draw(window)
        special_card_button = Button.create_special_card_button()
        special_card_button.draw(window)

        # --- Settlement Surfaces ---
        Settlement.prepare_board_surfaces(window, HexagonTile.distinct_vertices, HexagonTile.hexagons)

        # --- Roads ---

        # --- Player ---
        current_player = players[0]  # Current player
        print(":;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(len(current_player.roads))

        Player.draw_players(window)
        print(len(current_player.roads))

        # --- Cards prompt ---
        cards_prompt.show_cards(window, current_player)

        END_START_ROUND = False

        while running:
            # TODO place roads only if you have enough resources
            # TODO trade mechanic
            #print(len(current_player.roads))
            GAME_START = False  # TODO dont pass as parameter to settlement_place!

            # Add buttons hover feature
           # road_button.hover()
            settlement_button.hover()
            special_card_button.hover()

            for player in players:
               # print(len(player.settlements))
                #print(len(player.roads))
                if len(player.settlements) < 2 or len(player.roads) < 2:
                    GAME_START = True
                elif len(current_player.roads) == 2 and current_player.roads[-1].is_placed is False:
                    GAME_START = True
                elif players.index(player) == 3 and END_START_ROUND is False:
                    print("intra")
                    GAME_START = True
                    END_START_ROUND = True

            # Finished placing initial settlements and roads
            if END_START_ROUND is True and GAME_START is True:
                current_player = players[0]
                Board.redraw_board(window, robber_pos, roll, current_player)
            elif GAME_START and len(current_player.settlements) == 2 and len(current_player.roads) == 2:
                if current_player.roads[-1].is_placed is True:
                    # Switch player
                    current_player = players[(players.index(current_player) + 1) % len(players)]
                    Board.redraw_board(window, robber_pos, roll, current_player)

            if(road_button.clicked_up or GAME_START is True):
                print('prepare road')
                # --- Roads ---
                # This needs to activate only when the player is placing a road
                if len(current_player.roads) != 0:
                    current_player.current_road = current_player.roads[-1]
                else:
                    current_player.current_road = Road()
                    current_player.roads.append(current_player.current_road)
                    print('APPEND')

                if current_player.current_road.is_placed is True:  # If we successfully placed a road, prepare a new one
                    print('prepare NEW road')
                    current_player.roads.append(Road())

            # --- Event loop ---
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("running")
                    if dice_btn.collidepoint(mouse_pos):
                        if GAME_START:
                            if(len(current_player.roads) <= 2 and len(current_player.settlements) < 2):
                                if(len(current_player.roads) == 0):
                                    Error.error_popup_place_settlements_roads(window)
                                    Board.redraw_board(window, robber_pos, roll, current_player)
                                elif len(current_player.roads) != 0 and current_player.roads[-1].is_placed is False:
                                    Error.error_popup_place_settlements_roads(window)
                                    Board.redraw_board(window, robber_pos, roll, current_player)
                            elif(len(current_player.roads) <= 2):
                                if(len(current_player.roads) == 0):
                                    Error.error_popup_place_roads(window)
                                    Board.redraw_board(window, robber_pos, roll, current_player)
                                elif current_player.roads[-1].is_placed is False:
                                    Error.error_popup_place_roads(window)
                                    Board.redraw_board(window, robber_pos, roll, current_player)
                            elif(len(current_player.settlements) < 2):
                                Error.error_popup_place_settlements(window)
                                Board.redraw_board(window, robber_pos, roll, current_player)
                                
                            print("error, all players need to place sett first")
                        else:
                            print("dice")
                            roll = [Dice.dice_roll(), Dice.dice_roll()]

                            # Acquire resources
                            for player in players:
                                print('aquiring')
                                player.acquire_cards(sum(roll))
                            Board.redraw_board(window, robber_pos, roll, current_player)

                            if sum(roll) == 7:
                                print("Robber")
                                Dice.dices(window, roll)
                                pygame.display.update()

                                # --- Move robber ---
                                robber_pos = Robber.move_robber_event(window, running)

                                # --- Update board ---
                                Board.redraw_board(window, robber_pos, roll, current_player)

                            else:  # Switch to next player
                                current_player = players[(players.index(current_player) + 1) % len(players)]
                                #time.sleep(3)
                                Board.redraw_board(window, robber_pos, roll, current_player)
                                # TODO switch to start of turn state
    #----------------------------------------------------------------------------------------------

                    if road_button.rect.collidepoint(mouse_pos):
                        print('buy road')
                        road_button.clicked = True

                    if settlement_button.rect.collidepoint(mouse_pos):
                        print('buy settlement')
                        road_button.clicked = True

                    """
                    if special_card_button.rect.collidepoint(mouse_pos):
                        print('buy special_card')
                        special_card_button.clicked = True
                    """

                    # TODO: after first click
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
                    print('enter place settlement')
                    # Place settlement event
                    SettlementEventHandler.place(window, robber_pos, roll, current_player, GAME_START)

                    if(settlement_button.clicked):
                        if Settlement.placement_is_possible(player, GAME_START) is False:
                            Error.error_popup_resources(window)
                            Board.redraw_board(window, robber_pos, roll, current_player)
                        else:
                            settlement_button.clicked_up = True
                            settlement_button.clicked = False

                    # TODO: Implement special cards
                    """
                    if(special_card_button.clicked):
                        if SpecialCard.placement_is_possible(player, GAME_START) is False:
                            Error.error_popup_resources(window)
                            Board.redraw_board(window, robber_pos, roll, current_player)
                        else:
                            special_card_button.clicked_up = True
                            special_card_button.clicked = False
                    """

                    # Release road event
                    print("entered")
                    if(road_button.clicked):
                        if Road.placement_is_possible(current_player, GAME_START) is False:
                            Error.error_popup_resources(window)
                            Board.redraw_board(window, robber_pos, roll, current_player)
                        else:
                            road_button.clicked_up = True
                            road_button.clicked = False
                    elif(road_button.clicked_up or GAME_START is True):
                        # If placing the road was unsuccessful, remove it from the list
                        if RoadEventHandler.place(window, event, current_player.current_road, current_player) == -1:
                            print('didnt work out')
                            #if(len(current_player.roads) != 0):
                             #   current_player.roads.pop()
                        else:
                            print('new road')
                            road_button.clicked_up = False
                            # If placing the road was successful, append it to the main list of roads as well
                            roads.append(current_player.current_road)
                        #road_button.clicked = False

                elif event.type == pygame.MOUSEMOTION:
                    # Dragging road event
                    #print('draggin')
                    RoadEventHandler.drag(window, pygame.mouse.get_pos(), current_player.current_road)

                # Hover settlement event TODO
                # SettlementEventHandler.hover_settlement(window, roll)

            # --- Dice ---

            dice_btn = Dice.roll_dice_btn(window)

            if dice_first_dsp:
                Dice.dices(window, [1, 1])
                dice_first_dsp = False

            Dice.dices(window, roll)

            pygame.display.update()

        pygame.quit()

    # TODO: remove this after testing
    if __name__ == "__main__":
        window = window_setup()
        main(window)
        exit()