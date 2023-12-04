import pygame
from Scripts.constants import *

roads = []  # List of all roads


class Road:

	def __init__(self):
		self.is_placed = False

		self.is_dragged = False

		self.start = [0, 0]
		self.end = [0, 0]
		self.borders = []  # List of settlement borders that the road is connected to

	def draw_road(self, window):
		""" Draws road on the screen

		:param window: Display window
		:return: None
		"""

		pygame.draw.line(window, (200, 50, 0), self.start, self.end, 7)

		# Redraw start settlement so that it is not covered by the road
		settlement = self.borders[0]
		settlement.draw_settlement(window)

		window.blit(settlement.image,
		            (settlement.position[0] - SETTLEMENT_SPRITE, settlement.position[1] - SETTLEMENT_SPRITE))
		pygame.display.update()
