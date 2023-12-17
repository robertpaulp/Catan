# Importing modules
import pygame
import time
import math
import random
import sys
from threading import Event

from BaseGame.Buttons.buttons import Button
from BaseGame.Board.board import Board
from BaseGame.CardsPrompt.cards_prompt import cards_prompt, CardsPrompt
from BaseGame.Dice.dice import Dice
from BaseGame.Hexagon_Tiles.hexagon_tile import HexagonTile
from BaseGame.Player.player import Player, players
from BaseGame.Road.road import Road, roads
from BaseGame.Robber.robber import Robber
from constants import *

class PopUp:
    @staticmethod
    def starting_round_popup(window):
        popup_image = pygame.image.load(POPUP_STARTING_ROUND_SPRITE)
        popup_image = pygame.transform.scale(popup_image, (383.4, 234))
        window.blit(popup_image, (500, 250))
        pygame.display.update()

        Event().wait(2)

    @staticmethod
    def round_number_popup(window, ROUND_NUMBER):
        #time.sleep(1)
        popup_image = pygame.image.load(POPUP_ROUND_NUMBER_SPRITE)
        popup_image = pygame.transform.scale(popup_image, (383.4, 234))
        window.blit(popup_image, (500, 250))
        font = pygame.freetype.SysFont('Segoe UI Black', 50)
        name_surface = font.render(str(ROUND_NUMBER), WHITE)
        window.blit(name_surface[0], (680, 385))
        pygame.display.update()

        Event().wait(2)

    @staticmethod
    def show_settlement_info(window):
        image = pygame.image.load(PAPIRUS_SETTLEMENT_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (SCREEN_WIDTH - 753, SCREEN_HEIGHT - 190))

    @staticmethod
    def show_road_info(window):
        image = pygame.image.load(PAPIRUS_ROAD_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (SCREEN_WIDTH - 573, SCREEN_HEIGHT - 190))