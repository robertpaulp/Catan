import pygame.draw

from base_game_cls import Settlement
from base_game_cls import HexagonTile
from constants import *
import time


class SettlementHover:
	def __init__(self):
		pass

	def trigger(self, window):
		for node in HexagonTile.hexagon_points:
			hover_area = pygame.draw.circle(window, (0, 0, 0, 0), node, SETTLEMENT_SPRITE, 0)

			if hover_area.collidepoint(pygame.mouse.get_pos()):
				print(time.time())
