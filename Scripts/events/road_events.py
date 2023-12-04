import pygame

from Scripts.board_elements.settlement import *
from Scripts.constants import *
from Scripts.player.player import Player
from Scripts.board_elements.road import Road
import time


class RoadEventHandler:
	@staticmethod
	def place_road(window, event: pygame.event, player: Player, action: str):
		""" Handles road placement events

		:param window: Display window
		:param event: Event to handle
		:param player: Current player
		:param action: Action to perform
		:return: None
		"""
		mouse_pos = pygame.mouse.get_pos()
		road = Road()

		match action:
			case "press":
				if event.button == 1:
					for settlement in player.settlements:
						if settlement.rect.collidepoint(mouse_pos):
							# Set road mouse-dragging state to True
							road.is_dragged = True
							road.borders.append(settlement)

							# Set road start point
							mouse_x, mouse_y = event.pos

							if road.start == [0, 0]:  # If road has not been placed yet
								road.start[0] = mouse_x
								road.start[1] = mouse_y
							else: # If road is being dragged
								offset_x = road.start[0] - mouse_x
								offset_y = road.start[1] - mouse_y

			case "release":
				if event.button == 1:
					road.is_dragged = False

					road.end[0] = event.pos[0]
					road.end[1] = event.pos[1]
			case "dragging":
				if road.is_dragged:
					road.end[0] = event.pos[0]
					road.end[1] = event.pos[1]
