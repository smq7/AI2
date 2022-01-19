import asyncio
import random
import time
import timeit
import numpy as np
import pygame
from Constants import *
vec = pygame.math.Vector2

import queue

class Enemy:
    """
    This class describe an Enemy class in Pacman game (Ghost).
    Now it is only for add AFK enemy. All mob functional will be added later, in next labs.
    """
    def __init__(self, application, start_position, ghost_type = RANDOM):
        self.type = None
        self.application = application
        self.position = start_position
        self.pix_position = self.get_pix_pos()
        self.path = None
        self.grid_position = start_position
        self.direction = vec(0, 0)
        self.personality = ghost_type
        self.speed = 2

    def draw(self):
        """
        Drawing the Ghost with some parameters, like color, position and size
        :return:
        """
        pygame.draw.circle(self.application.screen, ICE_COLOR,
                           (self.pix_position.x, self.pix_position.y),
                           self.application.cell_width//2-2)

    def get_pix_pos(self):
        """
        This method finds a pixel position of Ghost to make more easier to draw it on map.
        :return: vector(x,y) where x is an X coordinate the center of Ghost. y - Y coordinate with same meaning.
        """
        return vec((self.position[0]*self.application.cell_width) + PADDING // 2 + self.application.cell_width // 2,
                   (self.position[1]*self.application.cell_height) +
                   PADDING // 2 + self.application.cell_height // 2)

    def update(self):
        self.target = (int(self.application.player.grid_pos[1]), int(self.application.player.grid_pos[0]))
        if self.target != self.grid_position:
            self.pix_position += self.direction * self.speed
            if self.time_to_move():
                self.move()

        # Setting grid position in reference to pix position
        self.grid_position[0] = (self.pix_position[0]-PADDING +
                            self.application.cell_width//2)//self.application.cell_width+1
        self.grid_position[1] = (self.pix_position[1]-PADDING +
                            self.application.cell_height//2)//self.application.cell_height+1

    def time_to_move(self):
        if int(self.pix_position.x+PADDING//2) % self.application.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_position.y+PADDING//2) % self.application.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True
        return False

    def get_random_direction(self):
        while True:
            rand_int = random.randint(0, 3)
            random_direction = vec(0, 0)
            if rand_int == 0:
                random_direction = vec(-1, 0)
            elif rand_int == 1:
                random_direction = vec(1, 0)
            elif rand_int == 2:
                random_direction = vec(0, 1)
            elif rand_int == 3:
                random_direction = vec(0, -1)
            if vec(self.grid_position + random_direction) not in self.application.walls:
                return random_direction

    def move(self):
        if self.personality == RANDOM:
            self.direction = self.get_random_direction()


    def load_grid(self):
        grid = np.zeros((ROWS+1, COLS), dtype=int)
        with open("./Game_data/Map.txt", "r") as file:
            for y, line in enumerate(file):
                for x, char in enumerate(line[:-1]):
                    if char == "W":
                        grid[y, x] = 1
                    else:
                        grid[y, x] = 0
        return grid

    def is_valid_target(self, target):
        grid = self.load_grid()
        if grid[int(target.y), int(target.x)] == 1:
            return False
        else:
            return True

    def exec_timer(self):
        ucs = []
        bfs = []
        dfs = []
        for i in range(10):
            start = np.random.randint(1, 25, (1, 2))[0]
            target = np.random.randint(1, 25, (1, 2))[0]
            start = vec(start[0], start[1])
            target = vec(target[0], target[1])

            if self.is_valid_target(start) and self.is_valid_target(target):
                start_time = time.time()
                for i in range(100):
                    self.UCS(start, target)
                ucs.append(time.time() - start_time)

                start_time = time.time()
                for i in range(100):
                    self.BFS(start, target)
                bfs.append(time.time() - start_time)

                start_time = time.time()
                for i in range(100):
                    self.DFS(start, target)
                dfs.append(time.time() - start_time)

        print(f"Середній час виконання UCS = {np.mean(ucs)}")
        print(f"Середній час виконання BFS = {np.mean(bfs)}")
        print(f"Середній час виконання DFS = {np.mean(dfs)}")

