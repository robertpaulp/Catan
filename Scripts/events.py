import pygame.draw

from board_elements import settlement
from base_game_cls import HexagonTile
from constants import *
import time


class SettlementHover:
	def __init__(self):
		pass

	def trigger(self, hover_areas, window):
		for area in hover_areas:
			if area.collidepoint(pygame.mouse.get_pos()):
				print(time.time())
				# pygame.transform.scale(area, (0, 0))
