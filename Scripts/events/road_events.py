import pygame

from Scripts.board_elements.settlement import *
from Scripts.constants import *
from Scripts.player.player import Player
from Scripts.board_elements.road import Road, roads
from Scripts.board_elements.settlement import Settlement
import time


class RoadEventHandler:
	@staticmethod
	def place_road(window, event: pygame.event, settlements: list, road: Road, player: Player, action: str):
		""" Handles road placement events

		:param settlements:
		:param window: Display window
		:param event: Event to handle
		:param road: Road to place
		:param player: Current player
		:param action: Action to perform
		:return: None
		"""
		mouse_pos = pygame.mouse.get_pos()

		match action:
			case "press":
				if event.button == 1:
					for settlement in player.settlements:
						if settlement.rect.collidepoint(mouse_pos):
							print("pressed")
							# Set road mouse-dragging state to True
							road.is_dragged = True
							road.borders.append(settlement)

							# Set road start point
							mouse_x, mouse_y = event.pos

							if road.start == [0, 0]:  # If road has not been placed yet
								road.start = settlement.position

			case "release":
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
							for existing_road in roads:
								if existing_road.start == road.start and existing_road.end == settlement.position:
									road.is_dragged = False
									return -1

							print("placed")
							road.borders.append(settlement)  # Append end settlement to road borders

							road.is_placed = True
							road.is_dragged = False

							road.end = settlement.position

							print(road.start, road.end)
							road.draw_road(window)
							return 0

					# If mouse was not released on a valid settlement, reset road state
					road.is_dragged = False
					return -1

			case "dragging":
				if road.is_dragged:
					print("dragging")
					road.end[0] = event.pos[0]
					road.end[1] = event.pos[1]
