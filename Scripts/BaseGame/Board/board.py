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
from BaseGame.Dice.dice import Dice
from BaseGame.Hexagon_Tiles.hexagon_tile import HexagonTile
from BaseGame.Settlements.settlement import Settlement, settlements, sprites
from BaseGame.Road.road import Road, roads
from BaseGame.Player.player import Player, players
from BaseGame.Robber.robber import Robber
from BaseGame.Buttons.buttons import Button
from BaseGame.CardsPrompt.cards_prompt import cards_prompt, CardsPrompt
from BaseGame.Trade.trade import trade

# --- Board class ---
class Board:
    # TODO: Create a class called Board
    # Incorporate all the classes and create the board

    def redraw_board(window, robber_pos, roll, current_player=players[0], GAME_START = False):
        window.fill(BRASS)

        dice_btn = Dice.roll_dice_btn(window)

        if roll == [0, 0]:
            Dice.dices(window, [1, 1])

        Dice.dices(window, roll)

        HexagonTile.draw_sea_hexagon(window, SCREEN_WIDTH / 2 - HEXAGON_WIDTH / 2 - HEXAGON_WIDTH - 50, HEXAGON_Y_AXIS - 55)

        HexagonTile.create_hexagon_grid(window, HEXAGON_X_AXIS, HEXAGON_Y_AXIS, False)

        if GAME_START is False:
            # --- Buttons ---
            road_button = Button.create_road_button()
            road_button.draw(window)
            settlement_button = Button.create_settlement_button()
            settlement_button.draw(window)
            special_card_button = Button.create_special_card_button()
            special_card_button.draw(window)

        # --- Cards prompt ---
        cards_prompt.show_cards(window, current_player)

        # --- Trade prompt ---
        trade.show_trade(window, current_player)

        # Move robber
        if(robber_pos[0] != -1):
            Robber.move_robber(window, robber_pos)
        else:
            Robber.create_robber(window)
        
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
        Player.draw_players(window)