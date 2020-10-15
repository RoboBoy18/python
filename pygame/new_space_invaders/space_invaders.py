import sys
from os.path import abspath, dirname
import pygame

pygame.init()

# Create screen
SCREEN = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Space Invaders")

# Path
BASE_PATH = abspath(dirname(__file__))

# Font
FONT_PATH = BASE_PATH + "/fonts/"
FONT = FONT_PATH + "space_invaders.ttf"
TITLE_FONT = pygame.font.Font(FONT, 50)
SUB_TITLE_FONT = pygame.font.Font(FONT, 25)
MAIN_FONT = pygame.font.Font(FONT, 20)

# Image and sound
IMAGE_PATH = BASE_PATH + "/images/"
SOUND_PATH = BASE_PATH + "/sounds/"

# Icon
ICON = pygame.image.load(IMAGE_PATH + "ufo.png")
pygame.display.set_icon(ICON)

# Background image
BACKGROUND = pygame.image.load(IMAGE_PATH + "background.jpeg")

# Ship
SHIP = pygame.image.load(IMAGE_PATH + "ship.png")
ship_rect = SHIP.get_rect(topleft=(375, 540))
SHIP_SPEED = 5

# Enemy1
ENEMY1 = pygame.image.load(IMAGE_PATH + "enemy1.png")
# Resize enemy1
enemy1 = pygame.transform.scale(ENEMY1, (40, 40))

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (78, 255, 87)

# Game variables
CLOCK = pygame.time.Clock()
FPS = 60


def main_menu():
    global ENEMY1, enemy1

    while True:
        CLOCK.tick(FPS)

        title_text = TITLE_FONT.render("Space Invaders", True, WHITE)
        title_text2 = SUB_TITLE_FONT.render("Press enter to continue", True, WHITE)

        # Enemy points
        point_text = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)

        # Drawing with positions
        SCREEN.blit(BACKGROUND, (0, 0))

        SCREEN.blit(title_text, (164, 155))
        SCREEN.blit(title_text2, (201, 225))

        SCREEN.blit(enemy1, (318, 270))
        SCREEN.blit(point_text, (368, 270))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        pygame.display.update()

def enemy():
    global enemy1

    enemy1_rect = enemy1.get_rect(topleft=(115, 250))
    # enemy1 = pygame.transform.scale(ENEMY1, (40, 40))

    for i in range(10):
        enemy1_rect.x += 50
        SCREEN.blit(enemy1, enemy1_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()


def main():
    global ship_rect, SHIP_SPEED, ENEMY1, enemy1

    pygame.key.set_repeat(1, 10)

    while True:
        CLOCK.tick(FPS)

        SCREEN.fill(BLACK)

        # Drawing with positions
        SCREEN.blit(BACKGROUND, (0, 0))

        # Lives
        lives_text = MAIN_FONT.render("Lives", True, WHITE)
        # Resize enemy1 next to lives
        enemy1 = pygame.transform.scale(ENEMY1, (25, 25))

        score_text = MAIN_FONT.render("Score", True, WHITE)
        score_text_num = MAIN_FONT.render("0", True, GREEN)

        # Drawing with positions
        SCREEN.blit(lives_text, (640, 5))
        SCREEN.blit(enemy1, (715, 3))
        SCREEN.blit(enemy1, (742, 3))
        SCREEN.blit(enemy1, (769, 3))

        SCREEN.blit(score_text, (5, 5))
        SCREEN.blit(score_text_num, (85, 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and ship_rect.x > 10:
                ship_rect.x -= SHIP_SPEED
            if keys[pygame.K_RIGHT] and ship_rect.x < 740:
                ship_rect.x += SHIP_SPEED

        SCREEN.blit(SHIP, ship_rect)

        enemy()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
