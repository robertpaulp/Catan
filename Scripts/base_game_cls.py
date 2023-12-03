# Importing modules
import pandas as pd
import math
import numpy as np
import pygame
import game
import constants as c

# --- Hexagon class ---
class HexagonTile:

    def create_hexagon(window, x = c.HEXAGON_X_CENTER, y = c.HEXAGON_Y_CENTER, image = None):
        vertices = [

            # (x - c.HEXAGON_SIDE, y),
            # (x, y - (0.866 * c.HEXAGON_SIDE)),
            # (x + c.HEXAGON_SIDE, y),
            # (x + c.HEXAGON_SIDE, y + c.HEXAGON_SIDE),
            # (x, y + (0.866 * c.HEXAGON_SIDE) + c.HEXAGON_SIDE),
            # (x - c.HEXAGON_SIDE, y + c.HEXAGON_SIDE)

            (x - c.HEXAGON_SIDE, y),
            (x, y - c.HEXAGON_SIDE),
            (x + c.HEXAGON_SIDE, y),
            (x + c.HEXAGON_SIDE, y + c.HEXAGON_SIDE),
            (x, y + 2 * c.HEXAGON_SIDE),
            (x - c.HEXAGON_SIDE, y + c.HEXAGON_SIDE)
            
        ]

        if image is not None:
            image = pygame.transform.scale(image, (c.HEXAGON_WIDTH, c.HEXAGON_HEIGHT * 1.5))

            cropped = pygame.sprite.Sprite(image)

            cropped.blit(image, (0, 0), (0, 0, c.HEXAGON_WIDTH, c.HEXAGON_HEIGHT * 1.5))
            window.blit(image, (x - c.HEXAGON_SIDE, y - c.HEXAGON_SIDE))
        else:
            pygame.draw.polygon(window, c.WHITE, vertices, 0)

        pygame.draw.polygon(window, c.BLACK, vertices, 4)


    def create_hexagon_grid(window, x, y, hexagon_numbers):

        # Create the first row
        HexagonTile.create_row(window, x, y, hexagon_numbers, 3)

        # Create the second row
        x = c.HEXAGON_X_AXIS - c.HEXAGON_WIDTH / 2
        y += c.HEXAGON_HEIGHT 
        HexagonTile.create_row(window, x, y, hexagon_numbers, 4)

        # Create the third row
        x = c.HEXAGON_X_AXIS - c.HEXAGON_WIDTH
        y += c.HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, hexagon_numbers, 5)
        
        # Create the fourth row
        x = c.HEXAGON_X_AXIS - c.HEXAGON_WIDTH / 2 
        y += c.HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, hexagon_numbers, 4)

        # Create the fifth row
        x = c.HEXAGON_X_AXIS
        y += c.HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, hexagon_numbers, 3)
        
    def add_hexagon_number(window, x, y, number):
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(str(number), True, c.BLACK)
        text_rect = text.get_rect(center=(x, y + c.HEXAGON_SIDE / 2 - 5))
        pygame.draw.circle(window, c.BEIGE, (x, y + c.HEXAGON_SIDE / 2), c.HEXAGON_SIDE / 3, 0)
        pygame.draw.circle(window, c.BLACK, (x, y + c.HEXAGON_SIDE / 2), c.HEXAGON_SIDE / 3, 1)
        window.blit(text, text_rect)

    def create_row(window, x, y, hexagon_numbers, rows):
        for row in range(0, rows):
            HexagonTile.create_hexagon(window, x, y)
            number = hexagon_numbers.pop(0)
            if HexagonTile.check_for_desert(number):
                HexagonTile.add_hexagon_number(window, x, y, number)
            x += c.HEXAGON_WIDTH


    def check_for_desert(number):
        if number == -1:
            return False
        else:
            return True


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

    @staticmethod
    def dice_one(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)

    @staticmethod
    def dice_two(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    @staticmethod
    def dice_three(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)

    @staticmethod
    def dice_four(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    @staticmethod
    def dice_five(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)

    @staticmethod
    def dice_six(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    @staticmethod
    def create_dice(window, x, y):
        pygame.draw.rect(window, c.WHITE,(x, y, c.DICE_WIDTH, c.DICE_HEIGHT), 0, -1, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS)

    @staticmethod
    def dice_roll():
        dice = np.random.randint(1, 7)
        return dice

    @classmethod
    def dice_display_face(cls, face, window, x=c.DICE_X_AXIS, y=c.DICE_Y_AXIS):
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

    @classmethod
    def dices(cls, window, roll, x= c.DICE_X_AXIS, y= c.DICE_Y_AXIS):
        if roll[0] != 0:
            Dice.create_dice(window, x, y)
            Dice.dice_display_face(roll[0], window, x, y)

        if roll[1] != 0:
            Dice.create_dice(window, x + 90, y)
            Dice.dice_display_face(roll[1], window, x + 90, y)


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

    def roll_dice_btn(window, x=c.DICE_BTN_X_AXIS, y=c.DICE_BTN_Y_AXIS):
        button = pygame.draw.rect(window, c.BEIGE, (x, y, c.DICE_BTN_WIDTH, c.DICE_BTN_HEIGHT))
        pygame.draw.rect(window, c.BLACK, (x, y, c.DICE_BTN_WIDTH, c.DICE_BTN_HEIGHT), 4)
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(str("Roll Dice!"), True, c.BLACK)
        text_rect = text.get_rect(center=(x + 100, y + 25))
        window.blit(text, text_rect)
        return button
