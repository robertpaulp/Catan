import time
from threading import Event

import pygame.draw

from Settlements.settlement import Settlement, settlements, sprites
from Player.player import Player
from constants import *

from Board.board import redraw_board


class SettlementEventHandler:
	def __init__(self):
		pass

	@staticmethod
	def hover_settlement(window, roll):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in settlements:
			if settlement.is_placed is False:
				if settlement.rect.collidepoint(mouse_pos) and settlement.is_hovered is False:
					settlement.hover_state(window)
				elif not settlement.rect.collidepoint(mouse_pos) and settlement.is_hovered is True:
					settlement.is_hovered = False
					redraw_board(window, roll)

	@staticmethod
	def press(window):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in settlements:
			if settlement.rect.collidepoint(mouse_pos) and settlement.is_placed is False:
				settlement.prepared_for_placement = True

	@staticmethod
	def place(window, roll, player: Player, GAME_START):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in settlements:
			# If mouse was released on the settlement we prepared, draw it
			if settlement.rect.collidepoint(mouse_pos) and settlement.prepared_for_placement is True:
				# Check if placement is possible
				if Settlement.placement_is_possible(player, GAME_START) is False:
					SettlementEventHandler.__error_popup(window, roll, player)
					settlement.prepared_for_placement = False
					return

				# Draw settlement sprite and change state
				settlement.draw_settlement(window, player.color)
				settlement.prepared_for_placement = False
				settlement.is_placed = True
				settlement.color = player.color

				# Add settlement to player's settlements
				player.settlements.append(settlement)
				sprites.add(settlement)

				# Spend resources
				if GAME_START is False:
					SettlementEventHandler.__buy_settlement(player)
					redraw_board(window, roll, player)

			# If mouse was not released on the settlement we prepared, reset its state
			elif settlement.prepared_for_placement is True:
				settlement.prepared_for_placement = False

	@staticmethod
	def __buy_settlement(player):
		""" Spend resources to buy settlement

		:param player:
		:return:
		"""

		player.cards["Wood"] -= 1
		player.cards["Brick"] -= 1
		player.cards["Sheep"] -= 1
		player.cards["Wheat"] -= 1

	@staticmethod
	def __error_popup(window, roll, player):
		err_image = pygame.image.load("../Assets/Sprites/saracie_error.png")
		err_image = pygame.transform.scale(err_image, (400, 100))
		window.blit(err_image, (0, 0))
		pygame.display.update()

		Event().wait(2)
		redraw_board(window, roll, player)
