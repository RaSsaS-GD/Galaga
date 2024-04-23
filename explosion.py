import pygame

import constants as c

pygame.init()


class explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.image.load("Sprites/VFX/Explosion1.png"),
                       pygame.image.load("Sprites/VFX/Explosion2.png"),
                       pygame.image.load("Sprites/VFX/Explosion3.png"),
                       pygame.image.load("Sprites/VFX/Explosion4.png"),
                       pygame.image.load("Sprites/VFX/Explosion5.png")]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_speed = 0.1
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

