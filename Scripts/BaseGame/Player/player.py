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
		self.resource_cards = 0
		self.special_cards = 0
		self.current_road = Road()

		# Gameplay attributes
		self.cards = {
			"Wood": 0,
			"Wheat": 0,
			"Sheep": 0,
			"Brick": 0,
			"Ore": 0
		}  # Dictionary of cards: key = resource, value = number of cards
		self.settlements = []
		self.roads = []

		self.possible_trade = {
			"Wood": False,
			"Wheat": False,
			"Sheep": False,
			"Brick": False,
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
			name_surface = font.render(player.name, BROWN)
			window.blit(name_surface[0], NAME_POSITION[i])

			# Win points banner
			image = pygame.image.load(POINTS_BANNER_SPRITE)
			image = pygame.transform.scale_by(image, 1)
			window.blit(image, (PLAYER_BOARD_X_AXIS + 120, PLAYER_BOARD_Y_AXIS + 50 + i * 130))

			# Win points Quantity
			font = pygame.freetype.SysFont('Arial', 25)
			win_points_quantity= font.render(str(player.win_points), BROWN)
			window.blit(win_points_quantity[0], (PLAYER_BOARD_X_AXIS + 175, PLAYER_BOARD_Y_AXIS + 52 + i * 130))

			# Player Resources

			# Resource Cards Icon
			# TODO: Add resource card icon
			window.blit(player.image, RESOURCE_CARDS_POSITION)
			# Resource Cards Quantity
			font = pygame.freetype.SysFont('Arial', 25)
			resource_cards_quantity = font.render(str(player.resource_cards), BROWN)
			window.blit(resource_cards_quantity[0], (RESOURCE_CARDS_POSITION[0] + ICON_SIZE + 10, RESOURCE_CARDS_POSITION[1] + i * 130 + 5))
			
			
			i = i + 1

	# TODO : Delete this
	def draw_player(self, window):
		""" Draws player icon on the map

		:param window:
		:return:
		"""

		# PLayer Icon
		pygame.draw.rect(Player.image, self.color, (0, 0, ICON_SIZE, ICON_SIZE), 0)
		window.blit(Player.image, ICON_POSITION)

		# Player Name
		font = pygame.freetype.SysFont('Arial', 40)
		name_surface = font.render(self.name, (0, 0, 0))

		window.blit(name_surface[0], NAME_POSITION)

		# Player Resources

		# Wood
		pygame.draw.rect(Player.image, self.color, (0, 0, ICON_SIZE, ICON_SIZE), 0)
		window.blit(Player.image, WOOD_POSITION)
		# Quantity
		font = pygame.freetype.SysFont('Arial', 25)
		wood_surface = font.render(str(self.cards["Wood"]), (0, 0, 0))

		window.blit(wood_surface[0], (WOOD_POSITION[0] + ICON_SIZE + 10, WOOD_POSITION[1] + 5))

		# Wheat
		pygame.draw.rect(Player.image, self.color, (0, 0, ICON_SIZE, ICON_SIZE), 0)
		window.blit(Player.image, WHEAT_POSITION)
		# Quantity
		wheat_surface = font.render(str(self.cards["Wheat"]), (0, 0, 0))

		window.blit(wheat_surface[0], (WHEAT_POSITION[0] + ICON_SIZE + 10, WHEAT_POSITION[1] + 5))

		# Sheep
		pygame.draw.rect(Player.image, self.color, (0, 0, ICON_SIZE, ICON_SIZE), 0)
		window.blit(Player.image, SHEEP_POSITION)
		# Quantity
		sheep_surface = font.render(str(self.cards["Sheep"]), (0, 0, 0))

		window.blit(sheep_surface[0], (SHEEP_POSITION[0] + ICON_SIZE + 10, SHEEP_POSITION[1] + 5))

		# Brick
		pygame.draw.rect(Player.image, self.color, (0, 0, ICON_SIZE, ICON_SIZE), 0)
		window.blit(Player.image, BRICK_POSITION)
		# Quantity
		brick_surface = font.render(str(self.cards["Brick"]), (0, 0, 0))

		window.blit(brick_surface[0], (BRICK_POSITION[0] + ICON_SIZE + 10, BRICK_POSITION[1] + 5))

		# Ore
		pygame.draw.rect(Player.image, self.color, (0, 0, ICON_SIZE, ICON_SIZE), 0)
		window.blit(Player.image, ORE_POSITION)
		# Quantity
		ore_surface = font.render(str(self.cards["Ore"]), (0, 0, 0))

		window.blit(ore_surface[0], (ORE_POSITION[0] + ICON_SIZE + 10, ORE_POSITION[1] + 5))

		pygame.display.update()

	def acquire_cards(self, dice_roll):
		""" Acquires cards based on dice roll and settlement position

		:param dice_roll: Dice roll value
		:return: None
		"""
		print(dice_roll)
		for settlement in self.settlements:
			print(settlement.position)
			# If settlement is placed next to a hexagon with the dice roll associated to it, acquire resources
			if dice_roll in settlement.dice_rolls:
				resource = settlement.resources[settlement.dice_rolls.index(dice_roll)]
				self.cards[resource] += 1
				self.resource_cards += 1


# List of players
players = [Player(color=(255, 100, 100)), Player((230, 120, 0)), Player((51, 153, 255)), Player((110, 210, 0))]
