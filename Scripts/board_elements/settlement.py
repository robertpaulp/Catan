import pygame
from Scripts.constants import *
from Scripts.base_game_cls import HexagonTile

settlement_img = pygame.Surface((SETTLEMENT_SPRITE * 3, SETTLEMENT_SPRITE * 3), pygame.SRCALPHA)


class Settlement:
	settlements = []

	def __init__(self, window, position):
		""" Places settlement on the map

		"""

		self.image = pygame.Surface((SETTLEMENT_SPRITE * 3, SETTLEMENT_SPRITE * 3), pygame.SRCALPHA)
		self.rect = self.image.get_rect(center=position)
		self.position = position

		self.__draw_settlement(window)

	def __draw_settlement(self, window):
		""" Draws settlement icon on the map

		:param window:
		:return:
		"""

		# pygame.draw.circle(window, (255, 50, 255), self.center, SETTLEMENT_SPRITE, 0)

	@classmethod
	def prepare_board_surfaces(cls, window, nodes: tuple, opacity: int):
		""" Places possible settlement position surfaces on the map

		:param window: Window surface display
		:param nodes: Hexagon nodes
		:return: Dictionary containing (surface, position) elements
		"""

		settlement_locations = {}

		for node in nodes:
			settlement = Settlement(window, node)
			# settlement.image = pygame.Surface((SETTLEMENT_SPRITE * 3, SETTLEMENT_SPRITE * 3), pygame.SRCALPHA)

			cls.settlements.append(settlement)

			settlement.image.set_alpha(0)
			hover_area = pygame.draw.circle(settlement.image, (255, 0, 0, 255),
			                                (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), SETTLEMENT_SPRITE, 0)
			position = tuple(map(lambda x: x - SETTLEMENT_SPRITE, list(node)))

			settlement_locations[settlement.image] = position

			window.blit(settlement.image, position)
			pygame.display.update()

		return settlement_locations
