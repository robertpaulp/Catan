import pygame
from Scripts.constants import *
from Scripts.base_game_cls import HexagonTile

settlement_img = pygame.Surface((SETTLEMENT_SPRITE * 3, SETTLEMENT_SPRITE * 3), pygame.SRCALPHA)
color = (200, 100, 23)
lowered_opacity_color = (200, 100, 23, 50)

class Settlement:
	settlements = []

	def __init__(self, window, position, color):
		""" Places settlement on the map

		"""

		self.image = pygame.Surface((SETTLEMENT_SPRITE * 3, SETTLEMENT_SPRITE * 3), pygame.SRCALPHA)
		self.rect = self.image.get_rect(center=position)
		self.position = position
		self.is_placed = False
		self.is_hovered = False
		self.color = color

	def draw_settlement(self, window):
		""" Draws settlement icon on the map

		:param window:
		:return:
		"""

		pygame.draw.circle(self.image, color, (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), SETTLEMENT_SPRITE, 0)

		window.blit(self.image, (self.position[0] - SETTLEMENT_SPRITE, self.position[1] - SETTLEMENT_SPRITE))
		pygame.display.update()

	def hover_state(self, window):
		""" Draw lowered-opacity version of settlement during mouse hover

		:param window:
		:return:
		"""

		pygame.draw.circle(self.image, (255, 0, 0, 20), (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), SETTLEMENT_SPRITE, 0)
		self.is_hovered = True
		self.image.set_alpha(50)

		window.blit(self.image, (self.position[0] - SETTLEMENT_SPRITE, self.position[1] - SETTLEMENT_SPRITE))
		pygame.display.update()

	@staticmethod
	def prepare_board_surfaces(window, nodes: tuple, opacity: int):
		""" Places possible settlement position surfaces on the map

		:param window: Window surface display
		:param nodes: Hexagon nodes
		:return: Dictionary containing (surface, position) elements
		"""

		for node in nodes:
			settlement = Settlement(window, node, color)
			cls.settlements.append(settlement)

			settlement.image.set_alpha(255)
			hover_area = pygame.draw.circle(settlement.image, (0, 0, 0, 0),
			                                (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), SETTLEMENT_SPRITE, 0)
			position = tuple(map(lambda x: x - SETTLEMENT_SPRITE, list(node)))

			window.blit(settlement.image, position)
			pygame.display.update()
