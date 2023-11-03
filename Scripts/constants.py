from win32api import GetSystemMetrics

# Screen Constants
SCREEN_WIDTH = GetSystemMetrics(0) - 400
SCREEN_HEIGHT = GetSystemMetrics(1) - 200

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_CYAN_BLUE = (100, 181, 246)

# Dice Constants
DICE_WIDTH = 80
DICE_HEIGHT = 80
DICE_X_AXIS = SCREEN_WIDTH - DICE_WIDTH * 2 - 20
DICE_Y_AXIS = 20
DICE_CORNER_RADIUS = 10
DOT_RADIUS = 7
DOT_OFFSET_UP = DICE_WIDTH / 4
DOT_OFFSET_CENTER = DICE_WIDTH / 2
DOT_OFFSET_DOWN = DICE_WIDTH - DOT_OFFSET_UP