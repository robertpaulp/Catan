import pygame.draw

from Scripts.board_elements.settlement import *
from Scripts.player.player import Player
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
	def place_settlement(window, settlements: list, player: Player, action: str):
		mouse_pos = pygame.mouse.get_pos()

		match action:
			case "prepared":
				for settlement in settlements:
					if settlement.rect.collidepoint(mouse_pos) and settlement.is_placed is False:
						settlement.prepared_for_placement = True

			case "placing":
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
