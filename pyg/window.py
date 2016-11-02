import pygame
from pyg import NUMBER_OF_PIXELS
from langton.parser import transform
from pyg.object import MyRect
from langton.langton import LangtonAntsStructure
from langton.parser import turn_left, turn_right, Step


class Window:
    def __init__(self, resolution: (int, int), background_color: (int, int, int), command: str):
        self.resolution = resolution
        self.screen = pygame.display.set_mode(self.resolution)
        self.background_color = background_color
        self.screen.fill(self.background_color)
        self.clock = pygame.time.Clock()
        self.start_left = 0
        self.start_top = 0
        self.line_points = []
        self.generate_lines()
        self.langton = LangtonAntsStructure(resolution)

        self.step_list = transform(command)
        self.move = (-1, 0)
        self.moveable = True
        self.actual = self.langton.get_first_pos()
        self.clock_tick = 250

    def main_loop(self):
        loop_counter = 0
        event_map = dict()
        event_map['running'] = True
        event_map['space_pressed'] = False
        while event_map['running']:
            self.event_loop(event_map)
            if loop_counter % 1000 == 0:
                print(loop_counter)
            elif loop_counter % 100 == 0:
                print("fps: %s" %(self.clock.get_fps()))
            if event_map['space_pressed']:
                continue
            self.clock.tick(self.clock_tick)
            #self.draw_scene()
            self.actual = proceed(self, self.actual)
            self.draw_lines()
            pygame.display.flip()
            loop_counter += 1

    def event_loop(self, event_map):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_map['running'] = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    event_map['space_pressed'] = not event_map['space_pressed']
                elif event.key == pygame.K_KP_MINUS:
                    self.clock_tick -= 1
                    print(self.clock_tick)
                elif event.key == pygame.K_KP_PLUS:
                    self.clock_tick += 1
                    print(self.clock_tick)

    def draw_scene(self):
        self.screen.fill(self.background_color)
        self.draw_rects()
        self.draw_lines()

    def draw_rects(self):
        for i in range(0, self.resolution[0]//NUMBER_OF_PIXELS):
            for j in range(0, self.resolution[1]//NUMBER_OF_PIXELS):
                self.draw_rect(self.langton.square_map[(i, j)])

    def draw_rect(self, rect: MyRect):
        pygame.draw.rect(self.screen, rect.color, rect.rect)

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
            pos_iter += NUMBER_OF_PIXELS

    def generate_horizontal_lines(self):
        start_pos_x = 0
        start_pos_y = 0
        end_pos_x = self.resolution[0]
        end_pos_y = 0

        pos_iter = 0
        while pos_iter < self.resolution[0]:
            self.line_points.append(((start_pos_x, start_pos_y + pos_iter), (end_pos_x, end_pos_y + pos_iter)))
            pos_iter += NUMBER_OF_PIXELS

    def draw_lines(self):
        for line in self.line_points:
            pygame.draw.line(self.screen, (0, 0, 0), line[0], line[1])


def proceed(window: Window, actual: (int, int)) -> (int, int):
    actual_square = window.langton.get_square(actual)
    next_step = window.step_list[(actual_square.state + 1) % len(window.step_list)]
    take_care_of_square(actual_square, next_step)

    actual_step = window.step_list[actual_square.state]
    if actual_step.letter == 'L':
        window.move = turn_left(window.move)
    else:
        window.move = turn_right(window.move)

    return make_a_move(window, actual)


def make_a_move(window: Window, actual: (int, int)) -> (int, int):
    neutral = actual
    if not window.moveable:
        return neutral
    if 0 >= actual[0] + window.move[0]:
        window.moveable = False
        return neutral
    elif window.resolution[0] <= (actual[0] + window.move[0])*NUMBER_OF_PIXELS:
        window.moveable = False
        return neutral
    elif 0 >= actual[1] + window.move[1]:
        window.moveable = False
        return neutral
    elif window.resolution[1] <= (actual[1] + window.move[1])*NUMBER_OF_PIXELS:
        window.moveable = False
        return neutral
    else:
        return actual[0] + window.move[0], actual[1] + window.move[1]


def take_care_of_square(square: MyRect, next_step: Step):
    square.color = next_step.color
    square.state = next_step.number
    window.draw_rect(square)

if __name__ == '__main__':
    #10k
    #command = "RL"

    #82k and not found
    #command = "LRLRR"

    #symetrical
    #command = "LLRR"

    #square
    command = "LRRRRRLLR"
    window = Window((1400, 1000), (255, 255, 255), command)
    window.main_loop()
