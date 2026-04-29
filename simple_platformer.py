import pygame
import sys

# Initierar pygame
pygame.init()

# Skärmen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")

clock = pygame.time.Clock()

# Färger
WHITE = (255,255,255)
BLUE = (50,150,255)
GREEN = (50,200,50)

# Spelaren
player = pygame.Rect(100, 300, 40, 50)
player_vel_y = 0
gravity = 0.5
jump_strength = -10
speed = 5
on_ground = False
spelar_bild = pygame.image.load("")
spelar_bild = spelar_bild.convert_alpha()
spelar_bild = pygame.transform.scale(spelar_bild,(40,50))


# Plattformar
platforms = [
    pygame.Rect(0,550,800,50),
    pygame.Rect(200,450,200,20),
    pygame.Rect(500,350,200,20)
]

# Game loop
while True:
    screen.fill(WHITE)

    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_strength
        on_ground = False

    # Gravitation
    player_vel_y += gravity
    player.y += player_vel_y

    # Kollision
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if player_vel_y > 0:
                player.bottom = platform.top
                player_vel_y = 0
                on_ground = True

    # Rita plattformar
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Rita spelaren
    #pygame.draw.rect(screen, BLUE, player)
    screen.blit(spelar_bild, (player.x,player.y))

    pygame.display.flip()
    clock.tick(60)
