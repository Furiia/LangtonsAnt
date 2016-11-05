NUMBER_OF_PIXELS = 10
FPS_LIMIT = 251
#width, height
RESOLUTION = (1400, 1000)
BASE_COLOR = (255, 255, 255)
COLORS = [(255, 255, 255),
          (128, 128, 128),
          (255, 0, 127),
          (127, 0, 255),
          (0, 0, 255),
          (0, 255, 255),
          (0, 255, 0),
          (255, 255, 0),
          (255, 128, 0),
          (255, 0, 0),
          (0, 0, 0)]
MOVE_LEFT = (-1, 0)
MOVE_DOWN = (0, 1)
MOVE_RIGHT = (1, 0)
MOVE_UP = (0, -1)
MOVES_LIST = [MOVE_UP, MOVE_RIGHT, MOVE_DOWN, MOVE_LEFT]
MOVES_ROTATIONS = {
                    'L': {
                        MOVE_UP     : MOVE_LEFT,
                        MOVE_LEFT   : MOVE_DOWN,
                        MOVE_DOWN   : MOVE_RIGHT,
                        MOVE_RIGHT  : MOVE_UP},
                    'R': {
                        MOVE_UP     : MOVE_RIGHT,
                        MOVE_RIGHT  : MOVE_DOWN,
                        MOVE_DOWN   : MOVE_LEFT,
                        MOVE_LEFT   : MOVE_UP}}
