import random

import pygame
from Constants import *
from Search import *
vec = pygame.math.Vector2

"""
This is a Player class which help us to draw Hero, moving he and other useful events
"""


class Player:
    def __init__(self, application, pos):
        self.application = application
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.old_grid_pos = None
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(0, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = PLAYER_LIVES
        self.destination = DESTINATION
        self.points = self.generate_4_points()
        self.c = None
        # self.path = a_star(self.application.grid_map, (int(self.grid_pos[1]), int(self.grid_pos[0])), self.destination,
        #                    take_all_coins_heuristic, self.application.coins)
        self.path, self.c = self.way_through_all_points()

    def update(self):
        """
        This is a main function to update the Hero. There is a check of eating the coin,
        death from Ghost and some magic with Teleports
        :return:
        """
        if self.able_to_move:
            self.pix_pos += self.direction*self.speed
        if self.is_in_bounds():
            if self.stored_direction is not None:
                self.direction = self.stored_direction
            self.able_to_move = self.is_able_to_move()

        new_pos = [(self.pix_pos[0] - PADDING + self.application.cell_width // 2) // self.application.cell_width + 1,
                        (self.pix_pos[1] - PADDING + self.application.cell_height // 2) // self.application.cell_height + 1]

        if new_pos != self.grid_pos:
            self.old_grid_pos = self.grid_pos
            self.grid_pos = new_pos

            start = (int(self.grid_pos[1]), int(self.grid_pos[0]))
            end = self.destination
            # self.path = a_star(self.application.grid_map, start, end, take_all_coins_heuristic, self.application.coins)
            self.path, self.c = self.way_through_all_points()

        if self.on_coin():
            self.eat_coin()
        if self.on_enemy():
            self.application.remove_life()
        self.on_teleport()

    def draw(self):
        """
        Draw the Hero
        :return:
        """
        pygame.draw.circle(self.application.screen, PLAYER_COLOUR, (int(self.pix_pos.x),
                                                                    int(self.pix_pos.y)), self.application.cell_width // 2 - 2)

        for x in range(self.lives):
            pygame.draw.circle(self.application.screen, GREEN, (30 + 20 * x, HEIGHT - 15), 7)

    def draw_path(self):

        if self.c is not None:
            for c in self.c[1:-1]:
                pygame.draw.circle(self.application.screen, YELLOW,
                                   (c[1] * self.application.cell_width + 10 + PADDING // 2,
                                    c[0] * self.application.cell_height + 10 + PADDING // 2), 6)

        for p in self.path:
            pygame.draw.circle(self.application.screen, (0, 255, 0),
                               (p[1] * self.application.cell_width + 10 + PADDING // 2,
                                p[0] * self.application.cell_height + 10 + PADDING // 2), 4)


    def way_through_4_points(self):
        hero = (self.grid_pos[1], self.grid_pos[0])
        points = [hero] + self.points
        points.append(self.destination)
        if hero in self.points:
            self.points.remove(hero)
        routs = []
        for j in range(len(points) - 1):
            temp_routs = []
            for i in range(j + 1, len(points)):
                point1 = (int(points[j][0]), int(points[j][1]))
                point2 = (int(points[i][0]), int(points[i][1]))
                temp_routs.append(a_star(self.application.grid_map, point1, point2, euclid_heuristic, 0))
            routs += min(temp_routs, key=len)

        return routs, points

    def way_through_all_points(self):
        coins = []
        for c in self.application.coins:
            coins.append((c[1], c[0]))
        hero = (self.grid_pos[1], self.grid_pos[0])
        points = [hero] + coins
        points.append(self.destination)

        if hero in self.points:
            self.points.remove(hero)
        routs = []
        for j in range(len(points) - 1):
            temp_routs = []
            for i in range(j + 1, len(points)):
                point1 = (int(points[j][0]), int(points[j][1]))
                point2 = (int(points[i][0]), int(points[i][1]))
                temp_routs.append(a_star(self.application.grid_map, point1, point2, euclid_heuristic, 0))
            routs += min(temp_routs, key=len)

        return routs, points

    def generate_4_points(self):
        points = []
        for _ in range(4):
            point = random.choice(self.application.coins)
            points.append((point[1], point[0]))
        return points
    def on_coin(self):
        """Check is Hero on coin"""
        if self.grid_pos in self.application.coins:
            return True
        return False

    def eat_coin(self):
        """
        Eating the coin
        :return:
        """
        self.application.coins.remove(self.grid_pos)
        self.current_score += 1

    def on_teleport(self):
        """
        This method allow Hero to use Teleport
        :return:
        """
        if self.grid_pos in self.application.teleports:
            if self.grid_pos == self.application.teleports[0]:
                self.grid_pos = self.application.teleports[1] + vec((-1, 0))
                self.pix_pos = self.get_pix_pos()
            elif self.grid_pos == self.application.teleports[1]:
                self.grid_pos = self.application.teleports[0] + vec((1, 0))
                self.pix_pos = self.get_pix_pos()
            elif self.grid_pos == self.application.teleports[2]:
                self.grid_pos = self.application.teleports[3] + vec((-1, 0))
                self.pix_pos = self.get_pix_pos()
            elif self.grid_pos == self.application.teleports[3]:
                self.grid_pos = self.application.teleports[2] + vec((1, 0))
                self.pix_pos = self.get_pix_pos()

    def on_enemy(self):
        """
        Check is Hero on Enemy...
        Should I move this method to Enemy class
        :return:
        """
        for enemy in self.application.enemies:
            if enemy.position == self.grid_pos:
                return True

    def change_direction(self, direction):
        """

        :param direction: Vector(int, int) - direction to move.
        Description: (1,0) - East
                     (-1,0) - West
                     (0, 1) - South
                     (0,-1) - North
        :return:
        """
        self.stored_direction = direction

    def get_pix_pos(self):
        """
        Using grid position to calculate a pixel position on game screen
        :return: vec(x_pixel_position, y_pixel_position)
        """
        return vec((self.grid_pos[0] * self.application.cell_width) + PADDING // 2 + self.application.cell_width // 2,
                   (self.grid_pos[1] * self.application.cell_height) +
                   PADDING // 2 + self.application.cell_height // 2)

    def is_in_bounds(self):
        """
        Checking is Hero inside a cell to avoid Hero clipping in textures
        :return:
        """
        if int(self.pix_pos.x + PADDING // 2) % self.application.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y + PADDING // 2) % self.application.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def is_able_to_move(self):
        """
        Checking next cell considering direction
        :return:
        """
        for wall in self.application.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True
