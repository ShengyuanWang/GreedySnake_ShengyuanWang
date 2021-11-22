import pygame
import time
class Settings():
    def __init__(self):
        self.bg_color = (204,255,153)
        self.screen_width = 800
        self.screen_height = 600

        self.cell_size = 20
        assert self.screen_height % self.cell_size == 0
        assert self.screen_width % self.cell_size == 0
        self.cell_w = int(self.screen_width / self.cell_size)  # the number of grid in one row
        self.cell_h = int(self.screen_height / self.cell_size)  # the number of grid in one column
        self.num = self.cell_w * self.cell_h
        self.free_place = (self.cell_w + 1) * (self.cell_h + 1)
        self.snake_place = 2 * self.free_place

        # dictionary of moving direction
        self.move_directions = {
            'left': -1,
            'right': 1,
            'up': -self.cell_w,
            'down': self.cell_w
        }

        self.ERR = -404
        self.best_move = self.ERR
        self.Head_index = 0

        self.length = 0    # the length of snake
        self.game_stats = 0  # game status
        self.score = 0  # game score

        self.clock_frq = 5  #frequency
        self.display_clock = 60  # ai mode frequency
        self.my_clock = pygame.time.Clock()




