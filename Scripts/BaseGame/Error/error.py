# Importing modules
import pygame
import time
import math
import random
import sys
from threading import Event
from constants import *

class Error:

    waiting_time = 1

    @staticmethod
    def error_popup_resources(window):
        err_image = pygame.image.load(ERROR_RESOURCE_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(Error.waiting_time)

    @staticmethod
    def error_popup_place_roads(window):
        err_image = pygame.image.load(ERROR_PLACE_ROADS_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(Error.waiting_time)

    @staticmethod
    def error_popup_place_settlements(window):
        err_image = pygame.image.load(ERROR_PLACE_SETTLEMENTS_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(Error.waiting_time)

    @staticmethod
    def error_popup_place_settlements_roads(window):
        err_image = pygame.image.load(ERROR_PLACE_SETTLEMENTS_ROADS_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(Error.waiting_time)

    @staticmethod
    def error_popup_roll_dice(window):
        err_image = pygame.image.load(ERROR_ROLL_DICE_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(Error.waiting_time)

    @staticmethod
    def error_popup_already_rolled(window):
        err_image = pygame.image.load(ERROR_ALREADY_ROLLED_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(Error.waiting_time)

    @staticmethod
    def error_popup_robber(window):
        err_image = pygame.image.load(ERROR_ROBBER_SPRITE)
        err_image = pygame.transform.scale(err_image, (400, 100))
        window.blit(err_image, (0, 0))
        pygame.display.update()

        Event().wait(Error.waiting_time)
        pygame.draw.rect(window, BRASS, (0, 0, 405, 105))
        pygame.display.update()