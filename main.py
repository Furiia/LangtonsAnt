import pyg
import pygame
from pyg.object import MySquare
from pyg.window import PyWindow
from langton.automata import Machine

window_obj = None
clock = pygame.time.Clock()
clock.tick(pyg.FPS_LIMIT)
square_tab = []
machine = None
actual_position = None
square = MySquare()


def main_loop():
    global clock
    loop_counter = 0
    event_map = dict()
    event_map['running'] = True
    event_map['space_pressed'] = False
    while event_map['running']:
        event_loop(event_map)
        if event_map['space_pressed']:
            continue
        if loop_counter % 1000 == 0:
            print(loop_counter)
        elif loop_counter % 100 == 0:
            print("fps: %s" % (clock.get_fps()))
        next_step()
        pygame.display.flip()
        loop_counter += 1
        clock.tick(pyg.FPS_LIMIT)


def event_loop(event_map: dict):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event_map['running'] = False
        if event.type == pygame.KEYDOWN:
            global clock
            if event.key == pygame.K_SPACE:
                event_map['space_pressed'] = not event_map['space_pressed']
            elif event.key == pygame.K_KP_MINUS:
                pyg.FPS_LIMIT -= 1
                clock.tick(pyg.FPS_LIMIT)
                print(pyg.FPS_LIMIT)
            elif event.key == pygame.K_KP_PLUS:
                pyg.FPS_LIMIT += 1
                clock.tick(pyg.FPS_LIMIT)
                print(pyg.FPS_LIMIT)


def prepare_knowledge_space():
    global square_tab
    number_of_squares_x = pyg.RESOLUTION[0]//pyg.NUMBER_OF_PIXELS
    number_of_squares_y = pyg.RESOLUTION[1]//pyg.NUMBER_OF_PIXELS
    for i in range(0, number_of_squares_x):
        result_tab = []
        for j in range(0, number_of_squares_y):
            result_tab.append(0)
        square_tab.append(result_tab)


def start(commands: str):
    global machine
    global window_obj
    prepare_knowledge_space()
    machine = Machine(commands=commands)
    window_obj = PyWindow(pyg.RESOLUTION, pyg.BASE_COLOR)
    window_obj.draw_lines()
    main_loop()


def next_step():
    global machine
    global window_obj
    global square
    actual_state_number = square_tab[square.position_tab[0]][square.position_tab[1]]
    actual_state = machine.get_state(actual_state_number)
    next_state = machine.get_next_state(actual_state_number)
    square_tab[square.position_tab[0]][square.position_tab[1]] = next_state.number
    square.rotate_movement_vector(actual_state.command)
    square.draw_square(window_obj.surface, next_state)
    square.move_square()


if __name__ == '__main__':
    command = "LR"
    start(command)

