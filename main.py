import time, sys, pygame, math
pygame.init()
#test
test = True
#DISPLAY
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 1000
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
color = 255, 0, 0
clock = pygame.time.Clock()
#Game Vars
backroundx = 0
backroundy = 0
tempbackroundx = -300
tempbackroundy = 0
tempbackround = False
#Backround
backroundold = pygame.image.load('Assets/backround.png')
backround = pygame.transform.scale(backroundold, (1000, 1000))
#Run Loop
running = True
while running:
    if backroundx == -1000:
        backroundx = 0
        tempbackround = False
    if backroundx <= -300:
        tempbackround = True
        print('test')
    if tempbackround == False:
        pygame.Surface.blit(display, backround, (backroundx, backroundy))
        pygame.display.flip()
        backroundx = backroundx - 1
        time.sleep(0.01)
    