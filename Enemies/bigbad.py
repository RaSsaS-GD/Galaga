import random
import constants as c

import pygame
from player import playerBullet_group

speed = 5
bigbad_image = pygame.image.load("Sprites/Pogo.png")


class BIGBAD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = bigbad_image
        self.image = pygame.transform.scale(self.original_image, (75, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, c.WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        self.score = 500

    def update(self):
        self.rect.y += speed
        if self.rect.y > c.HEIGHT:
            self.rect.y = random.randint(-200, 50)
            self.rect.x = random.randint(0, c.WIDTH - self.rect.width)
        hit = pygame.sprite.spritecollide(self, playerBullet_group, True)
        if hit:
            c.player_score += self.score
            self.kill()


big_bads = [BIGBAD() for i in range(5)]
