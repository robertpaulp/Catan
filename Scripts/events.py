import pygame.draw

from board_elements.settlement import *
from game import redraw_board
from base_game_cls import HexagonTile
from constants import *
import time


class SettlementEventHandler:
	def __init__(self):
		pass

	@staticmethod
	def trigger(window):
		for settlement in Settlement.settlements:
			if settlement.rect.collidepoint(pygame.mouse.get_pos()) and settlement.is_hovered is False:
				print("ceva")
				settlement.hover_state(window)

	@staticmethod
	def handle_settlement_placement(window):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in Settlement.settlements:  # TODO: move to event handler
			if settlement.rect.collidepoint(mouse_pos) and settlement.is_placed is False:
				settlement.draw_settlement(window)
				settlement.is_placed = True
