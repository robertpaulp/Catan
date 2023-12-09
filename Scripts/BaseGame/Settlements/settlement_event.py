import time
from threading import Event

import pygame.draw

from BaseGame.Settlements.settlement import Settlement, settlements, sprites
from BaseGame.Player.player import Player
from BaseGame.Error.error import Error
from constants import *

from BaseGame.Board.board import Board


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
					Board.redraw_board(window, roll)

	@staticmethod
	def press(window):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in settlements:
			if settlement.rect.collidepoint(mouse_pos) and settlement.is_placed is False:
				settlement.prepared_for_placement = True

	@staticmethod
	def place(window, robber_pos, roll, player: Player, GAME_START):
		mouse_pos = pygame.mouse.get_pos()

		for settlement in settlements:
			# If mouse was released on the settlement we prepared, draw it
			if settlement.rect.collidepoint(mouse_pos) and settlement.prepared_for_placement is True:
				# Check if placement is possible
				if Settlement.placement_is_possible(player, GAME_START) is False:
					Error.error_popup_resources(window)
					Board.redraw_board(window, robber_pos, roll, player)
					settlement.prepared_for_placement = False
					return

				# Draw settlement sprite and change state
				settlement.draw_settlement(window, player.color)
				settlement.prepared_for_placement = False
				settlement.is_placed = True
				settlement.color = player.color

				# Add settlement to player's settlements
				if settlement not in player.settlements:
					player.settlements.append(settlement)
					print(settlement.position)
					print('player got settlement')
					sprites.add(settlement)

				# Spend resources
				if GAME_START is False:
					SettlementEventHandler.__buy_settlement(player)
					Board.redraw_board(window, roll, player)

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