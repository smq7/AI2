"""
This file is intended for constants
 in game as size of window,
 colors of ghost or player and etc.
"""
ROWS = 31
COLS = 28
PADDING = 50
# Screen constants
WIDTH, HEIGHT = COLS * 20 + PADDING, ROWS * 20 + PADDING
FPS = 60

MAZE_WIDTH, MAZE_HEIGHT = WIDTH - PADDING, HEIGHT - PADDING



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

# Enemy constants
RANDOM = 1
DEFAULT = 2

# Map constants
WALL = 1
COIN = 2
PLAYER = 223
ENEMY = 333
DEFAULT_GHOST = 222
RANDOM_GHOST = 221
BLOCKED = 1
PASSAGE = 0
WATER = 8
SWAMP = 9
ICE = 10
COINS_AMOUNT = 10


MINMAX = 1
EXPECT = 2
