# Importing modules
import pygame
import random
import sys
"""
sys.path.append("./BaseGame/Board/")
sys.path.append("./BaseGame/Hexagon Tiles/")
sys.path.append("./BaseGame/Robber/")
sys.path.append("./BaseGame/Dice/")"""
from Scripts.BaseGame.Board import board
from Scripts.BaseGame.Buttons import Button, button
from Scripts.BaseGame.CardsPrompt import cards_prompt, CardsPrompt
from Scripts.BaseGame.Dice import Dice, dice
from Scripts.BaseGame.Hexagon_Tiles import hexagon_tile, hexagon
from Scripts.BaseGame.Player import Player, players
from Scripts.BaseGame.Road import Road, road, road_events
from Scripts.BaseGame.Robber import Robber, robber
from Scripts.BaseGame.Settlements import settlement, settlement_event
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

        # --- Background ---
        window.fill(LIGHT_CYAN_BLUE)

        # --- Hexagon grid ---
        hexagon.create_hexagon_grid(window, HEXAGON_X_AXIS, HEXAGON_Y_AXIS)

        # --- Robber ---
        robber.create_robber(window)

        # --- Settlement Surfaces ---
        # Settlement.prepare_board_surfaces(window, base.HexagonTile.distinct_vertices, base.HexagonTile.hexagons)

        # --- Cards prompt ---
        cards_prompt.show_cards(window, current_player)

        # --- Buttons ---
        road_button = Button.create_road_button()
        road_button.draw(window)
        settlement_button = Button.create_settlement_button()
        settlement_button.draw(window)
        special_card_button = Button.create_special_card_button()
        special_card_button.draw(window)

        # --- Player ---
        current_player = players[0]  # Current player

        current_player.draw_player(window)

        while running:
            # --- Event loop ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if dice_btn.collidepoint(mouse_pos):
                        roll = [dice.dice_roll(), dice.dice_roll()]

                        if sum(roll) == 7:                            
                            # --- Update dice roll before moving robber ---
                            dice.dices(window, roll)
                            pygame.display.update()

                            # --- Move robber ---
                            robber_pos = robber.move_robber_event(window, running)

                            # --- Update board ---
                            board.redraw_board(window, robber_pos)


            # --- Dice ---
            dice_btn = dice.roll_dice_btn(window)

            if dice_first_dsp:
                dice.dices(window, [1, 1])
                dice_first_dsp = False

            dice.dices(window, roll)

            pygame.display.update()

        pygame.quit()

    # TODO: remove this after testing
    if __name__ == "__main__":
        window = window_setup()
        main(window)
        exit()