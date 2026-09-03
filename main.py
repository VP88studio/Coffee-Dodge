import time, sys, pygame, math, random, json
pygame.init()
pygame.font.init()

#test
testpillar = False
testpress = False
testscore = False
tesths = False
testsave = True
testfps = False
testpillary = True
testbuy = True
#DISPLAY
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 1000
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
color = 255, 0, 0
clock = pygame.time.Clock()
#loadingscreen
gamestatus = 4
if gamestatus == 4:
    loadingold = pygame.image.load('Assets/loading.png')
    loadingimg = pygame.transform.scale(loadingold, (750, 1000))
    display.blit(loadingimg, (-25,0))
    pygame.display.flip()
    time.sleep(1.5)
    gamestatus = 1
#Font
font = pygame.font.Font('Assets/font.ttf', 120)
mode_font = pygame.font.Font('Assets/font.ttf', 70)
money_font = pygame.font.Font('Assets/font.ttf', 50)
#Backround
backrounddetails = 'Assets/backround.png'
birddetails = 'Assets/bird.png'
pillardetails = 'Assets/pillar.png'
backroundold = pygame.image.load(backrounddetails)
backround = pygame.transform.scale(backroundold, (1049, 1499))
backroundflip = pygame.transform.rotate(backround, 180)
#Home Screen
homeold = pygame.image.load('Assets/home.png')
homeimg = pygame.transform.scale(homeold, (750, 1000))
#Shop
shopold = pygame.image.load('Assets/shop.png')
shopimg = pygame.transform.scale(shopold, (750, 1000))
equippedold = pygame.image.load('Assets/equipped.png')
equippedimg = pygame.transform.scale(equippedold, (160, 120))
equipold = pygame.image.load('Assets/equip.png')
equipimg = pygame.transform.scale(equipold, (160, 120))
moneyold = pygame.image.load('Assets/money.png')
moneyimg = pygame.transform.scale(moneyold, (60, 60))
milkbirdold = pygame.image.load('Assets/milkbird.png')
milkbirdimg = pygame.transform.scale(milkbirdold, (120, 80))
milkpillarold = pygame.image.load('Assets/milkpillar.png')
milkpillarimg = pygame.transform.scale(milkpillarold, (400, 600))
shopmilkpillarold = pygame.image.load('Assets/milkpillar.png')
shopmilkpillarimg = pygame.transform.scale(milkpillarold, (100, 150))
BLUE = 0,0,255
#Json Save File
defult_data = {
    'highscore': 0,
    'mode': 'Normal',
    'coffeebeans': 0,
    'item1': False,
    'item1equipped': False
}
def save(datasave):
    with open('Saves/saves.json', 'w') as file:
        json.dump(datasave, file, indent=4)
        if tesths:
            print('Save Successful')
try:
    with open('Saves/saves.json', 'r') as file:
        game_data = json.load(file)
        if testsave:
            print(game_data)
            print('Save Found')
            print(f"FoundData {game_data}")
except FileNotFoundError:
    game_data = defult_data
    if testsave:
        print('Save Not Found')
        print(f"NotFoundData {game_data}")
def movesave():
    defult_data['highscore'] = int(highscore['highscore'])
    defult_data['mode'] = modevar
    defult_data['coffeebeans'] = game_data['coffeebeans']
    defult_data['item1'] = game_data['item1']
    if tesths:
        print(f'HS: {int(highscore['highscore'])}')
        print(f"Big Boy HS: {defult_data['highscore']}")
        print(f'coffeebeans: {defult_data['coffeebeans']}')
    save(defult_data)
    pygame.quit()
    sys.exit()
#shop
shophome = {
    'x': 255,
    'y': 870,
    'width': 190,
    'height': 70
}
equip1 = {
    'x': 90,
    'y': 375,
    'width': 160,
    'height': 45
}
#home
startbutton = {
    'x': 180,
    'y': 350,
    'width': 340,
    'height': 100
}
easybutton = {
    'x': 200,
    'y': 475,
    'width': 300,
    'height': 60
}
normalbutton = {
    'x': 200,
    'y': 545,
    'width': 300,
    'height': 60
}
hardbutton = {
    'x': 200,
    'y': 620,
    'width': 300,
    'height': 60
}
shopbutton = {
    'x': 180,
    'y': 700,
    'width': 340,
    'height': 90
}
#GameOverScreen
gameoverold = pygame.image.load('Assets/gameover.png')
gameoverimg = pygame.transform.scale(gameoverold, (750, 1070))
restartbuttonold = pygame.image.load('Assets/restartbutton.png')
restartbuttonimg = pygame.transform.scale(restartbuttonold, (400, 300))
homebuttonold = pygame.image.load('Assets/homebutton.png')
homebuttonimg = pygame.transform.scale(homebuttonold, (400, 300))
restartbutton = {
    'x': 150,
    'y': 500,
    'width': 400,
    'hight': 300
}
homebutton = {
    'x': 150,
    'y': 700,
    'width': 400,
    'height': 300
}
#Pillar
pillarold = pygame.image.load(pillardetails)
pillar = pygame.transform.scale(pillarold, (400, 600))
pillarflip = pygame.transform.rotate(pillar, 180)
#bird
birdold = pygame.image.load(birddetails)
birdimg = pygame.transform.scale(birdold, (120, 80))
#Game Vars and Functions
gamecolor = 230, 115, 0
highscore = {
    "highscore": ''
}
WHITE = 255,255,255
score = 0
resetgame = False
gamestatus = 1
birdx = 290
bird_mask = pygame.mask.from_surface(birdimg)
pillar_mask = pygame.mask.from_surface(pillar)
pillarflip_mask = pygame.mask.from_surface(pillarflip)
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
    def draw(self):
        self.pillar1 = display.blit(pillarimgload, (pillar1x, first_pillary))
        self.pillar1flip = display.blit(pillarimgflipload, (pillar1x, first_pillary + 850))
        self.pillar2 = display.blit(pillarimgload, (pillar2x, second_pillary))
        self.pillar2flip = display.blit(pillarimgflipload, (pillar2x, second_pillary + 850))
        self.pillar3 = display.blit(pillarimgload, (pillar3x, third_pillary))
        self.pillar3flip = display.blit(pillarimgflipload, (pillar3x, third_pillary + 850))
pillaryplus = 40    
pillarload = pillarobj()
highscore['highscore'] = str(game_data['highscore'])
equip1img = equipimg
#gets width     of the backround image 
backround_width = backround.get_width()
#sets the backround x position
backroundx = 0
#sets the speed that it scrolls can be used to make harder gamemodes
scrollspeed = 2
first_pillary = random.randint(-280, -70)
second_pillary = random.randint(-280, -70)
third_pillary = random.randint(-280, -70)
def rollpillary():
    global first_pillary, second_pillary, third_pillary
    if scrollspeed == 4:
        first_pillary = random.randint(-280, -70)
        second_pillary = random.randint(first_pillary - pillaryplus, first_pillary + pillaryplus)
        third_pillary = random.randint(second_pillary - pillaryplus, second_pillary + pillaryplus)
    else:
        first_pillary = random.randint(-280, -70)
        second_pillary = random.randint(-280, -70)
        third_pillary = random.randint(-280, -70)
if game_data['mode'] == 'easy':
    scrollspeed = 1
if game_data['mode'] == 'normal':
    scrollspeed = 2
if game_data['mode'] == 'hard':
    scrollspeed = 4
pillary = -280
bird_hightspeed = 0
save(defult_data)
print(highscore['highscore'])

#gameimagesloading
pillarimgload = pillar
pillarimgflipload = pillarflip
birdimgload = birdimg

if testbuy:
    print(game_data['item1'])
#-70
#-280
#Run Loop
running = True
while running:
    if testfps:
        print(clock.get_fps())
    highscorex = 110
    #Equipped Items
    if game_data['item1equipped']:
        birdimgload = milkbirdimg
    if game_data['item1equipped'] == False:
        birdimgload = birdimg
    #Modes
    if scrollspeed == 1:
        mode = 'Mode: Easy'
        modevar = 'easy'
        modex = 155
    if scrollspeed == 2:
        mode = 'Mode: Normal'
        modevar = 'normal'
        modex = 100
    if scrollspeed == 4:
        mode = "Mode: Hard"
        modevar = 'hard'
        modex = 145
    mousepos = pygame.mouse.get_pos()
    if gamestatus == 0:
        #backround dont move
        display.blit(shopimg, (-25, -20))
        display.blit(milkbirdimg, (108, 228))
        if game_data['item1'] == True:
            display.blit(equip1img, (90, 340))
        display.blit(moneyimg, (5, 5))
        money_surface = money_font.render(str(game_data['coffeebeans']), True, gamecolor)
        display.blit(money_surface, (75, 2))
        shophome_rect = pygame.Rect((shophome['x'], shophome['y']), (shophome['width'], shophome['height']))
        equip1_rect = pygame.Rect((equip1['x'], equip1['y']), (equip1['width'], equip1['height']))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movesave()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_data['coffeebeans'] = int(game_data['coffeebeans']) + 9999999999999
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shophome_rect.collidepoint(mousepos):
                    gamestatus = 1
                if equip1_rect.collidepoint(mousepos):
                    if game_data['item1'] == False: 
                        if game_data['coffeebeans'] == 100 or game_data['coffeebeans'] >= 100:
                            game_data['coffeebeans'] = int(game_data['coffeebeans']) - 100
                            game_data['item1'] = True
                            item1equipvar = True
                            equip1img = equipimg
                            print(game_data['item1'])
                    if game_data['item1'] == True:
                        if item1equipvar:
                            equipimg = equipimg
                            item1equipvar = False
                        else:
                            if equip1img == equippedimg:
                                equip1img = equipimg
                                game_data['item1equipped'] = False
                            else:
                                equip1img = equippedimg
                                game_data['item1equipped'] = True
                print('click')
    if gamestatus == 1:
        if highscore['highscore'] == '':
            highscore['highscore'] = '0'
        #home backround DONT MOVE UNLESS U WANNA SPEND 3 HOURS DYING ON THE INSIDE
        display.blit(homeimg, (-25,0))
        mode_surface = mode_font.render(mode, True, gamecolor)
        hs_surface = mode_font.render(f'Highscore: {highscore['highscore']}', True, gamecolor)
        if int(highscore['highscore']) <= 10:
            highscorex = 110
        if int(highscore['highscore']) == 10 or int(highscore['highscore']) >= 10 and int(highscore['highscore']) <= 100:
            highscorex = 90
        if int(highscore['highscore']) == 100 or int(highscore['highscore']) >= 100 and int(highscore['highscore']) <= 1000:
            highscorex = 75
        display.blit(hs_surface, (highscorex, 820))
        display.blit(mode_surface, (modex, 10))
        shop_rect = pygame.Rect((shopbutton['x'], shopbutton['y']), (shopbutton['width'], shopbutton['height']))
        start_rect = pygame.Rect((startbutton['x'], startbutton['y']), (startbutton['width'], startbutton['height']))
        easy_rect = pygame.Rect((easybutton['x'], easybutton['y']), (easybutton['width'], easybutton['height']))
        normal_rect = pygame.Rect((normalbutton['x'], normalbutton['y']), (normalbutton['width'], normalbutton['height']))
        hard_rect = pygame.Rect((hardbutton['x'], hardbutton['y']), (hardbutton['width'], hardbutton['height']))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movesave()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(mousepos):
                    gamestatus = 3
                if shop_rect.collidepoint(mousepos):
                    gamestatus = 0
                if easy_rect.collidepoint(mousepos):
                    scrollspeed = 1
                if normal_rect.collidepoint(mousepos):
                    scrollspeed = 2
                if hard_rect.collidepoint(mousepos):
                    scrollspeed = 4
    if gamestatus == 2:
        if highscore['highscore'] == '':
            highscore['highscore'] = '0'
        if score >= int(highscore['highscore']):
            highscore['highscore'] = str(score)
            print(highscore['highscore'])
        restart_rect = pygame.Rect((restartbutton['x'], restartbutton['y']), (restartbutton['width'], restartbutton['hight']))
        home_rect = pygame.Rect((homebutton['x'], homebutton['y']), (homebutton['width'], homebutton['height']))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movesave()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(mousepos):
                    resetgame = True
                    gamestatus = 3
                if home_rect.collidepoint(mousepos):
                    resetgame = True
                    gamestatus = 1
        
        display.blit(gameoverimg, (-25, -35))
        display.blit(homebuttonimg, (homebutton['x'], homebutton['y']))
        display.blit(restartbuttonimg, (restartbutton['x'], restartbutton['y']))
        
    if gamestatus == 3:
        if resetgame:
            score = 0 
            birdy = 500
            pillar1x = 600
            pillar2x = 900
            pillar3x = 1200
            rollpillary()
            print(highscore['highscore'])
            resetgame = False
        keys = pygame.key.get_pressed()
        #check if events happening
        for event in pygame.event.get():
            if testpress:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gamestatus = 2
                    if event.key == pygame.K_s:
                        print('AdminScore')
                        score = score + 1
            #checking if player quit
            if event.type == pygame.QUIT:
                movesave()
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
        pillar3x -= scrollspeed
        if pillar1x == -260:
            pillar1x = 600
            if scrollspeed == 4:    
                first_pillary = random.randint(third_pillary - pillaryplus, third_pillary + pillaryplus)
                if testpillary:
                    print(first_pillary)
            first_pillary = random.randint(-280, -70)
        if pillar2x == -260:
            pillar2x = 600
            if scrollspeed == 4:
                second_pillary = random.randint(first_pillary - pillaryplus, first_pillary + pillaryplus)
                if testpillary:
                    print(second_pillary)
            second_pillary = random.randint(-280, -70)
        if pillar3x == -260:
            pillar3x = 600
            if scrollspeed == 4:
                third_pillary = random.randint(second_pillary - pillaryplus, second_pillary + pillaryplus)
                if testpillary:
                    print(third_pillary)
            third_pillary = random.randint(-280, 70)
        #collison detection
        pillar1_offsetx = (pillar1x - birdx)
        pillar2_offsetx = (pillar2x - birdx)
        pillar3_offsetx = (pillar3x - birdx)

        pillar1_offsety = (first_pillary - birdy)
        pillar2_offsety = (second_pillary - birdy)
        pillar3_offsety = (third_pillary - birdy)
        pillarflip1_offsety = ((first_pillary + 850) - birdy)
        pillarflip2_offsety = ((second_pillary + 850) - birdy)
        pillarflip3_offsety = ((third_pillary + 850) - birdy)
        pillar1_pos = (pillar1x, first_pillary)
        birdpos = (birdx, birdy)
        pillar1_offset = (pillar1_offsetx, pillar1_offsety)
        pillar2_offset = (pillar2_offsetx, pillar2_offsety)
        pillar3_offset = (pillar3_offsetx, pillar3_offsety)
        pillarflip1_offset = (pillar1_offsetx, pillarflip1_offsety)
        pillarflip2_offset = (pillar2_offsetx, pillarflip2_offsety)
        pillarflip3_offset = (pillar3_offsetx, pillarflip3_offsety)
        #score
        if birdx == pillar1x + 202:
            score += 1
            if testscore:
                print(score)
        if birdx == pillar2x + 202:
            score += 1
            if testscore:
                print(score)
        if birdx == pillar3x + 202:
            score += 1
            if testscore:
                print(score)
        #player die actions
        if bird_mask.overlap(pillar_mask, pillar1_offset) or bird_mask.overlap(pillar_mask, pillar2_offset) or bird_mask.overlap(pillar_mask, pillar3_offset):
            game_data['coffeebeans'] = int(game_data['coffeebeans']) + score
            if testpillar:
                print("top pillar touched")
            gamestatus = 2
        if bird_mask.overlap(pillarflip_mask, pillarflip1_offset) or bird_mask.overlap(pillarflip_mask, pillarflip2_offset) or bird_mask.overlap(pillarflip_mask, pillarflip3_offset):
            game_data['coffeebeans'] = int(game_data['coffeebeans']) + score
            if testpillar:
                print("bottom pillar touched")
            gamestatus = 2
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
        display.blit(birdimgload, (birdx, birdy))
        pillarload.draw()
        if testpillar == True:
            print(pillarload.xposlist, pillarx[0], pillarx[1], pillarx[2])
        #fontimage
        score_surface = font.render(str(score), True, (230, 115, 0))
        display.blit(score_surface, (300, 0))
    #reset screen
    pygame.display.update()
    clock.tick(60)