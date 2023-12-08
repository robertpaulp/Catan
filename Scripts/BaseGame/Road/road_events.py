import pygame

from Settlements import Settlement, settlements
from constants import *
from Player import Player
from Road import Road, roads
from Settlements import Settlement
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

					if road.start == [0, 0]:  # If road has not been placed yet
						road.start = settlement.position
						
			# Start point is a road
			if len(road.borders) == 0:
				for existing_road in player.roads:
					if existing_road.is_placed is True and existing_road.borders[1].rect.collidepoint(mouse_pos):
						print("pressed")
						# Set road mouse-dragging state to True
						road.is_dragged = True
						road.borders.append(existing_road.borders[1])

						if road.start == [0, 0]:
							road.start = existing_road.borders[1].position

	@staticmethod
	def place(window, event: pygame.event, road: Road, player: Player):
		""" Handles road placement events

		:param window: Display window
		:param event: Event to handle
		:param road: Road to place
		:param player: Current player
		:return: None
		"""

		if event.button == 1:
			for settlement in settlements:
				# If mouse was released on a valid settlement, draw the road
				# Check if road has valid start point (settlement exists)
				if settlement.rect.collidepoint(event.pos) and road.start != [0, 0]:
					# Check if the end settlement is not the same as the start settlement
					if settlement.position == road.start:
						road.is_dragged = False
						return -1

					# Check if there is not already a road between the two settlements
					for existing_road in player.roads:
						if existing_road.start == road.start and existing_road.end == settlement.position:
							road.is_dragged = False
							return -1

					print("placed")
					road.borders.append(settlement)  # Append end settlement to road borders

					road.is_placed = True
					road.is_dragged = False

					road.end = settlement.position

					print(road.start, road.end)
					road.draw_road(window, player.color)
					return 0

			# If mouse was not released on a valid settlement, reset road state
			road.is_dragged = False
			return -1

	@staticmethod
	def drag(window, event: pygame.event, road: Road):
		""" Drag road to mouse position

		:param window: Display window
		:param event: Event to handle
		:param road: Road to place
		:return: None
		"""

		if road.is_dragged:
			print("dragging")
			road.end[0] = event.pos[0]
			road.end[1] = event.pos[1]