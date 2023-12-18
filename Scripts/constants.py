from win32api import GetSystemMetrics

# Screen Constants
SCREEN_WIDTH = 1476
SCREEN_HEIGHT = 784

# Color Constants
WHITE = (255, 255, 255)
TRANSPARENT_WHITE = (255, 255, 255, 70)
BLACK = (0, 0, 0)
LIGHT_CYAN_BLUE = (100, 181, 246)
BEIGE = (245, 245, 220)
TRANSPARENT = (0, 0, 0, 0)
SANDY = (228, 213, 183)
BRASS = (225, 193, 110)
BRASS2 = (211, 148, 68)
BRONZE = (205, 127, 50)
TRANSPARENT = (0, 0, 0, 0)
BROWN = (147, 81, 22)

# Resources colors
BRICK_COLOR = (188, 74, 60)
LUMBER_COLOR = (3, 75, 3)
ORE_COLOR = (144, 144, 144)
GRAIN_COLOR = (240, 215, 49)
WOOL_COLOR = (242, 240, 235)

# Hexagon Constants
HEXAGON_WIDTH = 115
HEXAGON_HEIGHT = 115
HEXAGON_X_CENTER = HEXAGON_WIDTH / 2
HEXAGON_Y_CENTER = HEXAGON_HEIGHT / 2
HEXAGON_SIDE = HEXAGON_WIDTH / 2
HEXAGON_CENTER = HEXAGON_HEIGHT / 2
HEXAGON_X_AXIS = SCREEN_WIDTH / 2 - HEXAGON_WIDTH / 2 - HEXAGON_WIDTH
HEXAGON_Y_AXIS = 75
POLYGON_RADIUS = 370

# Sprite Constants

POINTS_BANNER_SPRITE = "../Assets/Sprites/points_banner.png"
CARDS_TOTAL_SPRITE = "../Assets/Sprites/cards_total.png"

WOOD_SPRITE = "../Assets/Sprites/forest.png"
WHEAT_SPRITE = "../Assets/Sprites/field.png"
SHEEP_SPRITE = "../Assets/Sprites/pasture.png"
BRICK_SPRITE = "../Assets/Sprites/hill.png"
STONE_SPRITE = "../Assets/Sprites/mountain.png"
DESERT_SPRITE = "../Assets/Sprites/desert.png"
ROBBER_SPRITE = "../Assets/Sprites/robber.png"

SETTLEMENT_BUTTON_SPRITE = "../Assets/Sprites/settlement_button.png"
ROAD_BUTTON_SPRITE = "../Assets/Sprites/road_button.png"
SPECIAL_CARD_BUTTON_SPRITE = "../Assets/Sprites/special_card_button.png"
END_TURN_BUTTON_SPRITE = "../Assets/Sprites/end_turn_button.png"

PAPIRUS_SETTLEMENT_SPRITE = "../Assets/Sprites/papirus_settlement.png"
PAPIRUS_ROAD_SPRITE = "../Assets/Sprites/papirus_road.png"

PRESSED_ROAD_BUTTON_SPRITE = "../Assets/Sprites/pressed_road_button.png"
PRESSED_SETTLEMENT_BUTTON_SPRITE = "../Assets/Sprites/pressed_settlement_button.png"
PRESSED_END_TURN_BUTTON_SPRITE = "../Assets/Sprites/pressed_end_turn_button.png"

BANK_ICON_SPRITE = "../Assets/Sprites/bank_icon.png"
BANK_ARROWS_ICON_SPRITE = "../Assets/Sprites/bank_arrows_icon1.png"
SMALL_BUTTON_SPRITE = "../Assets/Sprites/small_button.png"
PRESSED_SMALL_BUTTON_SPRITE = "../Assets/Sprites/pressed_small_button.png"
EXIT_BUTTON_SPRITE = "../Assets/Sprites/exit_button.png"
PRESSED_EXIT_BUTTON_SPRITE = "../Assets/Sprites/pressed_exit_button.png"
WOOD_TABLE_SPRITE = "../Assets/Sprites/wood_table.png"
WOOD_TABLE_DARK_SPRITE = "../Assets/Sprites/wood_table_dark.png"

# Error sprites
ERROR_RESOURCE_SPRITE = "../Assets/Sprites/error_resource.png"
ERROR_PLACE_SPRITE = "../Assets/Sprites/error_place_first.png"
ERROR_ROBBER_SPRITE = "../Assets/Sprites/error_robber.png"
ERROR_PLACE_SETTLEMENTS_ROADS_SPRITE = "../Assets/Sprites/error_place_settlements_roads.png"
ERROR_PLACE_SETTLEMENTS_SPRITE = "../Assets/Sprites/error_place_settlements.png"
ERROR_PLACE_ROADS_SPRITE = "../Assets/Sprites/error_place_roads.png"
ERROR_ROLL_DICE_SPRITE = "../Assets/Sprites/error_roll_dice.png"
ERROR_ALREADY_ROLLED_SPRITE = "../Assets/Sprites/error_already_rolled.png"
# Pop up sprites
POPUP_STARTING_ROUND_SPRITE = "../Assets/Sprites/popup_starting_round.png"
POPUP_ROUND_NUMBER_SPRITE = "../Assets/Sprites/popup_round_number.png"
# Background
BACKGROUND_SPRITE = "../Assets/Sprites/background2.jpg"
TRADE_TABLE_SPRITE = "../Assets/Sprites/trade_table.png"
TRADE_BUTTON_BRICKS_SPRITE = "../Assets/Sprites/trade_button_bricks.png"
TRADE_BUTTON_LUMBER_SPRITE = "../Assets/Sprites/trade_button_lumber.png"
TRADE_BUTTON_ORE_SPRITE = "../Assets/Sprites/trade_button_ore.png"
TRADE_BUTTON_GRAIN_SPRITE = "../Assets/Sprites/trade_button_grain.png"
TRADE_BUTTON_WOOL_SPRITE = "../Assets/Sprites/trade_button_wool.png"
# Pressed trade buttons
TRADE_BUTTON_BRICKS_PRESSED_SPRITE = "../Assets/Sprites/trade_button_bricks_pressed.png"
TRADE_BUTTON_LUMBER_PRESSED_SPRITE = "../Assets/Sprites/trade_button_lumber_pressed.png"
TRADE_BUTTON_ORE_PRESSED_SPRITE = "../Assets/Sprites/trade_button_ore_pressed.png"
TRADE_BUTTON_GRAIN_PRESSED_SPRITE = "../Assets/Sprites/trade_button_grain_pressed.png"
TRADE_BUTTON_WOOL_PRESSED_SPRITE = "../Assets/Sprites/trade_button_wool_pressed.png"

#PRESSED_TRADE_BUTTON_SPRITE = "../Assets/Sprites/pressed_trade_button.png"
BRICKS_SPRITE = "../Assets/Sprites/bricks.png"
LUMBER_SPRITE = "../Assets/Sprites/lumber.png"
GRAIN_SPRITE = "../Assets/Sprites/grain.png"
ORE_SPRITE = "../Assets/Sprites/ore.png"
WOOL_SPRITE = "../Assets/Sprites/wool.png"

PRESSED_BRICKS_SPRITE = "../Assets/Sprites/pressed_bricks.png"
PRESSED_LUMBER_SPRITE = "../Assets/Sprites/pressed_lumber.png"
PRESSED_GRAIN_SPRITE = "../Assets/Sprites/pressed_grain.png"
PRESSED_ORE_SPRITE = "../Assets/Sprites/pressed_ore.png"
PRESSED_WOOL_SPRITE = "../Assets/Sprites/pressed_wool.png"

TRADE_POSITION_X = 490
TRADE_POSITION_Y = 200
TRADE_POSITION_X_RIGHT = 520
TRADE_POSITION_Y_DOWN = 330

# Player Constants
PLAYER_BOARD_X_AXIS = HEXAGON_X_AXIS + HEXAGON_WIDTH * 4.2
PLAYER_BOARD_Y_AXIS = HEXAGON_Y_AXIS - HEXAGON_HEIGHT / 2
PLAYER_BOARD_WIDTH = HEXAGON_WIDTH * 2.7
PLAYER_BOARD_HEIGHT = HEXAGON_HEIGHT * 4
ICON_SIZE = 30

NAME_POSITION = []
for i in range(4):
    NAME_POSITION.append((PLAYER_BOARD_X_AXIS + 80 + ICON_SIZE * 1.5, PLAYER_BOARD_Y_AXIS + 20 + 130 * i))
ICON_POSITION = (PLAYER_BOARD_X_AXIS + 80, PLAYER_BOARD_Y_AXIS + 20)
RESOURCE_CARDS_POSITION = (PLAYER_BOARD_X_AXIS + 90, PLAYER_BOARD_Y_AXIS + 90)
SPECIAL_CARDS_POSITION = (PLAYER_BOARD_X_AXIS + 90, PLAYER_BOARD_Y_AXIS + 100)

"""
WOOD_POSITION = (PLAYER_BOARD_X_AXIS + 90, PLAYER_BOARD_Y_AXIS + 60)
WHEAT_POSITION = (PLAYER_BOARD_X_AXIS + 90, PLAYER_BOARD_Y_AXIS + 100)
SHEEP_POSITION = (PLAYER_BOARD_X_AXIS + 90, PLAYER_BOARD_Y_AXIS + 140)
BRICK_POSITION = (PLAYER_BOARD_X_AXIS + 90, PLAYER_BOARD_Y_AXIS + 180)
ORE_POSITION = (PLAYER_BOARD_X_AXIS + 90, PLAYER_BOARD_Y_AXIS + 220)
"""

# Settlement
SETTLEMENT_SPRITE = 17

# Dice Constants
DICE_WIDTH = 80
DICE_HEIGHT = 80
DICE_X_AXIS = SCREEN_WIDTH - DICE_WIDTH * 2 - 30
DICE_Y_AXIS = SCREEN_HEIGHT - DICE_HEIGHT - 50 - 10
DICE_CORNER_RADIUS = 10
DOT_RADIUS = 7
DOT_OFFSET_UP = DICE_WIDTH / 4
DOT_OFFSET_CENTER = DICE_WIDTH / 2
DOT_OFFSET_DOWN = DICE_WIDTH - DOT_OFFSET_UP
DICE_BTN_WIDTH = 200
DICE_BTN_HEIGHT = 50
DICE_BTN_X_AXIS = SCREEN_WIDTH - DICE_BTN_WIDTH - 5
DICE_BTN_Y_AXIS = SCREEN_HEIGHT - 50 - 5

# Cards constants
CARDS_PROMPT_WIDTH = 450
CARDS_PROMPT_HEIGHT = 125
CARDS_PROMPT_X_AXIS = 20
CARDS_PROMPT_Y_AXIS = SCREEN_HEIGHT - CARDS_PROMPT_HEIGHT - 20 
CARD_WIDTH = 40
CARD_HEIGHT = 45
CARDS_POSITION_X = CARDS_PROMPT_X_AXIS + 40
CARDS_POSITION_Y = CARDS_PROMPT_Y_AXIS + 35
CARDS_SPACING_HELPER = 80

# Trade
TRADE_PROMPT_WIDTH = 300
TRADE_PROMPT_HEIGHT = 470
TRADE_PROMPT_X_AXIS = 20
TRADE_PROMPT_Y_AXIS = 150

TRADE_BUTTON_WIDTH = 220
TRADE_BUTTON_HEIGHT = 60
TRADE_BUTTON_X_AXIS = 50
TRADE_BUTTON_Y_AXIS = 260

# Menu Constants
FONT_PATH = "../Assets/Fonts/Grand9K Pixel.ttf"
BACKGROUND_PATH = "../Assets/Catan_1920x1080.jpg"
MUSIC_PATH = "../Assets/Music/Cunja Mija by Vox Vulgaris Crop.mp3"
TITLE_TEXT = "Catan"
TITLE_X_AXIS = SCREEN_WIDTH / 2
TITLE_Y_AXIS = 100
SHORT_DESCRIPTION_TEXT = "A game of wonders..."

## Play Button
PLAY_TEXT = "Play"
PLAY_BTN_WIDTH = 200
PLAY_BTN_HEIGHT = 100
PLAY_BTN_X_AXIS = SCREEN_WIDTH - PLAY_BTN_WIDTH - 50
PLAY_BTN_Y_AXIS = SCREEN_HEIGHT - PLAY_BTN_HEIGHT - 300
PLAY_SIZE = 50

## Options Button
OPTIONS_TEXT = "Options"
OPTIONS_BTN_WIDTH = 250
OPTIONS_BTN_HEIGHT = 100
OPTIONS_BTN_X_AXIS = SCREEN_WIDTH - OPTIONS_BTN_WIDTH - 50
OPTIONS_BTN_Y_AXIS = SCREEN_HEIGHT - OPTIONS_BTN_HEIGHT - 150
OPTIONS_SIZE = 50

## Quit Button
QUIT_TEXT = "Quit"
QUIT_BTN_WIDTH = 200
QUIT_BTN_HEIGHT = 100
QUIT_BTN_X_AXIS = SCREEN_WIDTH - QUIT_BTN_WIDTH - 50
QUIT_BTN_Y_AXIS = SCREEN_HEIGHT - QUIT_BTN_HEIGHT
QUIT_SIZE = 50

## Back Button
BACK_TEXT = "Back"
BACK_BTN_WIDTH = 200
BACK_BTN_HEIGHT = 100
BACK_BTN_X_AXIS = 50
BACK_BTN_Y_AXIS = SCREEN_HEIGHT - BACK_BTN_HEIGHT
BACK_SIZE = 50

GAME_START = True
END_START_ROUND = False