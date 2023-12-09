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
from BaseGame.Road.road_events import RoadEventHandler
from BaseGame.Robber.robber import Robber
from constants import *

class Error:
    @staticmethod
    def error_popup_resources(window):
        err_image = pygame.image.load(ERROR_RESOURCE_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(2)
        # Redraw after every error!!!
        # Board.redraw_board(window, roll, player)

    @staticmethod
    def error_popup_place_roads(window):
        err_image = pygame.image.load(ERROR_PLACE_ROADS_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(2)

    @staticmethod
    def error_popup_place_settlements(window):
        err_image = pygame.image.load(ERROR_PLACE_SETTLEMENTS_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(2)

    @staticmethod
    def error_popup_place_settlements_roads(window):
        err_image = pygame.image.load(ERROR_PLACE_SETTLEMENTS_ROADS_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(2)

    @staticmethod
    def error_popup_robber(window):
        err_image = pygame.image.load(ERROR_ROBBER_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(2)