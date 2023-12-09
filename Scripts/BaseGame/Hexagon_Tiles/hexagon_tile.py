# Importing modules
import math
import pygame
import random
import sys
import numpy as np

sys.path.append("../../")

from constants import *

# --- Hexagon class ---
class HexagonTile:
    hexagons = []  # List of hexagons
    distinct_vertices = []  # List of distinct vertices

    center_points = []
    resourcesArray = []
    resources = [
            ["Wood", WOOD_SPRITE],
            ["Wheat", WHEAT_SPRITE],
            ["Sheep", SHEEP_SPRITE],
            ["Brick", BRICK_SPRITE],
            ["Ore", STONE_SPRITE]
        ]
    hexagon_numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, -1]
    hexagon_points = []
    desert_index = -1

    def __init__(self):
        self.center = None
        self.resource = None
        self.number = 0
        self.vertices = []
        self.edges = []

    def create_hexagon(window, x = HEXAGON_X_CENTER, y = HEXAGON_Y_CENTER, image = None, number = 0):
        hexagon = HexagonTile()
        hexagon.number = number
        HexagonTile.hexagons.append(hexagon)

        vertices = [

            # (x - HEXAGON_SIDE, y),
            # (x, y - (0.866 * HEXAGON_SIDE)),
            # (x + HEXAGON_SIDE, y),
            # (x + HEXAGON_SIDE, y + HEXAGON_SIDE),
            # (x, y + (0.866 * HEXAGON_SIDE) + HEXAGON_SIDE),
            # (x - HEXAGON_SIDE, y + HEXAGON_SIDE)

            (x - HEXAGON_SIDE, y),                                  # Top left
            (x + HEXAGON_SIDE * 0.1, y - HEXAGON_SIDE * 0.8),     # Top middle
            (x + HEXAGON_SIDE * 1.2, y),                            # Top right
            (x + HEXAGON_SIDE * 1.2, y + HEXAGON_SIDE * 1.2),     # Bottom right
            (x + HEXAGON_SIDE * 0.1, y + 2 * HEXAGON_SIDE),     # Bottom middle
            (x - HEXAGON_SIDE, y + HEXAGON_SIDE * 1.2)            # Bottom left
            
        ]

        hexagon.center = (x, y)
        hexagon.vertices = vertices

        for node in vertices:
            if node not in HexagonTile.distinct_vertices:
                HexagonTile.distinct_vertices.append(node)
        HexagonTile.hexagon_points.append(vertices)

        if image is not None:
            image = pygame.image.load(image)
            image = pygame.transform.scale(image, (HEXAGON_WIDTH * 1.1, HEXAGON_HEIGHT * 1.35))
            image = pygame.transform.rotate(image, 1)
            window.blit(image, (x - HEXAGON_SIDE, y - HEXAGON_SIDE / 2 - 15))

        else:
            pygame.draw.polygon(window, WHITE, vertices, 0)

        pygame.draw.polygon(window, BLACK, vertices, 4)

    def add_hexagon_number(window, x, y, number):
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(str(number), True, BLACK)
        text_rect = text.get_rect(center=(x + HEXAGON_SIDE * 0.1, y + HEXAGON_SIDE / 2 - 5))
        HexagonTile.center_points.append(text_rect.center)
        pygame.draw.circle(window, BEIGE, (x + HEXAGON_SIDE * 0.1, y + HEXAGON_SIDE / 2), HEXAGON_SIDE / 3, 0)
        pygame.draw.circle(window, BLACK, (x + HEXAGON_SIDE * 0.1, y + HEXAGON_SIDE / 2), HEXAGON_SIDE / 3, 1)
        window.blit(text, text_rect)

    def check_for_desert(number):
        if number == -1:
            return False
        else:
            return True
        
    def get_index(tile):
        return HexagonTile.resourcesArray.index(tile)
    
    def check_for_corner_case(index):
        # 0 : no problem
        # 1 : there is no tile on the left
        # 2 : there is no tile on the right
        left_problem = [0, 3, 7, 12, 16]
        right_problem = [2, 6, 11, 15, 18]
        for i in left_problem:
            if index == i:
                return 1
        for i in right_problem:
            if index == i:
                return 2
        return 0

    
    def append_center_points(desert_idx):
        check = HexagonTile.check_for_corner_case(desert_idx)
        align_x = 0

        if check == 1:
            right_tile_center = HexagonTile.center_points[desert_idx + 1]
            # Align
            align_x = right_tile_center[0] - (HEXAGON_WIDTH * 1.1) * 2
            HexagonTile.center_points.insert(desert_idx, (align_x, right_tile_center[1]))
        else:
            left_tile_center = HexagonTile.center_points[desert_idx - 1]
            # Align
            align_x = left_tile_center[0] + (HEXAGON_WIDTH * 1.1)
            HexagonTile.center_points.insert(desert_idx, (align_x, left_tile_center[1]))
    
    def get_resource():
        return HexagonTile.resources[np.random.randint(0, 5)]
    
    def shuffle_numbers(resource_array):
        if len(resource_array) != len(HexagonTile.hexagon_numbers):
            raise ValueError("len(resource_array) != len(HexagonTile.hexagon_numbers)")
        
        sublist = HexagonTile.hexagon_numbers[0:len(HexagonTile.hexagon_numbers) - 1]
        random.shuffle(sublist)
        HexagonTile.hexagon_numbers[0:len(HexagonTile.hexagon_numbers) - 1] = sublist

        for i in range(0, len(resource_array)):
            if resource_array[i] == "Desert":
                HexagonTile.hexagon_numbers[i], HexagonTile.hexagon_numbers[-1] = HexagonTile.hexagon_numbers[-1], HexagonTile.hexagon_numbers[i]
                HexagonTile.desert_index = i
                break 

    def create_resource_array(length):
        # Ensure that there one of each resource
        for i in range(0, 5):
            HexagonTile.resourcesArray.append(HexagonTile.resources[i][0])
        HexagonTile.resourcesArray.append("Desert")
        # Add the rest of the resources
        for i in range(0, length - 6):
            resource = HexagonTile.get_resource()
            HexagonTile.resourcesArray.append(resource[0]) 
        # Shuffle the array
        HexagonTile.resourcesArray.sort(key=lambda x: random.random())

    def create_row(window, x, y, hexagon_numbers, rows):
        for row in range(0,rows):
            number = hexagon_numbers.pop(0)
            if HexagonTile.check_for_desert(number):
                resource = HexagonTile.resourcesArray.pop(0)
                if resource == "Desert":
                    resource = HexagonTile.resourcesArray.pop(0)
                image = None
                for i in range(0, len(HexagonTile.resources)):
                    if resource == HexagonTile.resources[i][0]:
                        image = HexagonTile.resources[i][1]
                        break

                HexagonTile.create_hexagon(window, x, y, image, number)
                HexagonTile.add_hexagon_number(window, x, y, number)
            else:
                HexagonTile.create_hexagon(window, x, y, DESERT_SPRITE, number)
            x += HEXAGON_WIDTH * 1.1

    def draw_sea_hexagon(window, x, y):
        pts = []
        for i in range(6):
            x = x + 370 * math.cos(math.pi * 2 * i / 6)
            y = y + 370 * math.sin(math.pi * 2 * i / 6)
            pts.append([int(x), int(y)])

        pygame.draw.polygon(window, LIGHT_CYAN_BLUE, pts)
        pygame.draw.polygon(window, BLACK, pts, 4)

    def create_hexagon_grid(window, x, y, first_time = True):
        if first_time:
            HexagonTile.create_resource_array(len(HexagonTile.hexagon_numbers))
            HexagonTile.shuffle_numbers(HexagonTile.resourcesArray)
        resources_copy = HexagonTile.resourcesArray.copy()
        hexagon_numbers_copy = HexagonTile.hexagon_numbers.copy()

        # Create the first row
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 3)

        # Create the second row
        x = HEXAGON_X_AXIS - HEXAGON_WIDTH / 2 - HEXAGON_SIDE * 0.1
        y += HEXAGON_HEIGHT 
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 4)

        # Create the third row
        x = HEXAGON_X_AXIS - HEXAGON_WIDTH - HEXAGON_SIDE * 0.2
        y += HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 5)
        
        # Create the fourth row
        x = HEXAGON_X_AXIS - HEXAGON_WIDTH / 2 - HEXAGON_SIDE * 0.1
        y += HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 4)

        # Create the fifth row
        x = HEXAGON_X_AXIS
        y += HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 3)

        # TODO: Add adjacency to the nodes
        #for hexagon in HexagonTile.hexagons:

            

        HexagonTile.resourcesArray = resources_copy.copy()
        HexagonTile.hexagon_numbers = hexagon_numbers_copy.copy()
        HexagonTile.append_center_points(HexagonTile.get_index("Desert"))

        # Assign resources to hexagons
        for (resource, hexagon) in zip(HexagonTile.resourcesArray, HexagonTile.hexagons):
            hexagon.resource = resource
