import random
import pygame
import constants as c

clock = pygame.time.Clock()

# Stars
star_field_slow = []
star_field_medium = []
star_field_fast = []

for slow_stars in range(50):
    star_loc_x = random.randrange(0, c.WIDTH)
    star_loc_y = random.randrange(0, c.HEIGHT)
    star_field_slow.append([star_loc_x, star_loc_y])

for medium_stars in range(35):
    star_loc_x = random.randrange(0, c.WIDTH)
    star_loc_y = random.randrange(0, c.HEIGHT)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(15):
    star_loc_x = random.randrange(0, c.WIDTH)
    star_loc_y = random.randrange(0, c.HEIGHT)
    star_field_fast.append([star_loc_x, star_loc_y])

def create_stars(screen, col1, col2, col3):
    for star in star_field_slow:
        star[1] += 1
        if star[1] > c.HEIGHT:
            star[0] = random.randrange(0, c.WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, col1, star, 3)

    for star in star_field_medium:
        star[1] += 4
        if star[1] > c.HEIGHT:
            star[0] = random.randrange(0, c.WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, col2, star, 2)

    for star in star_field_fast:
        star[1] += 8
        if star[1] > c.HEIGHT:
            star[0] = random.randrange(0, c.WIDTH)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, col3, star, 1)

    pygame.display.flip()

    clock.tick(30)
