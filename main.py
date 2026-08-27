import time, sys, pygame, math, random, asyncio
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
backround = pygame.transform.scale(backroundold, (1049, 1499))
backroundflip = pygame.transform.rotate(backround, 180)
#Pillar
pillarold = pygame.image.load('Assets/pillar.png')
pillar = pygame.transform.scale(pillarold, (400, 600))
pillarflip = pygame.transform.rotate(pillar, 180)
#bird
birdold = pygame.image.load('Assets/bird.png')
birdimg = pygame.transform.scale(birdold, (120, 80))
#birdwidth 1536
#birdheight 1024
#3:2 ratio
#Game Vars and Functions
keys = pygame.key.get_pressed()
birdy = 460
def pillaryfinder():
    global first_pillary, second_pillary, third_pillary
    #every 209.8
    first_pillary = random.randint(-280, -70)
    second_pillary = random.randint(-280, -70)
    third_pillary = random.randint(-280, 70)
pillaryfinder()
class pillarobj:
    def __init__(self):
        self.xpos = backroundx + 808
        if backroundx + 808 == -240:
            self.xpos = backroundx - 200
        if backroundx == 0:
            pillaryfinder()
        self.pillary = first_pillary
        self.img  = pillar
        self.imgflip = pillarflip
        self.pillar1 = display.blit(self.img, (self.xpos, self.pillary))
        self.pillar1flip = display.blit(self.imgflip, (self.xpos, self.pillary + 850))
#gets width of the backround image 
backround_width = backround.get_width()
#sets the backround x position
backroundx = 0
#sets the speed that it scrolls can be used to make harder gamemodes
scrollspeed = 2
pillary = -280
bird_hightspeed = 0
#-70
#-280
#Run Loop
running = True
while running:
    keys = pygame.key.get_pressed()
    #check if events happening
    for event in pygame.event.get():

        #checking if player quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_hightspeed = -5
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bird_hightspeed = -5
    if birdy < 0:
        birdy = 0
        bird_hightspeed = 0
    if birdy > 920:
        birdy = 919
        bird_hightspeed = 0
    bird_hightspeed += (0.125)
    birdy += bird_hightspeed
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
    display.blit(birdimg, (290, birdy))
    pillarimgthingy = pillarobj()
    pillarimgthingy.pillar1
    pygame.display.update()
    clock.tick(60)