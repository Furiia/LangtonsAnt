from pyg.object import MyRect
from pyg import NUMBER_OF_PIXELS


class LangtonAntsStructure:
    def __init__(self, resolution: (int, int)):
        self.number_of_x_squares = resolution[0]//NUMBER_OF_PIXELS
        self.number_of_y_squares = resolution[1]//NUMBER_OF_PIXELS
        self.square_map = {}
        self.__generate_square_map()

    def __generate_square_map(self):
        for i in range(0, self.number_of_x_squares):
            for j in range(0, self.number_of_y_squares):
                self.square_map[(i, j)] = MyRect(i*NUMBER_OF_PIXELS, j*NUMBER_OF_PIXELS, NUMBER_OF_PIXELS, NUMBER_OF_PIXELS)

    def get_first_square(self) -> MyRect:
        return self.square_map[(self.number_of_x_squares//2, self.number_of_y_squares//2)]

    def get_first_pos(self) -> (int, int):
        return (self.number_of_x_squares//2, self.number_of_y_squares//2)

    def get_square(self, pos: (int, int)) -> MyRect:
        return self.square_map[pos]

