import pygame
import pyg
from langton.automata import State


class MySquare:
    def __init__(self):
        self.position_tab = MySquare.get_first_position_tab()
        self.rect = pygame.Rect(MySquare.get_first_position_pixel()[0], MySquare.get_first_position_pixel()[1], pyg.NUMBER_OF_PIXELS, pyg.NUMBER_OF_PIXELS)
        self.movement_vector = pyg.MOVE_UP

    def draw_square(self, surface: pygame.SurfaceType, state: State):
        pygame.draw.rect(surface, state.color, self.rect)
        self.__draw_border(surface)

    def __draw_border(self, surface: pygame.SurfaceType):
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)

    def set_pos(self, new_left: int, new_top: int):
        self.rect.left = new_left
        self.rect.top = new_top

    def rotate_movement_vector(self, command: str):
        self.movement_vector = pyg.MOVES_ROTATIONS[command][self.movement_vector]

    def move_square(self):
        if not self.__is_move_possible():
            return
        self.__modify_position_tab()
        self.rect.left = self.rect.left + (self.movement_vector[0] * pyg.NUMBER_OF_PIXELS)
        self.rect.top = self.rect.top + (self.movement_vector[1] * pyg.NUMBER_OF_PIXELS)

    def __modify_position_tab(self):
        self.position_tab = (self.position_tab[0] + self.movement_vector[0], self.position_tab[1] + self.movement_vector[1])

    def get_position_tab(self) -> (int, int):
        return self.position_tab

    def __is_move_possible(self):
        left = self.rect.left + (self.movement_vector[0] * pyg.NUMBER_OF_PIXELS)
        top = self.rect.top + (self.movement_vector[1] * pyg.NUMBER_OF_PIXELS)
        if left < 0:
            return False
        elif left >= pyg.RESOLUTION[0]:
            return False
        elif top < 0:
            return False
        elif top >= pyg.RESOLUTION[1]:
            return False
        return True

    @staticmethod
    def get_first_position_tab() -> (int, int):
        return pyg.RESOLUTION[0] // pyg.NUMBER_OF_PIXELS // 2, pyg.RESOLUTION[1] // pyg.NUMBER_OF_PIXELS // 2

    @staticmethod
    def get_first_position_pixel() -> (int, int):
        return pyg.RESOLUTION[0] // 2, pyg.RESOLUTION[1] // 2
