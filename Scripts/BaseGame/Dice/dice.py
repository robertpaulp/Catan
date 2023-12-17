# Importing modules
import math
import pygame
import random
import sys
import numpy as np
from threading import Event

sys.path.append("../../")

from constants import *

# --- Dice class ---
class Dice:

    def dice_one(window, x, y):
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_CENTER, y + DOT_OFFSET_CENTER), DOT_RADIUS, 0)

    def dice_two(window, x, y):
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_UP), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_DOWN), DOT_RADIUS, 0)

    def dice_three(window, x, y):
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_DOWN), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_CENTER, y + DOT_OFFSET_CENTER), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_UP), DOT_RADIUS, 0)

    def dice_four(window, x, y):
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_UP), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_DOWN), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_UP), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_DOWN), DOT_RADIUS, 0)

    def dice_five(window, x, y):
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_UP), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_DOWN), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_UP), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_DOWN), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_CENTER, y + DOT_OFFSET_CENTER), DOT_RADIUS, 0)

    def dice_six(window, x, y):
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_UP), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_CENTER), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_UP, y + DOT_OFFSET_DOWN), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_UP), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_CENTER), DOT_RADIUS, 0)
        pygame.draw.circle(window, BLACK, (x + DOT_OFFSET_DOWN, y + DOT_OFFSET_DOWN), DOT_RADIUS, 0)

    def create_dice(window, x, y):
        pygame.draw.rect(window, WHITE,(x, y, DICE_WIDTH, DICE_HEIGHT), 0, -1, DICE_CORNER_RADIUS, DICE_CORNER_RADIUS, DICE_CORNER_RADIUS, DICE_CORNER_RADIUS)

    def dice_roll():
        dice = np.random.randint(1, 7)
        return dice
    
    def dice_display_face(face, window, x=DICE_X_AXIS, y=DICE_Y_AXIS):
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

    def dices(window, roll, x= DICE_X_AXIS, y= DICE_Y_AXIS):
        if roll[0] != 0:
            Dice.create_dice(window, x, y)
            Dice.dice_display_face(roll[0], window, x, y)

        if roll[1] != 0:
            Dice.create_dice(window, x + 90, y)
            Dice.dice_display_face(roll[1], window, x + 90, y)

    def roll_dice_btn(window, x=DICE_BTN_X_AXIS, y=DICE_BTN_Y_AXIS):
        button = pygame.draw.rect(window, BEIGE, (x, y, DICE_BTN_WIDTH, DICE_BTN_HEIGHT))
        pygame.draw.rect(window, BLACK, (x, y, DICE_BTN_WIDTH, DICE_BTN_HEIGHT), 4)
        font = pygame.font.SysFont('Segoe UI Black', 28)
        text = font.render(str("Roll Dice!"), True, BLACK)
        text_rect = text.get_rect(center=(x + 100, y + 25))
        window.blit(text, text_rect)
        return button