import pygame
import sys

import constants
import constants as c
import sound

# Entities
from font import get_font
from button import Button
from stars import create_small_stars, create_medium_stars, create_big_stars

# Entities
from Enemies.EnemyBullet import EnemyBullet
from player import player, playerBullet_group
from Enemies.bigbad import big_bads
from Enemies.Pitgo import pitgos, enemyBullet_group
from Enemies.zako import zako

pygame.init()

SCREEN = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Galaga")
clock = pygame.time.Clock()

BG = pygame.image.load("Sprites/Menus/Main_Menu.png")

# Entities
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(big_bads)
all_sprites.add(pitgos)


def play():
    pygame.mixer.music.stop()
    sound.start_level.play()

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(8).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(c.WIDTH / 2, c.HEIGHT / 2 + 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(c.WIDTH / 2, c.HEIGHT / 2 + 200),
                           text_input="BACK", font=get_font(8), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        SCORE_TEXT = get_font(8).render(f"SCORE {c.player_score}", True, c.RED)
        SCORE_RECT = PLAY_TEXT.get_rect(center=(c.WIDTH / 2, 4))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        create_small_stars(SCREEN, c.WHITE, 4)

        all_sprites.draw(SCREEN)
        all_sprites.update()
        enemyBullet_group.draw(SCREEN)
        enemyBullet_group.update()
        playerBullet_group.draw(SCREEN)
        playerBullet_group.update()

        pygame.display.update()
        clock.tick(c.FPS)
        if c.player_score >= 1000:
            c.FPS = 60
        if c.player_score >= 2000:
            c.FPS = 90



def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.mixer.music.load("Sounds/Menu.mp3")
    pygame.mixer.music.play(-1)

    while True:
        SCREEN.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(32).render("GALAGA", True, c.LIGHT_GREEN)
        MENU_RECT = MENU_TEXT.get_rect(center=(c.WIDTH / 2, c.HEIGHT / 2 - 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_CREDITS_TEXT = get_font(8).render("Jaime, Luis, and Gerson", True, c.YELLOW)
        MENU_CREDITS_RECT = MENU_TEXT.get_rect(center=(c.WIDTH / 2, c.HEIGHT / 2 - 40))
        SCREEN.blit(MENU_CREDITS_TEXT, MENU_CREDITS_RECT)

        PLAY_BUTTON = Button(image=None, pos=(c.WIDTH / 2, c.HEIGHT / 2),
                             text_input="PLAY", font=get_font(8), base_color=c.LIGHT_BLUE, hovering_color=c.WHITE)
        OPTIONS_BUTTON = Button(image=None, pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color=c.WHITE)
        QUIT_BUTTON = Button(image=None, pos=(c.WIDTH / 2, c.HEIGHT / 2 + 40),
                             text_input="QUIT", font=get_font(8), base_color=c.RED, hovering_color=c.WHITE)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        create_small_stars(SCREEN, c.LIGHT_BLUE)
        create_medium_stars(SCREEN, c.YELLOW)
        create_big_stars(SCREEN, c.WHITE)

        pygame.display.update()




main_menu()
