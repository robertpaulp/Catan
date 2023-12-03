import pygame
from Scripts.constants import *
from Scripts.base_game_cls import HexagonTile


def prepare_board_surfaces(window, nodes):
	settlement_locations = {}

	for node in nodes:
		surface = pygame.Surface((SETTLEMENT_SPRITE + 10, SETTLEMENT_SPRITE + 10), pygame.SRCALPHA)
		hover_area = pygame.draw.circle(surface, (255, 0, 0, 50), (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), 10, 0)
		position = tuple(map(lambda x: x - 10, list(node)))

		# settlement_locations.append(hover_area)
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
