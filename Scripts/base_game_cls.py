# Importing modules
import pandas as pd
import math
import numpy as np
import pygame
import random
import game
import constants as c

# --- Hexagon class ---
class HexagonTile:
    hexagons = []  # List of hexagons
    distinct_vertices = []  # List of distinct vertices

    center_points = []
    resourcesArray = []
    resources = [
            ["Wood", c.WOOD_SPRITE],
            ["Wheat", c.WHEAT_SPRITE],
            ["Sheep", c.SHEEP_SPRITE],
            ["Brick", c.BRICK_SPRITE],
            ["Ore", c.STONE_SPRITE]
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

    def create_hexagon(window, x = c.HEXAGON_X_CENTER, y = c.HEXAGON_Y_CENTER, image = None):
        hexagon = HexagonTile()
        HexagonTile.hexagons.append(hexagon)

        vertices = [

            # (x - c.HEXAGON_SIDE, y),
            # (x, y - (0.866 * c.HEXAGON_SIDE)),
            # (x + c.HEXAGON_SIDE, y),
            # (x + c.HEXAGON_SIDE, y + c.HEXAGON_SIDE),
            # (x, y + (0.866 * c.HEXAGON_SIDE) + c.HEXAGON_SIDE),
            # (x - c.HEXAGON_SIDE, y + c.HEXAGON_SIDE)

            (x - c.HEXAGON_SIDE, y),                                  # Top left
            (x + c.HEXAGON_SIDE * 0.1, y - c.HEXAGON_SIDE * 0.8),     # Top middle
            (x + c.HEXAGON_SIDE * 1.2, y),                            # Top right
            (x + c.HEXAGON_SIDE * 1.2, y + c.HEXAGON_SIDE * 1.2),     # Bottom right
            (x + c.HEXAGON_SIDE * 0.1, y + 2 * c.HEXAGON_SIDE),     # Bottom middle
            (x - c.HEXAGON_SIDE, y + c.HEXAGON_SIDE * 1.2)            # Bottom left
            
        ]

        hexagon.center = (x, y)
        hexagon.vertices = vertices

        for node in vertices:
            if node not in HexagonTile.distinct_vertices:
                HexagonTile.distinct_vertices.append(node)

        HexagonTile.hexagon_points.append(vertices)
        if image is not None:
            image = pygame.image.load(image)
            image = pygame.transform.scale(image, (c.HEXAGON_WIDTH * 1.1, c.HEXAGON_HEIGHT * 1.35))
            image = pygame.transform.rotate(image, 1)
            window.blit(image, (x - c.HEXAGON_SIDE, y - c.HEXAGON_SIDE / 2 - 15))

        else:
            pygame.draw.polygon(window, c.WHITE, vertices, 0)

        pygame.draw.polygon(window, c.BLACK, vertices, 4)

    def add_hexagon_number(window, x, y, number):
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(str(number), True, c.BLACK)
        text_rect = text.get_rect(center=(x + c.HEXAGON_SIDE * 0.1, y + c.HEXAGON_SIDE / 2 - 5))
        HexagonTile.center_points.append(text_rect.center)
        pygame.draw.circle(window, c.BEIGE, (x + c.HEXAGON_SIDE * 0.1, y + c.HEXAGON_SIDE / 2), c.HEXAGON_SIDE / 3, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.HEXAGON_SIDE * 0.1, y + c.HEXAGON_SIDE / 2), c.HEXAGON_SIDE / 3, 1)
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
            align_x = right_tile_center[0] - (c.HEXAGON_WIDTH * 1.1) * 2
            HexagonTile.center_points.insert(desert_idx, (align_x, right_tile_center[1]))
        else:
            left_tile_center = HexagonTile.center_points[desert_idx - 1]
            # Align
            align_x = left_tile_center[0] + (c.HEXAGON_WIDTH * 1.1)
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

                HexagonTile.create_hexagon(window, x, y, image)
                HexagonTile.add_hexagon_number(window, x, y, number)
            else:
                HexagonTile.create_hexagon(window, x, y, c.DESERT_SPRITE)
            x += c.HEXAGON_WIDTH * 1.1

    def create_hexagon_grid(window, x, y, first_time = True):
        if first_time:
            HexagonTile.create_resource_array(len(HexagonTile.hexagon_numbers))
            HexagonTile.shuffle_numbers(HexagonTile.resourcesArray)
        resources_copy = HexagonTile.resourcesArray.copy()
        hexagon_numbers_copy = HexagonTile.hexagon_numbers.copy()

        # Create the first row
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 3)

        # Create the second row
        x = c.HEXAGON_X_AXIS - c.HEXAGON_WIDTH / 2 - c.HEXAGON_SIDE * 0.1
        y += c.HEXAGON_HEIGHT 
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 4)

        # Create the third row
        x = c.HEXAGON_X_AXIS - c.HEXAGON_WIDTH - c.HEXAGON_SIDE * 0.2
        y += c.HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 5)
        
        # Create the fourth row
        x = c.HEXAGON_X_AXIS - c.HEXAGON_WIDTH / 2 - c.HEXAGON_SIDE * 0.1
        y += c.HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 4)

        # Create the fifth row
        x = c.HEXAGON_X_AXIS
        y += c.HEXAGON_HEIGHT
        HexagonTile.create_row(window, x, y, HexagonTile.hexagon_numbers, 3)

        HexagonTile.resourcesArray = resources_copy.copy()
        HexagonTile.hexagon_numbers = hexagon_numbers_copy.copy()
        HexagonTile.append_center_points(HexagonTile.get_index("Desert"))

        # Assign resources to hexagons
        for (resource, hexagon) in zip(HexagonTile.resourcesArray, HexagonTile.hexagons):
            hexagon.resource = resource

# --- Settlement class ---
class Settlement:
    # TODO: Create a class called Settlement
    pass

# --- Road class ---
class Road:
    # TODO: Create a class called Road 
    pass

# --- Robber class ---
class Robber:
    # TODO: Create a class called Robber
    # Create the robber
    # Create the robber movement
    # Create the robber stealing
    # ADD card elimination if > 7 cards
    current_pos = (0,0)

    def delete_cards():
        pass

    # You can't move the robber in the same tile
    def check_move(mouse_pos):
        if mouse_pos[0] >= Robber.current_pos[0] - c.HEXAGON_SIDE/3 and mouse_pos[0] <= Robber.current_pos[0] + c.HEXAGON_SIDE/3 :
            if mouse_pos[1] >= Robber.current_pos[1] - c.HEXAGON_SIDE/3 and mouse_pos[1] <= Robber.current_pos[1] + c.HEXAGON_SIDE/3 :
                return False
        return True

        # if mouse_pos == robber_pos:
        #     return False
        # return True

    def create_robber(window):
        index = HexagonTile.get_index("Desert")
        Robber.current_pos = HexagonTile.center_points[index]
        pygame.draw.circle(window, c.BLACK, HexagonTile.center_points[index], c.HEXAGON_SIDE / 3, 0)

    def move_robber(window, x, y):
        Robber.current_pos = (x, y)
        pygame.draw.circle(window, c.BLACK, (x, y + 5), c.HEXAGON_SIDE / 3, 0)

# --- Dice class ---
class Dice:

    def dice_one(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)

    def dice_two(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    def dice_three(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)

    def dice_four(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    def dice_five(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_CENTER, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)

    def dice_six(window, x, y):
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_UP, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_UP), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_CENTER), c.DOT_RADIUS, 0)
        pygame.draw.circle(window, c.BLACK, (x + c.DOT_OFFSET_DOWN, y + c.DOT_OFFSET_DOWN), c.DOT_RADIUS, 0)

    def create_dice(window, x, y):
        pygame.draw.rect(window, c.WHITE,(x, y, c.DICE_WIDTH, c.DICE_HEIGHT), 0, -1, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS, c.DICE_CORNER_RADIUS)

    def dice_roll():
        dice = np.random.randint(1, 7)
        return dice
    
    def dice_display_face(face, window, x=c.DICE_X_AXIS, y=c.DICE_Y_AXIS):
        if face == 1:
            Dice.dice_one(window, x, y)
        elif face == 2:
            Dice.dice_two(window, x, y)
        elif face == 3:
            Dice.dice_three(window, x, y)
        elif face == 4:
            Dice.dice_four(window, x, y)
        elif face == 5:
            Dice.dice_five(window, x, y)
        elif face == 6:
            Dice.dice_six(window, x, y)
        else:
            print("Error")

    def dices(window, roll, x= c.DICE_X_AXIS, y= c.DICE_Y_AXIS):
        if roll[0] != 0:
            Dice.create_dice(window, x, y)
            Dice.dice_display_face(roll[0], window, x, y)

        if roll[1] != 0:
            Dice.create_dice(window, x + 90, y)
            Dice.dice_display_face(roll[1], window, x + 90, y)


# --- Card class ---
class Card:
    # TODO: Create a class called Card
    # Create the cards

    pass

# --- Player class ---
class Player:
    # TODO: Create a class called Player
    pass

# --- Board class ---
class Board:
    # TODO: Create a class called Board
    # Incorporate all the classes and create the board

    def roll_dice_btn(window, x=c.DICE_BTN_X_AXIS, y=c.DICE_BTN_Y_AXIS):
        button = pygame.draw.rect(window, c.BEIGE, (x, y, c.DICE_BTN_WIDTH, c.DICE_BTN_HEIGHT))
        pygame.draw.rect(window, c.BLACK, (x, y, c.DICE_BTN_WIDTH, c.DICE_BTN_HEIGHT), 4)
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(str("Roll Dice!"), True, c.BLACK)
        text_rect = text.get_rect(center=(x + 100, y + 25))
        window.blit(text, text_rect)
        return button