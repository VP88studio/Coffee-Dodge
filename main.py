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
#Backround
backroundold = pygame.image.load('Assets/backround.png')
backround = pygame.transform.scale(backroundold, (1254, 1254))
#Game Vars and Functions
#gets width of the backround image 
backround_width = backround.get_width()
#sets the backround x position
backroundx = 0
#sets the speed that it scrolls can be used to make harder gamemodes
scrollspeed = 2


#Run Loop
running = True
while running:
    #check if events happening
    for event in pygame.event.get():
        #checking if player quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #makes backroundx = to backroundx - scrollspeed so every time it loops it it is equal to itself - scroll speed to make it move
    backroundx -= scrollspeed   
    #this means that if backround_width is more than or equal to backroundx it sets backroundx to 0
    if backroundx <= -backround_width:
        backroundx = 0
    #this displays the backround images
    display.blit(backround, (backroundx, 0))
    #this displays the second image by making the x position backroundx + the width of the first backround
    #idk how i didnt think of this in the 3 days i spent on this problem
    display.blit(backround, (backroundx + backround_width, 0))
    pygame.display.update()
    clock.tick(60)