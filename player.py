import pygame
import constants as c

playerBullet_group = pygame.sprite.Group()

player_image = pygame.image.load("Sprites/Player.png")
playerBullet_image = pygame.image.load("Sprites/Player_Bullet.png")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (c.WIDTH // 2, c.HEIGHT // 2)
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= c.player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < c.WIDTH:
            self.rect.x += c.player_speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= c.player_speed
        if keys[pygame.K_DOWN] and self.rect.bottom < c.HEIGHT:
            self.rect.y += c.player_speed

        # Shooting
        if keys[pygame.K_SPACE] and c.time_now - self.last_shot > c.player_shot_cooldown:
            self.playerBullet = PlayerBullet(self.rect.centerx, self.rect.top)
            playerBullet_group.add(self.playerBullet)
            self.last_shot = c.time_now


player = Player()


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = playerBullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= c.playerBullet_speed
