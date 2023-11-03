# Importing modules
import pandas as pd
import math
import numpy as np
import pygame
import game
import constants as c

# --- Hexagon class ---
class HexagonTile:

    # TODO: Create a class called HexagonTile
    # Create the tiles
    # !! Add the sprites to the tiles !!
    pass

# --- Settlement class ---
class Settlement:
    # TODO: Create a class called Settlement
    pass

# --- Road class ---
class Road:
    # TODO: Create a class called Road 
    pass

# --- Robber class ---
class Robber:
    # TODO: Create a class called Robber
    # Create the robber
    # Create the robber movement
    # Create the robber stealing
    # ADD card elimination if > 7 cards
    pass

# --- Dice class ---
class Dice:

    def dice_one(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)

    def dice_two(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    def dice_three(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)

    def dice_four(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    def dice_five(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)

    def dice_six(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    def create_dice(window, x, y):
        pygame.draw.rect(window, c.WHITE,(x, y, c.DICE_WIDTH, c.DICE_HEIGHT), 0, -1, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS)

    def dice_roll():
        dice = np.random.randint(1, 7)
        return dice
    
    def dice_display(face, window, x=c.DICE_X_AXIS, y=c.DICE_Y_AXIS):
        if face == 1:
            Dice.dice_one(window, x, y)
        elif face == 2:
            Dice.dice_two(window, x, y)
        elif face == 3:
            Dice.dice_three(window, x, y)
        elif face == 4:
            Dice.dice_four(window, x, y)
        elif face == 5:
            Dice.dice_five(window, x, y)
        elif face == 6:
            Dice.dice_six(window, x, y)
        else:
            print("Error")

    def dice(window, x=c.DICE_X_AXIS, y=c.DICE_Y_AXIS):
        dice = Dice.dice_roll()
        Dice.create_dice(window, x, y)
        Dice.dice_display(dice, window, x, y)


# --- Card class ---
class Card:
    # TODO: Create a class called Card
    # Create the cards

    pass

# --- Player class ---
class Player:
    # TODO: Create a class called Player
    pass

# --- Board class ---
class Board:
    # TODO: Create a class called Board
    # Incorporate all the classes and create the board
    pass