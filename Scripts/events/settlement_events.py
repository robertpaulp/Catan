import pygame.draw

from Scripts.board_elements.settlement import *
from Scripts.constants import *
import time


class SettlementEventHandler:
	def __init__(self):
		pass

	@staticmethod
	def hover_settlement(window):
		for settlement in Settlement.settlements:
			if settlement.rect.collidepoint(pygame.mouse.get_pos()) and settlement.is_hovered is False:
				print("ceva")
				settlement.hover_state(window)

	@staticmethod
	def settlement_placement(window):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in Settlement.settlements:
			if settlement.rect.collidepoint(mouse_pos) and settlement.is_placed is False:
				# Draw settlement sprite and change state
				settlement.draw_settlement(window)
				settlement.is_placed = True
