import pygame
from Scripts.constants import *

settlement_img = pygame.Surface((SETTLEMENT_SPRITE * 3, SETTLEMENT_SPRITE * 3), pygame.SRCALPHA)
lowered_opacity_color = (200, 100, 23, 50)

settlements = []
sprites = pygame.sprite.Group()


class Settlement(pygame.sprite.Sprite):
	# settlements = []

	def __init__(self, window, position):
		""" Instantiates settlement object

		"""

		super().__init__()  # TODO group settlements into sprites

		# Structural attributes
		self.image = pygame.Surface((SETTLEMENT_SPRITE * 3, SETTLEMENT_SPRITE * 3), pygame.SRCALPHA)
		self.rect = self.image.get_rect(center=position)
		self.position = position

		# State attributes
		self.prepared_for_placement = False
		self.is_placed = False
		self.is_hovered = False
		self.color = (0, 0, 0, 0)

		# Gameplay attributes
		self.resources = []
		self.dice_rolls = []

	def draw_settlement(self, window, color):
		""" Draws settlement icon on the map

		:param color:
		:param window:
		:return:
		"""

		pygame.draw.circle(self.image, color, (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), SETTLEMENT_SPRITE, 0)

		window.blit(self.image, (self.position[0] - SETTLEMENT_SPRITE, self.position[1] - SETTLEMENT_SPRITE))
		pygame.display.update()

	def hover_state(self, window):  # TODO
		""" Draw lowered-opacity version of settlement during mouse hover

		:param window:
		:return:
		"""

		pygame.draw.circle(self.image, (255, 0, 0, 100), (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), SETTLEMENT_SPRITE, 5)
		self.is_hovered = True

		window.blit(self.image, (self.position[0] - SETTLEMENT_SPRITE, self.position[1] - SETTLEMENT_SPRITE))
		pygame.display.update()

	@staticmethod
	def placement_is_possible(player, GAME_START):
		if GAME_START is True:
			return True
		if player.cards["Wood"] >= 1 and player.cards["Brick"] >= 1 and player.cards["Sheep"] >= 1 and player.cards["Wheat"] >= 1:
			return True
		return False

	@staticmethod
	def prepare_board_surfaces(window, nodes: tuple, hexagons: list):
		""" Places possible settlement position surfaces on the map

		:param hexagons: Hexagon tiles
		:param window: Window surface display
		:param nodes: Hexagon nodes
		:return: Dictionary containing (surface, position) elements
		"""

		for node in nodes:
			settlement = Settlement(window, node)

			# Get adjacent resources and dice roll values
			for hexagon in hexagons:
				if node in hexagon.vertices:
					settlement.resources.append(hexagon.resource)
					settlement.dice_rolls.append(hexagon.number)

			settlements.append(settlement)

			settlement.image.set_alpha(255)
			hover_area = pygame.draw.circle(settlement.image, (0, 0, 0, 0),
			                                (SETTLEMENT_SPRITE, SETTLEMENT_SPRITE), SETTLEMENT_SPRITE, 0)
			position = tuple(map(lambda x: x - SETTLEMENT_SPRITE, list(node)))

			window.blit(settlement.image, position)
			pygame.display.update()
