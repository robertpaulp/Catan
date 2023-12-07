# Importing modules
import math
import pygame
import random
import sys

sys.path.append("../../")
sys.path.append("../Hexagon Tiles/")
sys.path.append("../Robber/")

from constants import *
from hexagon_tile import HexagonTile as hexagon
from robber import Robber as robber

# --- Board class ---
class Board:
    # TODO: Create a class called Board
    # Incorporate all the classes and create the board

    def redraw_board(window, robber_pos):
        window.fill(LIGHT_CYAN_BLUE)
        hexagon.create_hexagon_grid(window, HEXAGON_X_AXIS, HEXAGON_Y_AXIS, False)
        robber.move_robber(window, robber_pos)
        pygame.display.update()