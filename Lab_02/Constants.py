"""
This file is intended for constants
 in game as size of window,
 colors of ghost or player and etc.
"""

# Screen constants
WIDTH, HEIGHT = 670, 670
FPS = 60
PADDING = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - PADDING, HEIGHT - PADDING

ROWS = 31
COLS = 31

# Colour constants
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (187, 187, 187)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ICE_COLOR = (0, 204, 255)
SWAMP_COLOR = (102, 51, 0)
WATER_COLOR = (0, 102, 128)
EARTH = (51, 26, 0)
# Font constants
START_TEXT_SIZE = 36
START_FONT = 'Sans Serif'

# Game states
MENU = 1
GAMING = 2
GAME_OVER = 3
WINNER = 4

# Player constants
PLAYER_COLOUR = (255, 0, 0)
PLAYER_LIVES = 2
DESTINATION = (29, 29)

#Map constants
WALL = 1
COIN = 2
PLAYER = 3
ENEMY = 4
BLOCKED = 1
PASSAGE = 0
WATER = 8
SWAMP = 9
ICE = 10
