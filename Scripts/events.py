import pygame.draw

from board_elements.settlement import *
from game import redraw_board
from base_game_cls import HexagonTile
from constants import *
import time


class SettlementHover:
	def __init__(self):
		pass

	@staticmethod
	def trigger(window):
		for settlement in Settlement.settlements:
			if settlement.rect.collidepoint(pygame.mouse.get_pos()) and settlement.is_hovered is False:
				print("ceva")
				settlement.hover_state(window)

			# else:
			# 	redraw_board(window)
