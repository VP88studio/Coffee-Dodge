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
first_pillary = random.randint(-280, -70)
second_pillary = random.randint(-280, -70)
third_pillary = random.randint(-280, -70)
keys = pygame.key.get_pressed()
birdy = 460
pillarx = []
pillar1x = 600
pillar2x = 900
pillar3x = 1200
pillarx.append(pillar1x)
pillarx.append(pillar2x)
pillarx.append(pillar3x)
def pillarxlistmaker():
    pillarx[0] = pillar1x
    pillarx[1] = pillar2x
    pillarx[2] = pillar3x
pillarxlistmaker()
class pillarobj:
    def __init__(self):
        self.pillarylist = []
        self.xposlist = []
        self.xposlist.append(pillarx[0])
        self.xposlist.append(pillarx[1])
        self.xposlist.append(pillarx[2])
        self.pillarylist.append(first_pillary)
        self.pillarylist.append(second_pillary)
        self.pillarylist.append(third_pillary)
        self.img  = pillar
        self.imgflip = pillarflip
        self.pillar1 = display.blit(self.img, (self.xposlist[0], self.pillarylist[0]))
        self.pillar1flip = display.blit(self.imgflip, (self.xposlist[0], self.pillarylist[0] + 850))
        self.pillar2 = display.blit(self.img, (self.xposlist[1], self.pillarylist[1]))
        self.pillar2flip = display.blit(self.imgflip, (self.xposlist[1], self.pillarylist[1] + 850))
        self.pillar3 = display.blit(self.img, (self.xposlist[2], self.pillarylist[2]))
        self.pillar3flip = display.blit(self.imgflip, (self.xposlist[2], self.pillarylist[2] + 850))
        
#gets width     of the backround image 
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
    #pillar move loop
    pillarxlistmaker()
    pillar1x -= scrollspeed
    pillar2x -= scrollspeed
    if pillar1x == -260:
        pillar1x = 600
        first_pillary = random.randint(-280, -70)
    if pillar2x == -260:
        pillar2x = 600
        second_pillary = random.randint(-280, -70)
    third_pillary = random.randint(-280, 70)
    
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
    pillarload = pillarobj()
    pillarload.pillar1
    pillarload.pillar2
    pillarload.pillar3
    print(pillarload.xposlist, pillarx[0], pillarx[1])
    pygame.display.update()
    clock.tick(60)