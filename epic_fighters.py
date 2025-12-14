import pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
import random
tutorialfont = pygame.font.SysFont(None,30)
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
class projectile(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height,xvelocity,lifetime,origin,damage):
        self.inittop = top
        self.initback = back
        self.initial_velocity = xvelocity
        self.projectile_lifespan = lifetime
        self.dammage = damage
        self.spawner = origin
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    
    exists = True
    
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
    def step(self):
        self.move_ip(self.initial_velocity,0)
        self.projectile_lifespan-=1
        if self.projectile_lifespan < 1:
            self.exists = False
        for aplayer in player_list:
            if not aplayer == self.spawner:
                if self.colliderect(aplayer):
                    deal_dammage(self.dammage,aplayer)
                    aplayer.xmom = self.initial_velocity
                    self.exists = False
class player(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height,type,keys):
        self.inittop = top
        self.initback = back
        self.player_type = type
        self.player_keybinds = keys
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    
    ymom = 0 
    xmom = 0
    health = 0
    armour = 0
    attack_moving_damage = 0
    time_till_attck = 0
    attack_type = 0
    lost_healt_per_miss = 5
    charge = 0
    charge_set = False
    beat_type = 0
    beat_count = 0
    beats = []
    beat_on = False
    transformed = 0
    insanity = 0
    depravity = 1
    heal_block = 0
    multiply = [1,0]
    stun = 0
    healing = [0,0]
    beat_shown = -1
    
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
def truant(stagnum,stagplay):
    i = 0
    while i < stagnum:
        i +=1
        beats.remove(stagplay.beats[i*2])
        stagplay.beats.remove(stagplay.beats[i*2])
def deal_dammage(ammount,target):
    if target.armour > 1:
        target.armour -= ammount * target.multiply[0]
    else:
        target.health -= ammount * target.multiply[0]

i = 0
player_select_iterator = 0
players = 2
selection = 0
dp = 0
selecting = 1
player1 = player(100,1808,64,128,None,[pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4])
player2 = player(100,1808,64,128,None,[pygame.K_z,pygame.K_x,pygame.K_c,pygame.K_v])
player3 = player(100,1808,64,128,None,[pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_0])
player4 = player(100,1808,64,128,None,[pygame.K_h,pygame.K_j,pygame.K_k,pygame.K_l])
player_list = [player1,player2,player3,player4]
player1_beat1 = beat((200, 0, 0), 150, 1)
player1_beat2 = beat((200, 0, 0), 200, 1)
player1_beat3 = beat((200, 0, 0), 300, 1)
player1_beat4 = beat((0, 200, 0), 400, 1)
player1_beat5 = beat((0, 0, 200), 430, 1)
player1_beat6 = beat((200, 0, 0), 490, 1)
player1_beat7 = beat((0, 0, 200), 550, 1)
player1_beat8 = beat((200, 0, 0), 600, 1)
player1_beat9 = beat((200, 0, 0), 630, 1)
player1_beat10 = beat((0, 200, 0), 670, 1)
player1_beat11 = beat((0, 0, 200), 700, 1)
player1_beat12 = beat((0, 200, 0), 800, 1)
player1_beat13 = beat((200, 0, 0), 870, 1)
player1_beat14 = beat((200, 0, 0), 910, 1)
player1_beat15 = beat((200, 0, 0), 960, 1)
player1_beat16 = beat((0, 200, 0), 1050, 1)
player1_beat17 = beat((0, 0, 200), 1090, 1)
player1_beat18 = beat((200, 0, 0), 1130, 1)
player1_beat19 = beat((0, 0, 200), 1190, 1)
player1_beat20 = beat((200, 0, 0), 1260, 1)
player1_beat21 = beat((200, 0, 0), 1300, 1)
player1_beat22 = beat((0, 200, 0), 1350, 1)
player1_beat23 = beat((0, 0, 200), 1410, 1)
player1_beat24 = beat((0, 200, 0), 1500, 1)
player2_beat1 = beat((200, 0, 0), 180, 2)
player2_beat2 = beat((0, 200, 0), 250, 2)
player2_beat3 = beat((200, 0, 0), 300, 2)
player2_beat4 = beat((0, 0, 200), 360, 2)
player2_beat5 = beat((200, 0, 0), 400, 2)
player2_beat6 = beat((0, 0, 200), 430, 2)
player2_beat7 = beat((200, 0, 0), 500, 2)
player2_beat8 = beat((0, 200, 0), 540, 2)
player2_beat9 = beat((200, 0, 0), 580, 2)
player2_beat10 = beat((200, 0, 0), 650, 2)
player2_beat11 = beat((0, 200, 0), 700, 2)
player2_beat12 = beat((0, 0, 200), 800, 2)
player2_beat13 = beat((200, 0, 0), 850, 2)
player2_beat14 = beat((0, 200, 0), 920, 2)
player2_beat15 = beat((200, 0, 0), 980, 2)
player2_beat16 = beat((0, 0, 200), 1040, 2)
player2_beat17 = beat((200, 0, 0), 1100, 2)
player2_beat18 = beat((0, 0, 200), 1150, 2)
player2_beat19 = beat((200, 0, 0), 1180, 2)
player2_beat20 = beat((0, 200, 0), 1250, 2)
player2_beat21 = beat((200, 0, 0), 1310, 2)
player2_beat22 = beat((200, 0, 0), 1350, 2)
player2_beat23 = beat((0, 200, 0), 1400, 2)
player2_beat24 = beat((0, 0, 200), 1500, 2)
beats = [player1_beat1,player1_beat2,player1_beat3,player1_beat4,player1_beat5,player1_beat6,player1_beat7,player1_beat8,player1_beat9,player1_beat10,player1_beat11,player1_beat12,player1_beat13,player1_beat14,player1_beat15,player1_beat16,player1_beat17,player1_beat18,player1_beat19,player1_beat20,player1_beat21,player1_beat22,player1_beat23,player1_beat24,player2_beat1,player2_beat2,player2_beat3,player2_beat4,player2_beat5,player2_beat6,player2_beat7,player2_beat8,player2_beat9,player2_beat10,player2_beat11,player2_beat12,player2_beat13,player2_beat14,player2_beat15,player2_beat16,player2_beat17,player2_beat18,player2_beat19,player2_beat20,player2_beat21,player2_beat22,player2_beat23,player2_beat24]
player1.beats = [player1_beat1,player1_beat2,player1_beat3,player1_beat4,player1_beat5,player1_beat6,player1_beat7,player1_beat8,player1_beat9,player1_beat10,player1_beat11,player1_beat12,player1_beat13,player1_beat14,player1_beat15,player1_beat16,player1_beat17,player1_beat18,player1_beat19,player1_beat20,player1_beat21,player1_beat22,player1_beat23,player1_beat24]
player2.beats = [player2_beat1,player2_beat2,player2_beat3,player2_beat4,player2_beat5,player2_beat6,player2_beat7,player2_beat8,player2_beat9,player2_beat10,player2_beat11,player2_beat12,player2_beat13,player2_beat14,player2_beat15,player2_beat16,player2_beat17,player2_beat18,player2_beat19,player2_beat20,player2_beat21,player2_beat22,player2_beat23,player2_beat24]
rems = []
projectiles = []

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
        text = bossfont.render('jekyll&hyde',True,(0,0,0),(200,200,200))
        screen.blit(text,(100,500))
        text = bossfont.render('greatest_showman',True,(0,0,0),(200,200,200))
        screen.blit(text,(100,600))
        if selecting == 1:
            text = bossfont.render('<odysseus>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,400))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 30
                player_list[player_select_iterator].player_type = 1
                player_list[player_select_iterator].health = 370
                player_select_iterator += 1
        if selecting == 2:
            text = bossfont.render('<jekyll&hyde>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,500))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 30
                player_list[player_select_iterator].player_type = 2
                player_list[player_select_iterator].health = 400
                player_select_iterator += 1
        if selecting == 3:
            text = bossfont.render('<greatest_showman>',True,(0,0,0),(200,200,200))
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
        if aplay.player_type == 2:
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
    for aplay in player_list:
        aplay.move_ip(aplay.xmom,aplay.ymom)
        if not aplay.attack_moving_damage == 0:
            for aplayer in player_list:
                if not aplayer == aplay:
                    if aplay.colliderect(aplayer):
                        aplayer.health -= aplay.attack_moving_damage
                        aplay.xmom *= -0.3
                        aplay.attack_moving_damage = 0
        if aplay.xmom < -0.2:
            aplay.xmom+=0.1
        elif aplay.xmom > 0.2:
            aplay.xmom-=0.1
        else:
            aplay.xmom = 0
            aplay.attack_moving_damage = 0
        if aplay.bottom < 1500:
            aplay.ymom+=0.2
        else:
            aplay.ymom = 0
            aplay.move(aplay.x,1500 - aplay.height)
    if player2.beat_on == True:
        print("good")
    for aproj in projectiles:
        pygame.draw.rect(screen, (0,0,0), aproj)
        if aproj.exists == False:
            rems.append(aproj)
        else:
            aproj.step()
    for arem in rems:
        projectiles.remove(arem)
    rems.clear()
    pygame.draw.rect(screen, (200,200,0),player1)
    pygame.draw.rect(screen, (0,200,200),player2)
    pygame.draw.rect(screen, (200,0,200),player3)
    pygame.draw.rect(screen, (200,200,200),player4)
    i = 1
    while i < (players+1):
        text = tutorialfont.render('player ' + str(i) + ' health: ' + str(player_list[i-1].health),True,(0,0,0),(255,255,255))
        screen.blit(text,(200,(60*i)-32))
        text = tutorialfont.render('player ' + str(i) + ' armour: ' + str(player_list[i-1].armour),True,(0,0,0),(255,255,255))
        screen.blit(text,(400,(60*i)-32))
        # if player_list[i-1].beat_on == True:
        text = tutorialfont.render(str(player_list[i-1].beat_type),True,(0,0,0),(255,255,255))
        screen.blit(text,(700,(60*i)-32))
        pygame.draw.line(screen, (0,0,0), (0,(60*i)), (3000,(60*i)), 4)
        if player_list[i-1].beat_shown < 0:
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
    for aplayer in player_list:
        aplayer.beat_count = 0
        i = 0
        for abeat in beats:
            if abeat in aplayer.beats:
                if abeat.point_in_song < 75 and abeat.point_in_song > 50:
                    if abeat.color == (200, 0, 0):
                        aplayer.beat_type = 1
                    elif abeat.color == (0, 0, 200):
                        aplayer.beat_type = 2
                    elif abeat.color == (0, 200, 0):
                        aplayer.beat_type = 3
                    elif abeat.color == (200, 200, 0):
                        aplayer.beat_type = 4
                    elif abeat.color == (200, 0, 200):
                        aplayer.beat_type = 5
                    elif abeat.color == (100, 0, 200):
                        aplayer.beat_type = 6
                    if abeat.rachet == True:
                        aplayer.beat_on = True
                        abeat.rachet = False
                        for aplayer in player_list:
                            aplayer.heal_block -= 1
                            aplayer.heal_block -= 1
                            aplayer.beat_shown -= 1
                            aplayer.multiply[1] -= 1
                            if aplayer.multiply[1] < 1:
                                aplayer.multiply[0] = 1
                            aplayer.healing[1] -= 1
                            aplayer.health += aplayer.healing[0]
                            if aplayer.healing[1] < 1:
                                aplayer.healing[0] = 0
                            if aplayer.charge_set == False:
                                aplayer.charge = 0
                            else:
                                aplayer.charge_set == False
                else:
                    aplayer.beat_count += 1
                    i += 1
        if not i < len(beats):
            aplayer.beat_on = False
            aplayer.beat_type = 0
    for aplayer in player_list:
        if aplayer.armour > 0:
            aplayer.armour -= 0.2
        elif aplayer.armour < 0:
            aplayer.armour = 0
    if aplayer.beat_count == len(aplayer.beats):
        aplayer.beat_type = 0
    for aplayer in player_list:
        if aplayer.stun < 1:
            for akey in aplayer.player_keybinds:
                if key[akey]:
                    if aplayer.beat_type == 0:
                        aplayer.health -= aplayer.lost_healt_per_miss
            if aplayer.beat_type == 5:
                i = 0
                for aplay in player_list:
                    if aplay.x < aplayer.x:
                        i-=1
                    else:
                        i+=1
                if i < 0:
                    aplayer.xmom = 8
                else:
                    aplayer.xmom = -8
            if aplayer.beat_type == 6:
                if random.randint(0,1) == 0:
                    aplayer.xmom = 8
                else:
                    aplayer.xmom = -8
                deal_dammage(5,aplayer)
                arrow = projectile(aplayer.centerx-100,aplayer.top-10,200,aplayer.height + 10,0,10,aplayer,30)
                projectiles.append(arrow)
            if aplayer.player_type == 1 and aplayer.beat_on == True:
                if key[aplayer.player_keybinds[0]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        for aplayer in player_list:
                            if aplayer.centerx < aplayer.centerx + 70 and aplayer.centerx > aplayer.centerx - 70 and aplayer.bottom < aplayer.bottom - 40:
                                aplayer.xmom *= -0.1
                                aplayer.attack_moving_damage = 0
                        arrow = projectile(aplayer.centerx-70,aplayer.centery,140,10,0,10,aplayer,10)
                        projectiles.append(arrow)
                    elif aplayer.beat_type == 2:
                        i = 0
                        for aplay in player_list:
                            if aplay.x < aplayer.x:
                                i-=1
                            else:
                                i+=1
                        if i > 0:
                            i = 1
                        else:
                            i = -1
                        arrow = projectile(aplayer.x,aplayer.centery,30,10,3*i,400,aplayer,10)
                        projectiles.append(arrow)
                    elif aplayer.beat_type == 3:
                        if aplayer.heal_block < 0:
                            aplayer.armour = 50
                elif key[aplayer.player_keybinds[1]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        i = 0
                        for aplay in player_list:
                            if aplay.x < aplayer.x:
                                i-=1
                            else:
                                i+=1
                        if i > 0:
                            aplayer.xmom = 9
                        else:
                            aplayer.xmom = -9
                        aplayer.attack_moving_damage = 10
                    elif aplayer.beat_type == 2:
                        if aplayer.charge == 0:
                            aplayer.charge = 1
                            aplayer.charge_set = True
                        elif aplayer.charge == 1:
                            i = 0
                            for aplay in player_list:
                                if aplay.x < aplayer.x:
                                    i-=1
                                else:
                                    i+=1
                            if i > 0:
                                aplayer.xmom = 7
                            else:
                                aplayer.xmom = -7
                            aplayer.attack_moving_damage = 30
                    elif aplayer.beat_type == 3:
                        for aplayer in player_list:
                            if aplayer.centerx < aplayer.centerx + 70 and aplayer.centerx > aplayer.centerx - 70 and aplayer.bottom < aplayer.bottom - 40:
                                if aplayer.centerx < aplayer.centerx:
                                    aplayer.xmom = -6
                                else:
                                    aplayer.xmom = 6
                        arrow = projectile(aplayer.centerx-70,aplayer.centery,140,10,0,10,aplayer,20)
                        projectiles.append(arrow)
                elif key[aplayer.player_keybinds[2]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        arrow = projectile(aplayer.centerx-80,aplayer.centery,160,10,0,10,aplayer,15)
                        projectiles.append(arrow)
                    elif aplayer.beat_type == 2:
                        i = 0
                        for aplay in player_list:
                            if aplay.x < aplayer.x:
                                i-=1
                            else:
                                i+=1
                        if i > 0:
                            aplayer.xmom = 12
                        else:
                            aplayer.xmom = -12
                        aplayer.ymom = -11
                        aplayer.attack_moving_damage = 10
                if key[aplayer.player_keybinds[3]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        for aplay in player_list:
                            if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                stagger(1,aplay)
                        arrow = projectile(aplayer.centerx-50,aplayer.centery,100,10,0,10,aplayer,10)
                        projectiles.append(arrow)
                    elif aplayer.beat_type == 3:
                        for aplay in player_list:
                            if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                aplay.lost_healt_per_miss += 5
                                stagger(3,aplay)
                        arrow = projectile(aplayer.centerx-50,aplayer.centery,100,10,0,10,aplayer,0)
                        projectiles.append(arrow)
            elif aplayer.player_type == 2 and aplayer.beat_on == True:
                aplayer.insanity += aplayer.depravity
                print("yum")
                if aplayer.insanity > 30:
                    aplayer.depravity+=1
                    for aplay in player_list:
                        if aplay.centerx < aplayer.centerx + 100 and aplay.centerx > aplayer.centerx - 100 and aplay.bottom < aplayer.bottom - 70:
                            if aplayer.transformed == 0:
                                aplayer.transformed = 1
                            else:
                                aplayer.transformed = 0
                    arrow = projectile(aplayer.centerx-100,aplayer.top-10,200,aplayer.height + 10,0,10,aplayer,30)
                    projectiles.append(arrow)
                elif key[aplayer.player_keybinds[0]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        if aplayer.transformed == 0:
                            if aplayer.heal_block < 0:
                                aplayer.health += 30
                            aplayer.beats[1].color = (200,0,200)
                        else:
                            for aplay in player_list:
                                if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                    aplay.heal_block = 5
                            arrow = projectile(aplayer.centerx-50,aplayer.top-10,100,aplayer.height + 10,0,10,aplayer,10)
                            projectiles.append(arrow)
                    elif aplayer.beat_type == 2:
                        if aplayer.transformed == 0:
                            for aplay in player_list:
                                if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                    truant(3,aplay)
                        else:
                            for aplay in player_list:
                                if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                    aplay.multiply = [2,3]
                    elif aplayer.beat_type == 3:
                        if aplayer.transformed == 0:
                            deal_dammage(aplayer.insanity,aplayer)
                            for aplay in player_list:
                                if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                    aplay.stun = aplayer.depravity
                            arrow = projectile(aplayer.centerx-50,aplayer.top-10,100,aplayer.height + 10,0,10,aplayer,aplayer.insanity*3)
                            projectiles.append(arrow)
                        else:
                            aplay.multiply = [1.1,2]
                            truant(2,aplay)
                elif key[aplayer.player_keybinds[1]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        i = 0
                        for aplay in player_list:
                            if aplay.x < aplayer.x:
                                i-=1
                            else:
                                i+=1
                        if i > 0:
                            aplayer.xmom = 8
                        else:
                            aplayer.xmom = -8
                        aplayer.attack_moving_damage = 10
                    elif aplayer.beat_type == 2:
                        if aplayer.transformed == 0:
                            aplayer.multiply = [-1,1]
                        else:
                            aplayer.beats[0].color = (100,0,200)
                            aplayer.beats[1].color = (100,0,200)
                            aplayer.beats[2].color = (100,0,200)
                    elif aplayer.beat_type == 3:
                        deal_dammage(aplayer.insanity,aplayer)
                        aplayer.healing = [2,aplayer.insanity]
                elif key[aplayer.player_keybinds[2]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        for aplay in player_list:
                            if not aplay == aplayer:
                                if aplayer.transformed == 0:
                                    deal_dammage(5,aplay)
                                else:
                                    stagger(1,aplay)
                    elif aplayer.beat_type == 2:
                        if aplayer.transformed == 0:
                            for aplay in player_list:
                                if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                    aplay.beat_shown = 3
                        else:
                            for aplay in player_list:
                                if aplay.centerx < aplayer.centerx + 70 and aplay.centerx > aplayer.centerx - 70 and aplay.bottom < aplayer.bottom - 40:
                                    stagger(2,aplay)
                            arrow = projectile(aplayer.centerx-70,aplayer.top-10,140,aplayer.height + 10,0,10,aplayer,10)
                            projectiles.append(arrow)
                    elif aplayer.beat_type == 3:
                        if aplayer.tranformed == 0:
                            aplayer.insanity -= 10
                            aplayer.health += 10
                        else:
                            deal_dammage(5,aplayer)
                            aplayer.insanity += 10
                if key[aplayer.player_keybinds[3]]:
                    if aplayer.beat_type == 1:
                        if aplayer.transformed == 0:
                            deal_dammage(5,aplayer)
                            aplayer.insanity += 10
                        else:
                            for aplayer in player_list:
                                if aplayer.centerx < aplayer.centerx + 80 and aplayer.centerx > aplayer.centerx - 80 and aplayer.bottom < aplayer.bottom - 40:
                                    deal_dammage(15,aplay)
                            arrow = projectile(aplayer.centerx-80,aplayer.top-10,160,aplayer.height + 10,0,10,aplayer,15)
                            projectiles.append(arrow)
                            i = 0
                            for aplay in player_list:
                                if aplay.x < aplayer.x:
                                    i-=1
                                else:
                                    i+=1
                            if i > 0:
                                aplayer.xmom = 7
                            else:
                                aplayer.xmom = -7
                    elif aplayer.beat_type == 2:
                        if aplayer.transformed == 0:
                            deal_dammage(15,aplayer)
                            aplayer.depravity += 1
                        else:
                            for aplayer in player_list:
                                if aplayer.centerx < aplayer.centerx + 80 and aplayer.centerx > aplayer.centerx - 80 and aplayer.bottom < aplayer.bottom - 40:
                                    aplay.health += 10
                                    aplay.stun = 3
                    elif aplayer.beat_type == 3:
                        aplayer.insanity += 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()