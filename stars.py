import random
import pygame
import constants as c

clock = pygame.time.Clock()

# Stars
star_field_small = []
star_field_medium = []
star_field_big = []

for slow_stars in range(50):
    star_loc_x = random.randrange(0, c.WIDTH)
    star_loc_y = random.randrange(0, c.HEIGHT)
    star_field_small.append([star_loc_x, star_loc_y])

for medium_stars in range(35):
    star_loc_x = random.randrange(0, c.WIDTH)
    star_loc_y = random.randrange(0, c.HEIGHT)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(15):
    star_loc_x = random.randrange(0, c.WIDTH)
    star_loc_y = random.randrange(0, c.HEIGHT)
    star_field_big.append([star_loc_x, star_loc_y])


def create_small_stars(screen, col, speed=8):
    for star in star_field_small:
        star[1] += speed
        if star[1] > c.HEIGHT:
            star[0] = random.randrange(0, c.WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, col, star, 1)


def create_medium_stars(screen, col, speed=4):
    for star in star_field_medium:
        star[1] += speed
        if star[1] > c.HEIGHT:
            star[0] = random.randrange(0, c.WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, col, star, 2)


def create_big_stars(screen, col, speed=1):
    for star in star_field_big:
        star[1] += speed
        if star[1] > c.HEIGHT:
            star[0] = random.randrange(0, c.WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, col, star, 3)

    pygame.display.flip()

    clock.tick(30)
