import math
import pygame


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image = pygame.transform.flip(pygame.image.load("Sprites/Pitgo/Fireball.png"), False, True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.angle = angle
        self.counter = 0
        self.speedx = 2
        self.speedy = 2

    def update(self):
        self.rect.x += self.speedx * math.cos(math.radians(self.angle))
        self.rect.y += self.speedy * math.sin(math.radians(self.angle))
        if self.rect.bottom < 0:
            self.kill()
