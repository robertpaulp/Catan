# Importing modules
import math
import pygame
import random
import sys
import numpy as np

sys.path.append("../../")
sys.path.append("../Hexagon_Tiles/")

from constants import *
from BaseGame.Hexagon_Tiles.hexagon_tile import HexagonTile as hexagon
from BaseGame.Error.error import Error
from BaseGame.Player.player import Player, players


# --- Robber class ---
class Robber:

    current_pos = (0,0)

    def delete_cards():
        for player in players:
            if player.resource_cards >= 7:
                numberToDelete = math.floor(player.resource_cards / 2)
                player.resource_cards -= numberToDelete
                for card in player.cards:
                    if numberToDelete == 0:
                        break
                    if player.cards[card] > 0:
                        player.cards[card] -= 1
                        numberToDelete -= 1


    def get_image():
        image = pygame.image.load(ROBBER_SPRITE)
        image = pygame.transform.scale(image, (HEXAGON_SIDE * 1.2, HEXAGON_SIDE * 1.2))

        return image

    # You can't move the robber in the same tile
    def check_move(mouse_pos):
        range_x = [Robber.current_pos[0] - HEXAGON_SIDE/3, Robber.current_pos[0] + HEXAGON_SIDE/3]
        range_y = [Robber.current_pos[1] - HEXAGON_SIDE/3, Robber.current_pos[1] + HEXAGON_SIDE/3]

        if (range_x[0] <= mouse_pos[0] <= range_x[1] and range_y[0] <= mouse_pos[1] <= range_y[1]):
            return False
        return True

    def create_robber(window):
        index = hexagon.get_index("Desert")
        Robber.current_pos = hexagon.center_points[index]

        image = Robber.get_image()
        
        window.blit(image, (hexagon.center_points[index][0] - HEXAGON_SIDE/1.8, hexagon.center_points[index][1] - HEXAGON_SIDE / 2))


    def move_robber(window, robber_pos):
        Robber.current_pos = robber_pos
        image = Robber.get_image()
        
        window.blit(image, (robber_pos[0] - HEXAGON_SIDE/1.8, robber_pos[1] - HEXAGON_SIDE / 2))
        

    def move_robber_event(window, running, dice_btn):
        moved_robber = False

        while not moved_robber:
            for inner_event in pygame.event.get():
                if inner_event.type == pygame.QUIT:
                    running = False
                    return None

                elif inner_event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if dice_btn.collidepoint(mouse_pos):
                        Error.error_popup_robber(window)

                    for center_point in hexagon.center_points:
                        range_x = [center_point[0] - HEXAGON_SIDE / 3, center_point[0] + HEXAGON_SIDE / 3]
                        range_y = [center_point[1] - HEXAGON_SIDE / 3, center_point[1] + HEXAGON_SIDE / 3]

                        if (range_x[0] <= mouse_pos[0] <= range_x[1] and range_y[0] <= mouse_pos[1] <= range_y[1]):
                            if Robber.check_move(mouse_pos):
                                Robber.move_robber(window, center_point)
                                robber_pos = center_point
                                moved_robber = True
                                break

        Robber.delete_cards()
        return robber_pos