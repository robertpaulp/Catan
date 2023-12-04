import pygame
from Scripts.constants import *
from Scripts.base_game_cls import HexagonTile


class Player:
	def __init__(self):
		# Gameplay attributes
		self.cards = {}  # Dictionary of cards: key = resource, value = number of cards
		self.settlements = []
		self.roads = []

		self.win_points = 0

	def acquire_cards(self, dice_roll):
		""" Acquires cards based on dice roll and settlement position

		:param dice_roll: Dice roll value
		:return: None
		"""

		for settlement in self.settlements:
			# If settlement is placed next to a hexagon with the dice roll associated to it, acquire resources
			if dice_roll in settlement.dice_rolls:
				for resource in settlement.resources:
					self.cards[resource] += 1

