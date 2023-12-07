# Importing modules
import pygame
import random
import sys

sys.path.append("Base Game/Board/")
sys.path.append("Base Game/Hexagon Tiles/")
sys.path.append("Base Game/Robber/")
sys.path.append("Base Game/Dice/")

from board import Board as board
from hexagon_tile import HexagonTile as hexagon
from robber import Robber as robber
from dice import Dice as dice
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

        # --- Player ---
        # current_player = players[0]  # Current player

        # current_player.draw_player(window)

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