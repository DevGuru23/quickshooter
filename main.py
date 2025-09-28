import random
import sys
import pygame
from pygame.locals import *

#GLOBAL VARIABLE
FPS = 50
SCREENWIDTH = 800
SCREENHEIGHT = 626
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/knife closed.png'
BACKGROUND = 'gallery/sprites/background2.png'
PLAYERX = 70


def welcomeScreen():
    playery = 70
    welx = 0
    wely =  0

    while True:
        for event in pygame.event.get():
        #if user clicks or cross or space then what to happen
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type==KEYDOWN and (event.key==K_SPACE):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0,0))
                SCREEN.blit(GAME_SPRITES['knife'][0], (PLAYERX, playery))
                SCREEN.blit(GAME_SPRITES['welcome'], (welx, wely))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playery = 0
    SCREEN.fill("White")

    while True:  #game LOOP
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        
            if event.type == KEYDOWN:
                if(event.key == K_s or event.key == K_DOWN):
                   if (event.type != KEYUP):
                    score += 1
                    print(score)
                if(event.key == K_w or event.key == K_UP):
                   if (event.type != KEYUP):
                    score -= 1
                    print(score)
            else: pass

               
                    
        crashTest = isCollide(PLAYERX, playery)
        if crashTest:
            return
        
        #blitting
        SCREEN.blit(GAME_SPRITES['background'], (0,0))
        SCREEN.blit(GAME_SPRITES['scoreboard'], (0,0))
        SCREEN.blit(GAME_SPRITES['knife'][0], (PLAYERX,playery))
        
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        xoffset = SCREENWIDTH*0.75
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
            xoffset = SCREENWIDTH*0.5
            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (xoffset, SCREENHEIGHT*0.1))
                xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery):
    return False
   

if __name__ == "__main__":
    #main function
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('QuickShooter ~AyushGarg')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['welcome'] = pygame.image.load('gallery/sprites/wel.png').convert_alpha()
    GAME_SPRITES['scoreboard'] = pygame.image.load('gallery/sprites/wel.png').convert_alpha()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()

    GAME_SPRITES['knife'] = (pygame.image.load('gallery/sprites/knife closed.png').convert_alpha(),
        pygame.image.load('gallery/sprites/knife half open.png').convert_alpha(),
        pygame.image.load('gallery/sprites/knife full open.png').convert_alpha())
    GAME_SPRITES['zombie'] = pygame.image.load('gallery/sprites/zombie.png').convert_alpha()    
    GAME_SPRITES['pistol'] = pygame.image.load('gallery/sprites/pistol.png').convert_alpha()
    GAME_SPRITES['shotgun'] = pygame.image.load('gallery/sprites/shotgun.png').convert_alpha()
    GAME_SPRITES['ak47'] = pygame.image.load('gallery/sprites/ak47.png').convert_alpha()
    
       
    GAME_SOUNDS['knife hit'] = pygame.mixer.Sound('gallery/sounds/knife.wav')
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/sounds/die.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/sounds/point.wav')
    
    while True:
        welcomeScreen()
        mainGame()