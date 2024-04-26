import random

import constants as c
import math
import pygame
from player import playerBullet_group
import Enemies.EnemyBullet as e

enemies = pygame.sprite.Group()
enemyBullet_group = pygame.sprite.Group()


class Pitgo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.transform.flip(pygame.image.load("Sprites/Pitgo/Pitgo_0.png"), False, True),
                       pygame.transform.flip(pygame.image.load("Sprites/Pitgo/Pitgo_1.png"), False, True)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, c.WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        self.animation_speed = 0.1
        self.last_update = pygame.time.get_ticks()
        self.direction = 1  # To control horizontal movement direction
        self.amplitude = 0  # Oscillation amplitude
        self.frequency = 0.05  # Oscillation frequency
        self.shoot_delay = random.randint(7000, 10000)  # Delay between shots
        self.last_shot = pygame.time.get_ticks()
        self.score = 125

    def update(self):
        self.rect.y += 1
        if self.rect.y > c.HEIGHT:
            self.rect.y = random.randint(-200, -50)
            self.rect.x = random.randint(0, c.WIDTH - self.rect.width)

        # Horizontal movement (zako-like motion)
        self.rect.x += self.direction
        if self.rect.x <= 0 or self.rect.x >= c.WIDTH - self.rect.width:
            self.direction *= -1  # Reverse direction if hitting screen edge

        # Vertical oscillation
        self.rect.y += self.amplitude * math.sin(self.frequency * pygame.time.get_ticks())

        # Animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        # Shoot bullets
        self.shoot(5, 72)

        # Collision detection with bullets
        hit = pygame.sprite.spritecollide(self, playerBullet_group, True)
        if hit:
            self.kill()
            c.player_score += self.score

    def shoot(self, amount, angle):
        pp = 0
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            pp += 1
            for x in range(amount):
                new_bullet = e.EnemyBullet(self.rect.centerx, self.rect.bottom, angle * x)
                enemyBullet_group.add(new_bullet)
            if pp >= 1:
                self.kill()


pitgos = [Pitgo() for i in range(10)]
