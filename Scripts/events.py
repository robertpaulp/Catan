import pygame.draw

from board_elements import settlement
from base_game_cls import HexagonTile
from constants import *
import time


class SettlementHover:
	def __init__(self):
		pass

	@staticmethod
	def trigger(hover_areas, window):
		for surface, position in hover_areas.items():
			settlement_area = surface.get_rect(topleft=position)

			if settlement_area.collidepoint(pygame.mouse.get_pos()):
				print("ceva")
				# pygame.transform.scale(area, (0, 0))
