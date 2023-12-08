# Importing modules
import math
import pygame
import random
import sys
import numpy as np

sys.path.append("../../")
sys.path.append("../Hexagon Tiles/")

from constants import *
from Hexagon_Tiles import HexagonTile as hexagon


class Player:
	image = pygame.Surface((PLAYER_BOARD_WIDTH, PLAYER_BOARD_HEIGHT), pygame.SRCALPHA)
	noPlayers = 1

	def __init__(self, color):
		self.name = f"Player {Player.noPlayers}"
		Player.noPlayers += 1

		self.color = color

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

		self.win_points = 0

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

		for settlement in self.settlements:
			# If settlement is placed next to a hexagon with the dice roll associated to it, acquire resources
			if dice_roll in settlement.dice_rolls:
				resource = settlement.resources[settlement.dice_rolls.index(dice_roll)]
				self.cards[resource] += 1


# List of players
players = [Player(color=(255, 0, 0)), Player((230, 120, 0)), Player((0, 0, 255)), Player((0, 255, 0))]
