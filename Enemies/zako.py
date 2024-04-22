import pygame
import sys

import constants as c
from player import playerBullet_group

zako_image = pygame.image.load("Sprites/Zako.png")

class Zako(pygame.sprite.Sprite):
    def __init__(self, initial_position, waypoints, wait_time):
        super().__init__()
        self.image = zako_image
        self.rect = self.image.get_rect()
        self.rect.center = initial_position
        self.waypoints = waypoints
        self.current_waypoint_index = 0
        self.wait_times = wait_times
        self.wait_timer = 0
        self.speed = 2

    def update(self):
        hit = pygame.sprite.spritecollide(self, playerBullet_group, True)
        if hit:
            self.kill()

        if self.current_waypoint_index < len(self.waypoints):
            if self.wait_timer > 0:
                self.wait_timer -= 1
            else:
                target = self.waypoints[self.current_waypoint_index]
                dx = target[0] - self.rect.centerx
                dy = target[1] - self.rect.centery
                dist = (dx ** 2 + dy ** 2) ** 0.5
                if dist < self.speed:
                    self.wait_timer = self.wait_times[self.current_waypoint_index]
                    self.current_waypoint_index += 1
                else:
                    move_x = dx / dist * self.speed
                    move_y = dy / dist * self.speed
                    self.rect.move_ip(move_x, move_y)


waypoints = [(c.WIDTH, c.HEIGHT), (c.WIDTH // 2 + 30, c.HEIGHT / 2 + 40), c.WIDTH, c.HEIGHT]
wait_times = [120, 90, 60]  # Wait times in frames for each waypoint

zako = Zako((c.WIDTH, c.HEIGHT), waypoints, wait_times)
