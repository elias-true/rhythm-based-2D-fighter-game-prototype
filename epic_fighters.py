import pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
import random
tutorialfont = pygame.font.SysFont(None,40)
bossfont = pygame.font.SysFont(None,70)
titlefont = pygame.font.SysFont(None,150)
run = True
screen = pygame.display.set_mode((3000,1500))
player1_beat_type = 0
player1_beat_count = 0
class beat():
    def __init__(self, color, point_in_song, player):
        self.color = color
        self.point_in_song = point_in_song
        self.player = player
        pass
    rachet = True
class player(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height,type):
        self.inittop = top
        self.initback = back
        self.player_type = type
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    
    ymom = 0 
    xmom = 0
    health = 0
    attack_moving_damage = 0
    time_till_attck = 0
    attack_type = 0
    
    def move_ip(self,deltaX:float,deltaY:float):
        self.tx = self.tx+deltaX
        self.ty = self.ty+deltaY
        selfAsRect = super()
        selfAsRect.move_ip(round(self.tx)-selfAsRect.x,round(self.ty)-selfAsRect.y)
#d        print("moved to "+str(self.tx)+","+str(self.ty))

    def move(self,X:float,Y:float):
        self.tx = X
        self.ty = Y
        selfAsRect = super()
        selfAsRect.move(round(X),round(Y))

    def resetInitialPosition(self):
        self.tx = self.initback
        self.ty = self.inittop
        self.move(self.tx,self.ty)

def stagger(stagnum,stagplay):
    i = 0
    while i < stagnum:
        if beats[i].player == stagplay:
            beats[i].point_in_song += random.randint(-10,10)
i = 0
player_select_iterator = 0
players = 2
selection = 0
dp = 0
selecting = 1
beat_on = False
player1 = player(100,1808,64,192,None)
player2 = player(100,1808,64,192,None)
player3 = player(100,1808,64,192,None)
player4 = player(100,1808,64,192,None)
player_list = [player1,player2,player3,player4]
player1_beat1 = beat((200, 0, 0), 150, 1)
player1_beat2 = beat((200, 0, 0), 200, 1)
player1_beat3 = beat((200, 0, 0), 300, 1)
player1_beat4 = beat((0, 200, 0), 400, 1)
player1_beat5 = beat((0, 0, 200), 430, 1)
player1_beat6 = beat((200, 200, 0), 490, 1)
player2_beat1 = beat((200, 0, 0), 180, 2)
player2_beat2 = beat((0, 200, 0), 250, 2)
player2_beat3 = beat((200, 0, 0), 300, 2)
player2_beat4 = beat((200, 0, 0), 360, 2)
player2_beat5 = beat((200, 0, 0), 400, 2)
player2_beat6 = beat((0, 0, 200), 430, 2)
beats = [player1_beat1,player1_beat2,player1_beat3,player1_beat4,player1_beat5,player1_beat6,player2_beat1,player2_beat2,player2_beat3,player2_beat4,player2_beat5,player2_beat6]
rems = []

while selection < 2:
    key = pygame.key.get_pressed()
    screen.fill((255,255,255))
    if selection == 0:
        text = titlefont.render('players',True,(0,0,0),(200,200,200))
        screen.blit(text,(50,0))
        text = bossfont.render('2',True,(0,0,0),(200,200,200))
        screen.blit(text,(100,400))
        text = bossfont.render('3',True,(0,0,0),(200,200,200))
        screen.blit(text,(100,500))
        text = bossfont.render('4',True,(0,0,0),(200,200,200))
        screen.blit(text,(100,600))
        if selecting == 1:
            text = bossfont.render('<2>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,400))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 30
                players = 2
                selection = 1
        if selecting == 2:
            text = bossfont.render('<3>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,500))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 30
                players = 3
                selection = 1
        if selecting == 3:
            text = bossfont.render('<4>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,600))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 30
                players = 4
                selection = 1
    elif selection == 1:
        text = titlefont.render('player ' + str(player_select_iterator+1) + ' character selection',True,(0,0,0),(200,200,200))
        screen.blit(text,(50,0))
        text = bossfont.render('odysseus',True,(0,0,0),(200,200,200))
        screen.blit(text,(100,400))
        text = bossfont.render('poseidon',True,(0,0,0),(200,200,200))
        screen.blit(text,(100,500))
        text = bossfont.render('circe',True,(0,0,0),(200,200,200))
        screen.blit(text,(100,600))
        if selecting == 1:
            text = bossfont.render('<odysseus>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,400))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 30
                player_list[player_select_iterator].player_type = 1
                player_list[player_select_iterator].health = 350
                player_select_iterator += 1
        if selecting == 2:
            text = bossfont.render('<poseidon>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,500))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 30
                player_list[player_select_iterator].player_type = 2
                player_list[player_select_iterator].health = 400
                player_select_iterator += 1
        if selecting == 3:
            text = bossfont.render('<circe>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,600))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 30
                player_list[player_select_iterator].player_type = 3
                player_list[player_select_iterator].health = 300
                player_select_iterator += 1
        if (player_select_iterator+1) > players:
            selection = 2
    if key[pygame.K_DOWN] == True and dp < 1:
        selecting+=1
        if selecting>3:
            selecting = 1
        dp = 30
    elif key[pygame.K_UP] == True and dp < 1:
        selecting-=1
        if selecting<1:
            selecting = 3
        dp = 30
    else:
        dp-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            selection = 3
    pygame.display.update()


for aplay in player_list:
    if not aplay.player_type == None:
        if aplay.player_type == 1:
            aplay.bottom = 1500
            aplay.height = 128
        elif aplay.player_type == 3:
            aplay.bottom = 1500
            aplay.height = 96
            aplay.width = 32
    else:
        rems.append(aplay)
for arem in rems:
    player_list.remove(arem)
rems.clear()
i = 0
while i < len(player_list):
    player_list[i].move((i*800)+100,1500-player_list[i].height)
    i += 1



while run == True:
    beats.sort(key=lambda beat: beat.point_in_song)
    key = pygame.key.get_pressed()
    screen.fill((255,255,255))
    for aplay in players:
        aplay.move_ip(aplay.xmom,0)
        if not aplay.attack_moving_damage == 0:
            for aplayer in players:
                if not aplayer == aplay:
                    if aplay.colliderect(aplayer):
                        aplayer.health -= aplay.attack_moving_dammage
        if aplay.xmom < 0.2:
            aplay.xmom+=0.1
        elif aplay.xmom > 0.2:
            aplay.xmom-=0.1
        else:
            aplay.xmom = 0
            aplay.attack_moving_damage = 0
    pygame.draw.rect(screen, (200,200,0),player1)
    pygame.draw.rect(screen, (0,200,200),player2)
    pygame.draw.rect(screen, (200,0,200),player3)
    pygame.draw.rect(screen, (200,200,200),player4)
    i = 1
    while i < (players+1):
        pygame.draw.line(screen, (0,0,0), (0,(60*i)), (3000,(60*i)), 4)
        pygame.draw.line(screen, (0,0,0), (50,((60*i)-25)), (50,((60*i)+25)), 4)
        pygame.draw.line(screen, (0,0,0), (75,((60*i)-25)), (75,((60*i)+25)), 4)
        i+=1
    for abeat in beats:
        pygame.draw.circle(screen, abeat.color, (abeat.point_in_song, (abeat.player * 60)), 12)
        abeat.point_in_song -= 1
        if abeat.point_in_song < 30:
            rems.append(abeat)
    for arem in rems:
        beats.remove(arem)
    rems.clear()
    player1_beat_count = 0
    for abeat in beats:
            if abeat.point_in_song < 75 and abeat.point_in_song > 50:
                if abeat.color == (200, 0, 0):
                    player1_beat_type = 1
                elif abeat.color == (0, 200, 0):
                    player1_beat_type = 2
                elif abeat.color == (0, 0, 200):
                    player1_beat_type = 3
                elif abeat.color == (200, 200, 0):
                    player1_beat_type = 4
                if abeat.rachet == True:
                    beat_on = True
                    abeat.rachet = False
            else:
                player1_beat_count += 1
    if player1_beat_count == len(beats):
        player1_beat_type = 0
    if key[pygame.K_1]:
        beat_on = False
        if player1_beat_type == 0:
            player1.health -= 5
        elif player1_beat_type == 1:
            for aplayer in players:
                if aplayer.centerx < player1.centerx + 70 and aplayer.centerx > player1.centerx - 70 and aplayer.centery < player1.centery + 40 and aplayer.centerx > player1.centerx - 40:
                    aplayer.health-=10
                    aplayer.xmom = 0
                    aplayer.time_till_attack = 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()