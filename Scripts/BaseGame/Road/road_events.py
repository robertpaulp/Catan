import pygame

import pygame.event

from constants import *
from BaseGame.Hexagon_Tiles.hexagon_tile import HexagonTile
from BaseGame.Settlements.settlement import Settlement, settlements, sprites
from BaseGame.Road.road import Road, roads
from BaseGame.Player.player import Player, players
from BaseGame.Board.board import Board
from BaseGame.Error.error import Error
import time


class RoadEventHandler:
	@staticmethod
	def press(window, event: pygame.event, road, player: Player):
		""" Handles road press events

		:param window: Display window
		:param event: Event to handle
		:param road: Road to place
		:param player: Current player
		:return: None
		"""
		mouse_pos = pygame.mouse.get_pos()

		if event.button == 1:
			# Start point is a settlement
			for settlement in player.settlements:
				if settlement.rect.collidepoint(mouse_pos):
					print("pressed")
					# Set road mouse-dragging state to True
					road.is_dragged = True
					road.borders.append(settlement)

					if road.start == (0, 0):  # If road has not been placed yet
						road.start = settlement.position
						
			# Start point is a road
			if len(road.borders) == 0:
				for existing_road in player.roads:
					if existing_road.is_placed is True and existing_road.borders[1].rect.collidepoint(mouse_pos):
						print("pressed")
						# Set road mouse-dragging state to True
						road.is_dragged = True
						road.borders.append(existing_road.borders[1])

						if road.start == (0, 0):
							road.start = existing_road.borders[1].position

	@staticmethod
	def place(window, event: pygame.event, road: Road, player: Player, GAME_START, robber_pos, roll):
		""" Handles road placement events

		:param window: Display window
		:param event: Event to handle
		:param road: Road to place
		:param player: Current player
		:return: None
		"""
		if Road.placement_is_possible(player, GAME_START) is False:
			road.is_dragged = False
			return -1

		if event.button == 1:
			for settlement in settlements:
				# If mouse was released on a valid settlement, draw the road
				# Check if road has valid start point (settlement exists)
				if settlement.rect.collidepoint(event.pos) and road.start != (0, 0):
					# Check if the end settlement is not the same as the start settlement
					if settlement.position == road.start:
						road.is_dragged = False
						return -1

					# Check if there is not already a road between the two settlements
					for existing_road in player.roads:
						if existing_road.start == road.start and existing_road.end == settlement.position:
							road.is_dragged = False
							return -1
						
					# Check if the two points of the road are adjacent  

					road.borders.append(settlement)  # Append end settlement to road borders

					road.is_placed = True
					road.is_dragged = False

					road.end = settlement.position

					print(road.start, road.end)
					road.draw_road(window, player.color)

					roads.append(road)

					if GAME_START is False:
						RoadEventHandler.__buy_road(player)
						Board.redraw_board(window, robber_pos, roll, player, GAME_START)
			
					return 0

			# If mouse was not released on a valid settlement, reset road state
			road.is_dragged = False
			return -1

	@staticmethod
	def drag(window, position, road: Road):
		""" Drag road to mouse position

		:param window: Display window
		:param event: Event to handle
		:param road: Road to place
		:return: None
		"""

		if road.is_dragged:
			road.end = position
		
	@staticmethod
	def __buy_road(player):
		""" Spend resources to buy settlement

		:param player:
		:return:
		"""
		print("buy")
		player.cards["Lumber"] -= 1
		player.cards["Bricks"] -= 1
		player.resource_cards -= 2