import pygame
from Scripts.constants import *
from Scripts.base_game_cls import HexagonTile


def prepare_board_surfaces(window, nodes):
	""" Places possible settlement position surfaces on the map

	:param window:
	:param nodes: Hexagon nodes
	:return: Dictionary containing (surface, position) elements
	"""

	settlement_locations = {}

	for node in nodes:
		surface = pygame.Surface((SETTLEMENT_SPRITE * 2, SETTLEMENT_SPRITE * 2), pygame.SRCALPHA)
		hover_area = pygame.draw.circle(surface, (255, 0, 0, 50), (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), 10, 0)
		position = tuple(map(lambda x: x - SETTLEMENT_SPRITE, list(node)))

		settlement_locations[surface] = position

		window.blit(surface, position)
		pygame.display.update()

	return settlement_locations


class Settlement:
	def __init__(self, placement_node: tuple, window):
		""" Places settlement on the map

		:param placement_node: Position of the desired settlement
		"""

		self.center = placement_node

		self.__draw_settlement(window)

	def __draw_settlement(self, window):
		""" Draws settlement icon on the map

		:param window:
		:return:
		"""
		pygame.draw.circle(window, (255, 50, 255), self.center, SETTLEMENT_SPRITE, 0)
