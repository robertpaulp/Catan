import pygame


class Road:
	def __init__(self):
		self.image = None
		self.rect = self.image.get_rect()
		self.is_placed = False

		self.is_dragged = False

		self.start = [0, 0]
		self.end = [0, 0]
		self.borders = []  # List of settlement borders that the road is connected to
