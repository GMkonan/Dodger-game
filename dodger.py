import pygame
import random
import math
from settings import Settings

pygame.init()
settings = Settings()

screen = pygame.display.set_mode((800,600))
player_image = pygame.image.load("fique-em-casa.png")
background = pygame.image.load("background.jpg")


font = pygame.font.Font('freesansbold.ttf',32)

for i in range (settings.num_of_enemies):
    settings.enemyimg.append(pygame.image.load("medico.png"))
    settings.enemyx.append(random.randint(0,770))
    settings.enemyy.append(random.randint(-300,0))
    settings.enemyy_change.append(0.9)

#functions
def player(x,y):
    screen.blit(player_image,(x,y))

def enemy(x,y,i):
    screen.blit(settings.enemyimg[i], (x,y))

def isCollision(enemyx,enemyy,playerx,playery):
    distance = math.sqrt((math.pow(enemyx-playerx,2)) + (math.pow(enemyy-playery,2)))
    if distance < 42:
        return True
    else:
        return False

def show_life(x, y):
    lifef = font.render("Life: " + str(settings.life), True, (255, 255, 255))
    screen.blit(lifef, (x, y))

def show_score(x, y):
    scorer = font.render("Score: " + str(settings.score), True, (255, 255, 255))
    screen.blit(scorer, (x, y))

def game_stop(x,y):
    settings.playerx_change = 0
    settings.playery_change = 0
    settings.enemyy_change = 0
    pausa = font.render("Paused", True, (255, 255, 255))
    screen.blit(pausa, (x, y))

running = True
while running:

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                settings.playery_change = -1
            if event.key == pygame.K_DOWN:
                settings.playery_change = 1
            if event.key == pygame.K_LEFT:
                settings.playerx_change = -1
            if event.key == pygame.K_RIGHT:
                settings.playerx_change = 1


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                settings.playerx_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                settings.playery_change = 0

    settings.playerx += settings.playerx_change
    settings.playery += settings.playery_change

    #verifica que o player n vai sair da tela no eixo X
    if settings.playerx <= 0:
        settings.playerx = 0
    elif settings.playerx >= 770:
        settings.playerx = 770

    if settings.playery <= 0:
        settings.playery = 0
    elif settings.playery >= 570:
        settings.playery = 570

    for i in range (settings.num_of_enemies):
        settings.enemyy[i] += settings.enemyy_change[i]

        collision = isCollision(settings.enemyx[i],settings.enemyy[i],settings.playerx,settings.playery)
        if collision:
            print(settings.life)
            settings.life -= settings.damage
            if settings.life <= 0:
                running = False
                print(settings.life)
            settings.enemyx[i] = random.randint(0,770)
            settings.enemyy[i] = random.randint(-300,0)
        enemy(settings.enemyx[i],settings.enemyy[i],i)

        if settings.enemyy[i] > 500:
            settings.score += 20
            settings.enemyx[i] = random.randint(0,770)
            settings.enemyy[i] = random.randint(-300,0)

    show_score(130,5)
    show_life(20,5)
    player(settings.playerx,settings.playery)
    pygame.display.update()
