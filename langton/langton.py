from pyg.object import MyRect


class LangtonAntsStructure:
    def __init__(self, resolution: (int, int)):
        self.number_of_x_squares = resolution[0]//10
        self.number_of_y_squares = resolution[1]//10
        self.square_map = {}
        self.__generate_square_map()
        self.__next_stage_of_square(self.get_first_square())

    def __generate_square_map(self):
        for i in range(0, self.number_of_x_squares):
            for j in range(0, self.number_of_y_squares):
                self.square_map[(i, j)] = MyRect(i*10, j*10, 10, 10)

    def get_first_square(self) -> MyRect:
        return self.square_map[(self.number_of_x_squares//2, self.number_of_y_squares//2)]

    def __next_stage_of_square(self, square: MyRect):
        square.color = (255, 0, 0)
