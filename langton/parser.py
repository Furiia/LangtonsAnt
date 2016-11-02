class Step:
    def __init__(self, number: int, letter: str):
        self.number = number
        self.color = colors[number]
        self.letter = letter

colors = [(255, 255, 255),
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


def transform(commands: str) -> [Step]:
    number = 0
    result = []
    for letter in commands:
        result.append(Step(number, letter))
        number += 1
    return result

move_up = (-1, 0)
move_right = (0, 1)
move_down = (1, 0)
move_left = (0, -1)

move_list = [move_up, move_right, move_down, move_left]


def turn_right(vec: (int, int)):
    for i in range(0, 4):
        if move_list[i] == vec:
            return move_list[(i + 1) % 4]


def turn_left(vec: (int, int)):
    for i in range(0, 4):
        if move_list[i] == vec:
            return move_list[(i - 1) % 4]


if __name__ == '__main__':
    a1 = transform('LRLRR')
    for elem in a1:
        print("%s : %s" %(elem.number, elem.letter))
