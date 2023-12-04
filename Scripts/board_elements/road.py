import pygame

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

		pygame.draw.line(window, (0, 0, 0), self.start, self.end, 5)
