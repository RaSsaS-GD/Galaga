import pygame
import constants as c

player_image = pygame.image.load("Sprites/Player.png")
playerBullet_image = pygame.image.load("Sprites/Player_Bullet.png")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (c.WIDTH // 2, c.HEIGHT // 2 - 50)
        self.last_shot_time = 0  # Track the time of the last shot

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= c.player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < c.WIDTH:
            self.rect.x += c.player_speed
        # if keys[pygame.K_UP] and self.rect.top > 0:
        #    self.rect.y -= c.player_speed
        # if keys[pygame.K_DOWN] and self.rect.bottom < c.HEIGHT:
        #    self.rect.y += c.player_speed

        # Shooting
        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()  # Get the current time
            if current_time - self.last_shot_time > c.player_shot_cooldown:
                # Only shoot if enough time has passed since the last shot
                self.playerBullet = PlayerBullet(self.rect.centerx, self.rect.top)
                playerBullet_group.add(self.playerBullet)
                self.last_shot_time = current_time  # Update the last shot time


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = playerBullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= c.playerBullet_speed


player = Player()
playerBullet_group = pygame.sprite.Group()
