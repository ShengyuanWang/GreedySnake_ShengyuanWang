"""
Course: CS123
Professor: Susan Fox
Editor: Shengyuan Wang
"""

import random


class Snake():
    def __init__(self, ai_settings):
        self.reset(ai_settings)

    # initial a snake
    def reset(self, ai_settings):
        # the location of the snake
        self.start_x = random.randint(5, ai_settings.cell_w - 6)
        self.start_y = random.randint(5, ai_settings.cell_h - 6)
        self.head_index = 0
        # the default moving position of the snake
        self.direction = 'right'
        # the dictionary of the intial position of snake, the snake initially have the position of snake and the left two grids
        self.coords = [{'x': self.start_x, 'y': self.start_y},
                       {'x': self.start_x - 1, 'y': self.start_y},
                       {'x': self.start_x - 2, 'y': self.start_y}]

    # update the snake, every time the snake move, we should insert a new snake head in the location of the dictionary
    # from the commen sense, every time the snake move, both the head and the tail move towards, but in the function we
    # refuse the deal with the taol bcause if the snake eat food, the tail actually not move.

    def update(self):
        newHead = {}
        # decide the snake head accoridng to the moving direction
        if self.direction == 'up':
            newHead = {'x': self.coords[self.head_index]['x'],
                       'y': self.coords[self.head_index]['y'] - 1}
        elif self.direction == 'down':
            newHead = {'x': self.coords[self.head_index]['x'],
                       'y': self.coords[self.head_index]['y'] + 1}
        elif self.direction == 'left':
            newHead = {'x': self.coords[self.head_index]['x'] - 1,
                       'y': self.coords[self.head_index]['y']}
        elif self.direction == 'right':
            newHead = {'x': self.coords[self.head_index]['x'] + 1,
                       'y': self.coords[self.head_index]['y']}
        self.coords.insert(0, newHead)



