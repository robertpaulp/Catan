import pygame
from Scripts.constants import *
from Scripts.base_game_cls import HexagonTile


class Player:
	def __init__(self):
		# Gameplay attributes
		self.cards = []  # List of (card, quantity) tuples
		self.settlements = []
		self.roads = []

		self.points = 0

	def acquire_card(self, card):
		self.cards.append(card)

