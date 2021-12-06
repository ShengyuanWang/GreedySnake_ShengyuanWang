"""
Course: CS123
Professor: Susan Fox
Editor: Shengyuan Wang
"""
import random

class Food():
    def __init__(self, ai_settings, snake):
        """
        this function aims to update the food position according to the input of ai setting and snake
        :param ai_settings: the setting of ai
        :param snake: the snake
        """
        self.update(ai_settings, snake)

    # Every time the snake eats the food, find another new place to place food
    def update(self, ai_settings, snake):
        """
        this function aims to update the food position according to the input of ai setting and snake
        :param ai_settings: the setting of ai
        :param snake: the snake
        :return: no return
        """
        flag = True
        food = {}
        while flag:
            food = {'x': random.randint(0, ai_settings.cell_w - 1),
                    'y': random.randint(0, ai_settings.cell_h - 1)}
            # When the new place is on the snake's body, find another place
            if food not in snake.coords:
                flag = False
        self.coord = food
