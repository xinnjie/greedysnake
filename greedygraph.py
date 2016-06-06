from point import point
from copy import deepcopy
from random import randrange
import time
import os
from inputwithoutwait import getch
class GreedySnake:
    def __init__(self, pos_x, pos_y, pat='o'):     # 方向是否合法交给controler控制
        self.__len = 1
        self.__pat = pat
        self.__head = point(pos_x, pos_y)
        self.__body = [deepcopy(self.__head)]

    @property
    def pat(self):
        return self.__pat

    @property
    def body(self):
        return self.__body

    def grow(self):
        self.__body.insert(0, deepcopy(self.__body[0]))

    def move_right(self):
        self.__body.pop()
        self.__head.x += 1
        self.__body.append(deepcopy(self.__head))

    def move_left(self):
        self.__body.pop()
        self.__head.x -= 1
        self.__body.append(deepcopy(self.__head))

    def move_up(self):
        self.__body.pop()
        self.__head.y -= 1
        self.__body.append(deepcopy(self.__head))

    def move_down(self):
        self.__body.pop()
        self.__head.y += 1
        self.__body.append(deepcopy(self.__head))

    def __str__(self):
        body = ''
        for point in self.__body:
            body += str(point)
        return body

class GreedyFruit:
    def __init__(self):
        return None

class GreedyGraph:
    def __init__(self, length, width, autofill=' '):
        self.__len = length
        self.__wid = width
        self.__autofill = autofill

    def paint(self, the_snake, the_fruit=None):
        self.__graph = [[self.__autofill for i in range(self.__wid)] for i in range(self.__len)]
        assert isinstance(the_snake, GreedySnake), print('snake is needed!')
        snake_pat = the_snake.pat
        for p in the_snake.body:
            self.__graph[p.x][p.y] = snake_pat

        for line in self.__graph:
            for pix in line:
                print(pix, end='')
            print()

class DirectionError(Exception):
    pass

class GreedyController:
    direct = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
    def __init__(self, the_snake, init_direction='right'):
        self.__cur_direction = init_direction
        self.__snake = the_snake

    @property
    def cur_direction(self):
        return self.__cur_direction

    @cur_direction.setter
    def cur_direction(self, direction):
        if direction not in GreedyController.direct.keys():
            raise DirectionError
        else:
            self.__cur_direction = GreedyController.direct[direction]

    def turn(self, direction):
        if GreedyController.direct[direction] == self.cur_direction:
            pass
        else:
            try:
                self.cur_direction == Controller.direct[direction]
            except DirectionError as e:
                print(e, 'direcion should be in w,s,a,d')

class GreedyApp:
    def __init__(self, length, width):
        self.__len = length
        self.__wid = width
        self.__graph = GreedyGraph(length, width)
        self.__snake = GreedySnake(length//2, width//2)
        self.__controller = GreedyController(self.__snake)

    def run(self):
        self.__graph.paint(self.__snake)
        while True:

            os.system('clear')





if __name__ == '__main__':
    length = 30
    width = 30
    graph = GreedyGraph(length, width)
    snake = GreedySnake(length//2, width//2)
    print(snake)

    print('-' * width)
    graph.paint(snake)
    print('-' * width)

    snake.move_right()
    print(snake)
    snake.grow()
    snake.move_down()
    print(snake)

    print('-'*width)
    graph.paint(snake)
    print('-'*width)

    controller = GreedyController(snake)
