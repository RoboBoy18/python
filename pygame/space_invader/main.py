import math
import random
import pygame
from pygame import mixer

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Background sound
pygame.mixer.music.load('back.wav')
pygame.mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption('Pygame')
icon = pygame.image.load('vr-gaming.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('space-invaders.png')
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(3.5)
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 8
bullet_state = 'Ready'

# Score
score = 0
font = pygame.font.Font('arcadeclassic.regular.ttf', 32)
text_x = 10
text_y = 10

# Game over
over_font = pygame.font.Font('arcadeclassic.regular.ttf', 70)


def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (250, 250))


def show_score(x, y):
    score_value = font.render("Score " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'Fire'
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


clock = pygame.time.Clock()
fps = 60
# Game loop
running = True
while running:
    clock.tick(fps)
    screen.fill((153, 209, 255))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -4
            if event.key == pygame.K_RIGHT:
                player_x_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state is 'Ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Checking the boundaries
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    for i in range(num_of_enemies):
        # Game over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 3.5
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -3.5
            enemy_y[i] += enemy_y_change[i]

        # Collision
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_sound = mixer.Sound('explosion.wav')
            bullet_sound.play()
            bullet_y = 480
            bullet_state = 'Ready'
            score += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = 'Ready'
    if bullet_state is 'Fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
