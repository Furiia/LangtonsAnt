import pyg


class State:
    def __init__(self, number: int, color: (int, int, int), command: str):
        self.number = number
        self.color = color
        self.command = command


class Machine:
    def __init__(self, commands: str = None):
        self.states_list = []
        if commands is not None:
            self.generate_states_list_from_command(commands)

    def get_states_list(self) -> [State]:
        return self.states_list

    def get_state(self, number: int) -> State:
        return self.states_list[number]

    def get_next_state(self, number: int) -> State:
        return self.states_list[(number + 1) % len(self.states_list)]

    def generate_states_list_from_command(self, commands):
        self.__parse(commands)

    def __parse(self, commands: str):
        number = 0
        for command in commands:
            self.states_list.append(State(number, pyg.COLORS[number % len(commands)], command))
            number += 1
