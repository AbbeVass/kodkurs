import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GREEN = (50, 200, 50)
RED = (200, 50, 50)

player = pygame.Rect(100, 300, 40, 50)
player_vel_y = 0
gravity = 0.5
jump_strength = -10
speed = 5
on_ground = False

platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(200, 450, 200, 20),
    pygame.Rect(500, 350, 200, 20)
]

# Spikar
spikes = [
    pygame.Rect(300, 530, 40, 20),
    pygame.Rect(350, 530, 40, 20),
    pygame.Rect(550, 330, 40, 20)
]

# Spawnpunkt
spawn_x, spawn_y = 100, 300

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_strength
        on_ground = False

    player_vel_y += gravity
    player.y += player_vel_y

    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if player_vel_y > 0:
                player.bottom = platform.top
                player_vel_y = 0
                on_ground = True

    # Kollision med spikar
    for spike in spikes:
        if player.colliderect(spike):
            # Resetta spelaren
            player.x = spawn_x
            player.y = spawn_y
            player_vel_y = 0

    # Rita plattformar
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Rita spikar
    for spike in spikes:
        pygame.draw.rect(screen, RED, spike)

    pygame.draw.rect(screen, BLUE, player)

    pygame.display.flip()
    clock.tick(60)