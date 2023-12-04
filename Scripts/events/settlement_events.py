import pygame.draw

from Scripts.board_elements.settlement import Settlement, settlements
from Scripts.player.player import Player
from Scripts.constants import *
import time


class SettlementEventHandler:
	def __init__(self):
		pass

	@staticmethod
	def hover_settlement(window):
		for settlement in settlements:
			if settlement.rect.collidepoint(pygame.mouse.get_pos()) and settlement.is_hovered is False:
				print("ceva")
				settlement.hover_state(window)

	@staticmethod
	def press(window):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in settlements:
			if settlement.rect.collidepoint(mouse_pos) and settlement.is_placed is False:
				settlement.prepared_for_placement = True

	@staticmethod
	def place(window, player: Player):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in settlements:
			# If mouse was released on the settlement we prepared, draw it
			if settlement.rect.collidepoint(mouse_pos) and settlement.prepared_for_placement is True:
				# Draw settlement sprite and change state
				settlement.draw_settlement(window)
				settlement.prepared_for_placement = False
				settlement.is_placed = True

				# Add settlement to player's settlements
				player.settlements.append(settlement)

			# If mouse was not released on the settlement we prepared, reset its state
			elif settlement.prepared_for_placement is True:
				settlement.prepared_for_placement = False
