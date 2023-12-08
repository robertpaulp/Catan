# Importing modules
import math
import pygame
import random
import sys

sys.path.append("../../")
sys.path.append("../Hexagon Tiles/")
sys.path.append("../Robber/")

import pygame

from constants import *
from Dice.dice import Dice
from Hexagon_Tiles.hexagon_tile import HexagonTile, Board, Dice
from Settlements.settlement import Settlement, settlements, sprites
from Road.road import Road, roads
from Player.player import Player, players

# --- Board class ---
class Board:
    # TODO: Create a class called Board
    # Incorporate all the classes and create the board

    def redraw_board(window, robber_pos):
        window.fill(LIGHT_CYAN_BLUE)

        dice_btn = Board.roll_dice_btn(window)

        if roll == [0, 0]:
        Dice.dices(window, [1, 1])

        Dice.dices(window, roll)

        hexagon.create_hexagon_grid(window, HEXAGON_X_AXIS, HEXAGON_Y_AXIS, False)

        # Move robber
        robber.move_robber(window, robber_pos)
        pygame.display.update()

         # Replace roads
        for road in roads:
            if road.is_placed is True:
                road.draw_road(window, road.color)

         # Replace settlements
        for settlement in settlements:
            if settlement.is_placed is True:
                settlement.draw_settlement(window, settlement.color)

            window.blit(settlement.image,
                        (settlement.position[0] - SETTLEMENT_SPRITE, settlement.position[1] - SETTLEMENT_SPRITE))
            pygame.display.update()

        # sprites.draw(window)
        # pygame.display.update()

        # Update player's resources
        current_player.draw_player(window)