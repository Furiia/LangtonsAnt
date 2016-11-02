import pygame
from pyg.object import MyRect


class Window:
    def __init__(self, resolution: (int, int), background_color: (int, int, int)):
        self.resolution = resolution
        self.screen = pygame.display.set_mode(self.resolution)
        self.background_color = background_color
        self.screen.fill(self.background_color)
        self.clock = pygame.time.Clock()
        self.start_left = 0
        self.start_top = 0
        self.line_points = []
        self.generate_lines()

    def main_loop(self):
        running = True
        while running:
            self.clock.tick(150)
            self.draw_scene()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def draw_rect(self, rect: MyRect):
        pygame.draw.rect(self.screen, (255, 0, 0), rect.rect)

    def draw_scene(self):
        self.screen.fill(self.background_color)
        self.draw_rect(MyRect(self.start_left, self.start_top, 10, 10))
        self.iterate_positions()
        self.draw_lines()

    def generate_lines(self):
        self.generate_vertical_lines()
        self.generate_horizontal_lines()

    def generate_vertical_lines(self):
        start_pos_x = 0
        start_pos_y = 0
        end_pos_x = 0
        end_pos_y = self.resolution[1]

        pos_iter = 0
        while pos_iter < self.resolution[0]:
            self.line_points.append(((start_pos_x + pos_iter, start_pos_y), (end_pos_x + pos_iter, end_pos_y)))
            pos_iter += 10

    def generate_horizontal_lines(self):
        start_pos_x = 0
        start_pos_y = 0
        end_pos_x = self.resolution[0]
        end_pos_y = 0

        pos_iter = 0
        while pos_iter < self.resolution[0]:
            self.line_points.append(((start_pos_x, start_pos_y + pos_iter), (end_pos_x, end_pos_y + pos_iter)))
            pos_iter += 10

    def draw_lines(self):
        for line in self.line_points:
            pygame.draw.line(self.screen, (0, 0, 0), line[0], line[1])

    def iterate_positions(self):
        if self.start_left + 10 > self.resolution[0]:
            if self.start_top + 10 > self.resolution[1]:
                self.start_left = 0
                self.start_top = 0
            else:
                self.start_left = 0
                self.start_top += 10
        else:
            self.start_left += 10


if __name__ == '__main__':
    window = Window((1400, 1000), (255, 255, 255))
    window.draw_rect(MyRect(0, 0, 10, 10))
    window.main_loop()
