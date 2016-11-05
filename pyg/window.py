import pygame
import pyg


class PyWindow:
    def __init__(self, resolution: (int, int), background_color: (int, int, int)):
        self.resolution = resolution
        self.background_color = background_color
        self.surface = pygame.display.set_mode(self.resolution)
        self.surface.fill(self.background_color)

    def draw_lines(self):
        self.__draw_vertical_lines()
        self.__draw_horizontal_lines()

    def __draw_vertical_lines(self):
        start_pos_x = 0
        start_pos_y = 0
        end_pos_x = 0
        end_pos_y = self.resolution[1]

        pos_iter = 0
        while pos_iter < self.resolution[0]:
            self.__draw_line(self.surface, (start_pos_x + pos_iter, start_pos_y), (end_pos_x + pos_iter, end_pos_y))
            pos_iter += pyg.NUMBER_OF_PIXELS

    def __draw_horizontal_lines(self):
        start_pos_x = 0
        start_pos_y = 0
        end_pos_x = self.resolution[0]
        end_pos_y = 0

        pos_iter = 0
        while pos_iter < self.resolution[0]:
            self.__draw_line(self.surface, (start_pos_x, start_pos_y + pos_iter), (end_pos_x, end_pos_y + pos_iter))
            pos_iter += pyg.NUMBER_OF_PIXELS

    @staticmethod
    def __draw_line(surface: pygame.SurfaceType, point_1: (int, int), point_2: (int, int), color: (int, int, int)=(0, 0, 0)):
            pygame.draw.line(surface, color, point_1, point_2)
