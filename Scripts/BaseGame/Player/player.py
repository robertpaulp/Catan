# Importing modules
import math
import pygame
import random
import sys
import numpy as np

sys.path.append("../../")
sys.path.append("../Hexagon Tiles/")

from constants import *
from BaseGame.Hexagon_Tiles.hexagon_tile import HexagonTile as hexagon
from BaseGame.Road.road import Road


class Player:
	image = pygame.Surface((PLAYER_BOARD_WIDTH, PLAYER_BOARD_HEIGHT), pygame.SRCALPHA)
	noPlayers = 1

	def __init__(self, color):
		self.name = f"Player {Player.noPlayers}"
		Player.noPlayers += 1

		self.color = color
		self.rolled = False

		self.resource_cards = 0
		self.special_cards = 0
		self.current_road = Road()

		# Gameplay attributes
		self.cards = {
			"Lumber": 0,
			"Grain": 0,
			"Wool": 0,
			"Bricks": 0,
			"Ore": 0
		}  # Dictionary of cards: key = resource, value = number of cards
		self.settlements = []
		self.roads = []

		self.possible_trade = {
			"Lumber": False,
			"Grain": False,
			"Wool": False,
			"Bricks": False,
			"Ore": False
		} 
		self.trade_counter = 0
		self.trade_button = []

		self.win_points = 0

	@staticmethod
	def draw_players(window):
		i = 0
		for player in players:
			# PLayer Icon
			pygame.draw.rect(player.image, player.color, (0, 0 + i * 130, ICON_SIZE, ICON_SIZE), 0)
			window.blit(player.image, ICON_POSITION)

			# Player Name
			font = pygame.freetype.SysFont('Segoe UI Black', 30)
			name_surface = font.render(player.name, BLACK)
			window.blit(name_surface[0], NAME_POSITION[i])

			# Win points banner
			image = pygame.image.load(POINTS_BANNER_SPRITE)
			image = pygame.transform.scale_by(image, 1)
			window.blit(image, (PLAYER_BOARD_X_AXIS + 120, PLAYER_BOARD_Y_AXIS + 50 + i * 130))

			# Win points Quantity
			font = pygame.freetype.SysFont('Arial', 25)
			win_points_quantity= font.render(str(player.win_points), BLACK)
			window.blit(win_points_quantity[0], (PLAYER_BOARD_X_AXIS + 175, PLAYER_BOARD_Y_AXIS + 52 + i * 130))

			# Player Resources

			# Resource Cards Icon

			image = pygame.image.load(CARDS_TOTAL_SPRITE)
			image = pygame.transform.scale_by(image, 1)
			window.blit(image, (RESOURCE_CARDS_POSITION[0] + ICON_SIZE + 10, RESOURCE_CARDS_POSITION[1] + i * 130 - 7 ))
			# Resource Cards Quantity
			font = pygame.freetype.SysFont('Arial', 25)
			resource_cards_quantity = font.render(str(player.resource_cards), BLACK)
			window.blit(resource_cards_quantity[0], (PLAYER_BOARD_X_AXIS + 175, RESOURCE_CARDS_POSITION[1] + i * 130 + 3))
			
			
			i = i + 1

	def acquire_cards(self, dice_roll):
		""" Acquires cards based on dice roll and settlement position

		:param dice_roll: Dice roll value
		:return: None
		"""
		for settlement in self.settlements:
			# If settlement is placed next to a hexagon with the dice roll associated to it, acquire resources
			if dice_roll in settlement.dice_rolls:
				resource = settlement.resources[settlement.dice_rolls.index(dice_roll)]
				self.cards[resource] += 1
				self.resource_cards += 1


# List of players
players = [Player(color=(255, 100, 100)), Player((230, 120, 0)), Player((51, 153, 255)), Player((110, 210, 0))]
