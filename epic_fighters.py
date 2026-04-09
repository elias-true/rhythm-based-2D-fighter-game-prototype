import pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
import random
import time as timekeep
tutorialfont = pygame.font.SysFont(None,30)
bossfont = pygame.font.SysFont(None,70)
titlefont = pygame.font.SysFont(None,150)
run = True
screen = pygame.display.set_mode((1540,790))
player1_beat_type = 0
player1_beat_count = 0
beat_ind_vel = 0
beat_ind_vel_player2 = 0

current_time = 1
last_second_time = timekeep.time()
tick_multiplier_debug = 1
ticks = 1
timestep = False
ticks1 = 1
tps = 1
last_second_time1 = 1
numberkey = 0



class movable(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height):
        self.inittop = top
        self.initback = back
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    
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
class beat():
    def __init__(self, color, point_in_song, player):
        self.color = color
        self.point_in_song = point_in_song
        self.player = player
        pass
    rachet = True
class projectile(movable):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height,xvelocity,yvelocity,lifetime,origin,damage):
        self.inittop = top
        self.initback = back
        self.initial_xvelocity = xvelocity
        self.initial_yvelocity = yvelocity
        self.projectile_lifespan = lifetime
        self.dammage = damage
        self.spawner = origin
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    
    exists = True
    passind = False
    
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
        self.move_ip(self.initial_velocity*tick_multiplier_debug,0)
        self.projectile_lifespan-=1
        if self.projectile_lifespan < 1:
            self.exists = False
        for aplayer in hitables:
            if not (aplayer == self.spawner or (aplayer in summons and aplayer.origin == self.spawner)):
                # self.passind = False
                # if aplayer
                if self.colliderect(aplayer):
                    deal_dammage(self.dammage,aplayer)
                    aplayer.xmom = self.initial_velocity
                    self.exists = False
class player(movable):
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
    toxin = 0
    multiply = [1,0]
    stun = 0
    healing = [0,0]
    beat_shown = -1
    beat_ind = False
    last_key_pressed = None
    
    # def move_ip(self,deltaX:float,deltaY:float):
#         self.tx = self.tx+deltaX
#         self.ty = self.ty+deltaY
#         selfAsRect = super()
#         selfAsRect.move_ip(round(self.tx)-selfAsRect.x,round(self.ty)-selfAsRect.y)
# #d        print("moved to "+str(self.tx)+","+str(self.ty))

#     def move(self,X:float,Y:float):
#         self.tx = X
#         self.ty = Y
#         selfAsRect = super()
#         selfAsRect.move(round(X),round(Y))

#     def resetInitialPosition(self):
#         self.tx = self.initback
#         self.ty = self.inittop
#         self.move(self.tx,self.ty)

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

class summon(movable):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height,health,damage,time_between_hits,ranged,attack_duration,origin):
        self.inittop = top
        self.initback = back
        self.health = health
        self.damage = damage
        self.time_between_hits = time_between_hits
        self.ranged = ranged
        self.attack_duration = attack_duration
        self.origin = origin
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    abylity_type = 0
    armour = 0
    cooldown = 0

i = 0
player_select_iterator = 0
players = 2
selection = -1
dp = 0
selecting = 1
titlewordsize = 70
titlewordsizechangespeed = 0
title_word_color = (0,0,0)
title_word_color_randomizer = 0
beatspassedplayer1 = 0
player1 = player(100,1808,64,128,None,[pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4])
player2 = player(100,1808,64,128,None,[pygame.K_z,pygame.K_x,pygame.K_c,pygame.K_v])
player3 = player(100,1808,64,128,None,[pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_0])
player4 = player(100,1808,64,128,None,[pygame.K_h,pygame.K_j,pygame.K_k,pygame.K_l])
player_list = [player1,player2,player3,player4]
beat_indicator_bottom = movable(0,785,1550,5)
beat_indicator_top = movable(0,0,1550,5)
beat_indicator_left = movable(0,0,5,800)
beat_indicator_right = movable(1535,0,5,1500)
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
player1_beat25 = beat((200, 0, 0), 1560, 1)
player1_beat26 = beat((200, 0, 0), 1620, 1)
player1_beat27 = beat((200, 0, 0), 1700, 1)
player1_beat28 = beat((0, 200, 0), 1770, 1)
player1_beat29 = beat((0, 0, 200), 1890, 1)
player1_beat30 = beat((200, 0, 0), 1940, 1)
player1_beat31 = beat((0, 0, 200), 2000, 1)
player1_beat32 = beat((200, 0, 0), 2080, 1)
player1_beat33 = beat((200, 0, 0), 2130, 1)
player1_beat34 = beat((0, 200, 0), 2200, 1)
player1_beat35 = beat((0, 0, 200), 2260, 1)
player1_beat36 = beat((0, 200, 0), 2310, 1)
player1_beat37 = beat((200, 0, 0), 2360, 1)
player1_beat38 = beat((200, 0, 0), 2440, 1)
player1_beat39 = beat((200, 0, 0), 2530, 1)
player1_beat40 = beat((0, 200, 0), 2590, 1)
player1_beat41 = beat((0, 0, 200), 2670, 1)
player1_beat42 = beat((200, 0, 0), 2720, 1)
player1_beat43 = beat((0, 0, 200), 2790, 1)
player1_beat44 = beat((200, 0, 0), 2850, 1)
player1_beat45 = beat((200, 0, 0), 2910, 1)
player1_beat46 = beat((0, 200, 0), 2950, 1)
player1_beat47 = beat((0, 0, 200), 3010, 1)
player1_beat48 = beat((200, 0, 0), 3090, 1)
player1_beat49 = beat((200, 0, 0), 3150, 1)
player1_beat50 = beat((200, 0, 0), 3200, 1)
player1_beat51 = beat((200, 0, 0), 3240, 1)
player1_beat52 = beat((0, 0, 200), 3310, 1)
player1_beat53 = beat((200, 0, 0), 3390, 1)
player1_beat54 = beat((200, 0, 0), 3460, 1)
player1_beat55 = beat((0, 0, 200), 3540, 1)
player1_beat56 = beat((0, 200, 0), 3610, 1)
player1_beat57 = beat((200, 0, 0), 3690, 1)
player1_beat58 = beat((200, 0, 0), 3740, 1)
player1_beat59 = beat((200, 0, 0), 3800, 1)
player1_beat60 = beat((0, 200, 0), 3880, 1)
player1_beat61 = beat((200, 0, 0), 3950, 1)
player1_beat62 = beat((200, 0, 0), 4030, 1)
player1_beat63 = beat((200, 0, 0), 4080, 1)
player1_beat64 = beat((0, 200, 0), 4140, 1)
player1_beat65 = beat((200, 0, 0), 4200, 1)
player1_beat66 = beat((200, 0, 0), 4250, 1)
player1_beat67 = beat((200, 0, 0), 4340, 1)
player1_beat68 = beat((0, 200, 0), 4410, 1)
player1_beat69 = beat((200, 0, 0), 4500, 1)
player1_beat70 = beat((0, 200, 0), 4580, 1)
player1_beat71 = beat((0, 0, 200), 4650, 1)
player1_beat72 = beat((200, 0, 0), 4740, 1)
player1_beat73 = beat((0, 0, 200), 4780, 1)
player1_beat74 = beat((0, 200, 0), 4810, 1)
player1_beat75 = beat((200, 0, 0), 4860, 1)
player1_beat76 = beat((200, 0, 0), 4900, 1)
player1_beat77 = beat((200, 0, 0), 4940, 1)
player1_beat78 = beat((200, 0, 0), 4990, 1)
player1_beat79 = beat((200, 0, 0), 5020, 1)
player1_beat80 = beat((0, 200, 0), 5060, 1)
player1_beat81 = beat((0, 0, 200), 5090, 1)
player1_beat82 = beat((200, 0, 0), 5130, 1)
player1_beat83 = beat((0, 200, 0), 5190, 1)
player1_beat84 = beat((0, 200, 0), 5280, 1)
player1_beat85 = beat((200, 0, 0), 5320, 1)
player1_beat86 = beat((0, 0, 200), 5410, 1)
player1_beat87 = beat((200, 0, 0), 5450, 1)
player1_beat88 = beat((200, 0, 0), 5540, 1)
player1_beat89 = beat((0, 0, 200), 5600, 1)
player1_beat90 = beat((0, 0, 200), 5670, 1)
player1_beat91 = beat((200, 0, 0), 5710, 1)
player1_beat92 = beat((200, 0, 0), 5770, 1)
player1_beat93 = beat((200, 0, 0), 5830, 1)
player1_beat94 = beat((200, 0, 0), 5900, 1)
player1_beat95 = beat((200, 0, 0), 5990, 1)
player1_beat96 = beat((0, 200, 0), 6030, 1)
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
player2_beat25 = beat((200, 0, 0), 1550, 2)
player2_beat26 = beat((0, 200, 0), 1610, 2)
player2_beat27 = beat((0, 200, 0), 1710, 2)
player2_beat28 = beat((0, 200, 0), 1780, 2)
player2_beat29 = beat((200, 0, 0), 1880, 2)
player2_beat30 = beat((0, 200, 0), 1950, 2)
player2_beat31 = beat((200, 0, 0), 2010, 2)
player2_beat32 = beat((200, 0, 0), 2080, 2)
player2_beat33 = beat((200, 0, 0), 2140, 2)
player2_beat34 = beat((200, 0, 0), 2200, 2)
player2_beat35 = beat((0, 0, 200), 2270, 2)
player2_beat36 = beat((200, 0, 0), 2300, 2)
player2_beat37 = beat((200, 0, 0), 2380, 2)
player2_beat38 = beat((200, 0, 0), 2440, 2)
player2_beat39 = beat((200, 0, 0), 2520, 2)
player2_beat40 = beat((0, 200, 0), 2570, 2)
player2_beat41 = beat((0, 0, 200), 2660, 2)
player2_beat42 = beat((200, 0, 0), 2720, 2)
player2_beat43 = beat((200, 0, 0), 2800, 2)
player2_beat44 = beat((0, 200, 0), 2860, 2)
player2_beat45 = beat((0, 200, 0), 2930, 2)
player2_beat46 = beat((200, 0, 0), 2995, 2)
player2_beat47 = beat((200, 0, 0), 3100, 2)
player2_beat48 = beat((0, 0, 200), 3170, 2)
player2_beat49 = beat((200, 0, 0), 3210, 2)
player2_beat50 = beat((0, 200, 0), 3250, 2)
player2_beat51 = beat((200, 0, 0), 3290, 2)
player2_beat52 = beat((200, 0, 0), 3340, 2)
player2_beat53 = beat((0, 0, 200), 3400, 2)
player2_beat54 = beat((200, 0, 0), 3450, 2)
player2_beat55 = beat((0, 0, 200), 3530, 2)
player2_beat56 = beat((200, 0, 0), 3620, 2)
player2_beat57 = beat((200, 0, 0), 3700, 2)
player2_beat58 = beat((0, 200, 0), 3740, 2)
player2_beat59 = beat((0, 0, 200), 3810, 2)
player2_beat60 = beat((0, 200, 0), 3870, 2)
player2_beat61 = beat((200, 0, 0), 3940, 2)
player2_beat62 = beat((200, 0, 0), 4040, 2)
player2_beat63 = beat((200, 0, 0), 4070, 2)
player2_beat64 = beat((0, 200, 0), 4150, 2)
player2_beat65 = beat((0, 0, 200), 4210, 2)
player2_beat66 = beat((200, 0, 0), 4260, 2)
player2_beat67 = beat((0, 0, 200), 4340, 2)
player2_beat68 = beat((200, 0, 0), 4400, 2)
player2_beat69 = beat((200, 0, 0), 4500, 2)
player2_beat70 = beat((0, 200, 0), 4550, 2)
player2_beat71 = beat((0, 0, 200), 4650, 2)
player2_beat72 = beat((0, 200, 0), 4750, 2)
player2_beat73 = beat((200, 0, 0), 4610, 2)
player2_beat74 = beat((200, 0, 0), 4650, 2)
player2_beat75 = beat((200, 0, 0), 4750, 2)
player2_beat76 = beat((0, 200, 0), 4800, 2)
player2_beat77 = beat((0, 0, 200), 4840, 2)
player2_beat78 = beat((200, 0, 0), 4940, 2)
player2_beat79 = beat((0, 0, 200), 4980, 2)
player2_beat80 = beat((200, 0, 0), 5050, 2)
player2_beat81 = beat((200, 0, 0), 5100, 2)
player2_beat82 = beat((0, 200, 0), 5140, 2)
player2_beat83 = beat((0, 0, 200), 5180, 2)
player2_beat84 = beat((0, 200, 0), 5270, 2)
player2_beat85 = beat((200, 0, 0), 5310, 2)
player2_beat86 = beat((200, 0, 0), 5410, 2)
player2_beat87 = beat((200, 0, 0), 5440, 2)
player2_beat88 = beat((0, 200, 0), 5540, 2)
player2_beat89 = beat((0, 0, 200), 5590, 2)
player2_beat90 = beat((200, 0, 0), 5670, 2)
player2_beat91 = beat((0, 0, 200), 5700, 2)
player2_beat92 = beat((200, 0, 0), 5770, 2)
player2_beat93 = beat((200, 0, 0), 5830, 2)
player2_beat94 = beat((0, 200, 0), 5900, 2)
player2_beat95 = beat((0, 0, 200), 6000, 2)
player2_beat96 = beat((0, 200, 0), 6040, 2)

beats = [player1_beat1,player1_beat2,player1_beat3,player1_beat4,player1_beat5,player1_beat6,player1_beat7,player1_beat8,player1_beat9,player1_beat10,player1_beat11,player1_beat12,player1_beat13,player1_beat14,player1_beat15,player1_beat16,player1_beat17,player1_beat18,player1_beat19,player1_beat20,player1_beat21,player1_beat22,player1_beat23,player1_beat24,player1_beat25,player1_beat26,player1_beat27,player1_beat28,player1_beat29,player1_beat30,player1_beat31,player1_beat32,player1_beat33,player1_beat34,player1_beat35,player1_beat36,player1_beat37,player1_beat38,player1_beat39,player1_beat40,player1_beat41,player1_beat42,player1_beat43,player1_beat44,player1_beat45,player1_beat46,player1_beat47,player1_beat48,player1_beat49,player1_beat50,player1_beat51,player1_beat52,player1_beat53,player1_beat54,player1_beat55,player1_beat56,player1_beat57,player1_beat58,player1_beat59,player1_beat60,player1_beat61,player1_beat62,player1_beat63,player1_beat64,player1_beat65,player1_beat66,player1_beat67,player1_beat68,player1_beat69,player1_beat70,player1_beat71,player1_beat72,player1_beat73,player1_beat74,player1_beat75,player1_beat76,player1_beat77,player1_beat78,player1_beat79,player1_beat80,player1_beat81,player1_beat82,player1_beat83,player1_beat84,player1_beat85,player1_beat86,player1_beat87,player1_beat88,player1_beat89,player1_beat90,player1_beat91,player1_beat92,player1_beat93,player1_beat94,player1_beat95,player1_beat96,player2_beat1,player2_beat2,player2_beat3,player2_beat4,player2_beat5,player2_beat6,player2_beat7,player2_beat8,player2_beat9,player2_beat10,player2_beat11,player2_beat12,player2_beat13,player2_beat14,player2_beat15,player2_beat16,player2_beat17,player2_beat18,player2_beat19,player2_beat20,player2_beat21,player2_beat22,player2_beat23,player2_beat24,player2_beat25,player2_beat26,player2_beat27,player2_beat28,player2_beat29,player2_beat30,player2_beat31,player2_beat32,player2_beat33,player2_beat34,player2_beat36,player2_beat37,player2_beat38,player2_beat39,player2_beat40,player2_beat41,player2_beat42,player2_beat43,player2_beat44,player2_beat45,player2_beat46,player2_beat47,player2_beat48,player2_beat49,player2_beat50,player2_beat51,player2_beat52,player2_beat53,player2_beat54,player2_beat55,player2_beat56,player2_beat57,player2_beat58,player2_beat59,player2_beat60,player2_beat61,player2_beat62,player2_beat63,player2_beat64,player2_beat65,player2_beat66,player2_beat67,player2_beat68,player2_beat69,player2_beat70,player2_beat71,player2_beat72,player2_beat73,player2_beat74,player2_beat75,player2_beat76,player2_beat77,player2_beat78,player2_beat79,player2_beat80,player2_beat81,player2_beat82,player2_beat83,player2_beat84,player2_beat85,player2_beat86,player2_beat87,player2_beat88,player2_beat89,player2_beat90,player2_beat91,player2_beat92,player2_beat93,player2_beat94,player2_beat95,player2_beat96]
player1.beats = [player1_beat1,player1_beat2,player1_beat3,player1_beat4,player1_beat5,player1_beat6,player1_beat7,player1_beat8,player1_beat9,player1_beat10,player1_beat11,player1_beat12,player1_beat13,player1_beat14,player1_beat15,player1_beat16,player1_beat17,player1_beat18,player1_beat19,player1_beat20,player1_beat21,player1_beat22,player1_beat23,player1_beat24,player1_beat25,player1_beat26,player1_beat27,player1_beat28,player1_beat29,player1_beat30,player1_beat31,player1_beat32,player1_beat33,player1_beat34,player1_beat35,player1_beat36,player1_beat37,player1_beat38,player1_beat39,player1_beat40,player1_beat41,player1_beat42,player1_beat43,player1_beat44,player1_beat45,player1_beat46,player1_beat47,player1_beat48,player1_beat49,player1_beat50,player1_beat51,player1_beat52,player1_beat53,player1_beat54,player1_beat55,player1_beat56,player1_beat57,player1_beat58,player1_beat59,player1_beat60,player1_beat61,player1_beat62,player1_beat63,player1_beat64,player1_beat65,player1_beat66,player1_beat67,player1_beat68,player1_beat69,player1_beat70,player1_beat71,player1_beat72,player1_beat73,player1_beat74,player1_beat75,player1_beat76,player1_beat77,player1_beat78,player1_beat79,player1_beat80,player1_beat81,player1_beat82,player1_beat83,player1_beat84,player1_beat85,player1_beat86,player1_beat87,player1_beat88,player1_beat89,player1_beat90,player1_beat91,player1_beat92,player1_beat93,player1_beat94,player1_beat95,player1_beat96]
player2.beats = [player2_beat1,player2_beat2,player2_beat3,player2_beat4,player2_beat5,player2_beat6,player2_beat7,player2_beat8,player2_beat9,player2_beat10,player2_beat11,player2_beat12,player2_beat13,player2_beat14,player2_beat15,player2_beat16,player2_beat17,player2_beat18,player2_beat19,player2_beat20,player2_beat21,player2_beat22,player2_beat23,player2_beat24,player2_beat25,player2_beat26,player2_beat27,player2_beat28,player2_beat29,player2_beat30,player2_beat31,player2_beat32,player2_beat33,player2_beat34,player2_beat36,player2_beat36,player2_beat37,player2_beat38,player2_beat39,player2_beat40,player2_beat41,player2_beat42,player2_beat43,player2_beat44,player2_beat45,player2_beat46,player2_beat47,player2_beat48,player2_beat49,player2_beat50,player2_beat51,player2_beat52,player2_beat53,player2_beat54,player2_beat55,player2_beat56,player2_beat57,player2_beat58,player2_beat59,player2_beat60,player2_beat61,player2_beat62,player2_beat63,player2_beat64,player2_beat65,player2_beat66,player2_beat67,player2_beat68,player2_beat69,player2_beat70,player2_beat71,player2_beat72,player2_beat73,player2_beat74,player2_beat75,player2_beat76,player2_beat77,player2_beat78,player2_beat79,player2_beat80,player2_beat81,player2_beat82,player2_beat83,player2_beat84,player2_beat85,player2_beat86,player2_beat87,player2_beat88,player2_beat89,player2_beat90,player2_beat91,player2_beat92,player2_beat93,player2_beat94,player2_beat95,player2_beat96]
rems = []
projectiles = []
summons = []
hitables = []

while selection < 2:
    current_time = timekeep.time()
    if current_time - last_second_time >= 0.005:
        tick_multiplier_debug = 200/(ticks/(current_time - last_second_time))
        #tick_multiplier_debug = #50/(ticks/(current_time - last_second_time))
        timestep = True
        ticks = 0
        numberkey = current_time - last_second_time
        last_second_time = current_time

    else:
        timestep = False
    ticks+=1
    ticks1+=1
    if current_time - last_second_time1 >= 1:
        tps = ticks1/(current_time - last_second_time1)
        # tick_multiplier_debug = 50/(ticks1/(current_time - last_second_time1))
        
        ticks1 = 0
        last_second_time1 = current_time
    key = pygame.key.get_pressed()
    screen.fill((255,255,255))
    text = bossfont.render('tps ' + str(round(tps)),True,(0,0,0),(200,200,200))
    screen.blit(text,(50,200))
    if selection == -1:
        text = pygame.font.SysFont(None,round(titlewordsize)).render(('beat '),True,title_word_color,(255,255,255))
        screen.blit(text,(200 - round(titlewordsize/2), 100 - round(titlewordsize/4)))
        if titlewordsize < 100:
            titlewordsize = 100
            titlewordsizechangespeed = 2
            title_word_color_randomizer = random.randint(1,4)
            if title_word_color_randomizer == 1:
                title_word_color = (200, 0, 0)
            elif title_word_color_randomizer == 2:
                title_word_color = (0, 0, 200)
            elif title_word_color_randomizer == 3:
                title_word_color = (0, 200, 0)
            elif title_word_color_randomizer == 4:
                title_word_color = (200, 200, 0)
        titlewordsize += titlewordsizechangespeed*tick_multiplier_debug
        titlewordsizechangespeed -= 0.03*tick_multiplier_debug
        text = pygame.font.SysFont(None, 110).render('down',True,(0,0,0),(255,255,255))
        screen.blit(text,(410,80))
        text = bossfont.render('<play>',True,(0,0,0),(255,255,255))
        screen.blit(text,(100,400))
        if key[pygame.K_RETURN] == True and dp < 1:
            dp = 70
            selection = 0
    elif selection == 0:
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
                dp = 70
                players = 2
                selection = 1
        if selecting == 2:
            text = bossfont.render('<3>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,500))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 70
                players = 3
                selection = 1
        if selecting == 3:
            text = bossfont.render('<4>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,600))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 70
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
                dp = 70
                player_list[player_select_iterator].player_type = 1
                player_list[player_select_iterator].health = 370
                player_select_iterator += 1
        if selecting == 2:
            text = bossfont.render('<jekyll&hyde>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,500))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 70
                player_list[player_select_iterator].player_type = 2
                player_list[player_select_iterator].health = 400
                player_select_iterator += 1
        if selecting == 3:
            text = bossfont.render('<greatest_showman>',True,(0,0,0),(200,200,200))
            screen.blit(text,(100,600))
            if key[pygame.K_RETURN] == True and dp < 1:
                dp = 70
                player_list[player_select_iterator].player_type = 3
                player_list[player_select_iterator].health = 300
                player_select_iterator += 1
        if (player_select_iterator+1) > players:
            selection = 2
    if key[pygame.K_DOWN] == True and dp < 1:
        selecting+=1
        if selecting>3:
            selecting = 1
        dp = 50
    elif key[pygame.K_UP] == True and dp < 1:
        selecting-=1
        if selecting<1:
            selecting = 3
        dp = 50
    else:
        dp-=1*tick_multiplier_debug
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            selection = 3
    if timestep == True:
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
    player_list[i].move((i*400)+100,750-player_list[i].height)
    i += 1



while run == True:
    current_time = timekeep.time()
    if current_time - last_second_time >= 0.02:
        tick_multiplier_debug = 300/(ticks/(current_time - last_second_time))
        #tick_multiplier_debug = #50/(ticks/(current_time - last_second_time))
        timestep = True
        ticks = 0
        last_second_time = current_time

    else:
        timestep = False
    ticks+=1
    ticks1+=1
    if current_time - last_second_time1 >= 1:
        tps = ticks1/(current_time - last_second_time1)
        # tick_multiplier_debug = 50/(ticks1/(current_time - last_second_time1))
        
        ticks1 = 0
        last_second_time1 = current_time
    hitables = player_list + summons
    beats.sort(key=lambda beat: beat.point_in_song)
    key = pygame.key.get_pressed()
    screen.fill((255,255,255))
    for aplay in player_list:
        aplay.move_ip(aplay.xmom*tick_multiplier_debug,aplay.ymom*tick_multiplier_debug)
        if not aplay.attack_moving_damage == 0:
            for aplayer in player_list:
                if not aplayer == aplay:
                    if aplay.colliderect(aplayer):
                        aplayer.health -= aplay.attack_moving_damage
                        aplay.xmom *= -0.3
                        aplay.attack_moving_damage = 0
        if aplay.xmom < -0.2*tick_multiplier_debug:
            aplay.xmom+=0.1*tick_multiplier_debug
        elif aplay.xmom > 0.2*tick_multiplier_debug:
            aplay.xmom-=0.1*tick_multiplier_debug
        else:
            aplay.xmom = 0
            aplay.attack_moving_damage = 0
        if aplay.bottom < 750:
            aplay.ymom+=0.2*tick_multiplier_debug
        else:
            aplay.ymom = 0
            aplay.move(aplay.x,750 - aplay.height)
        if aplay.left < 0:
            aplay.xmom *= -1
            aplay.move(0,aplay.y)
        if aplay.right > 1540:
            aplay.xmom *= -1
            aplay.move(1540 - aplay.width,aplay.y)
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
    
    pygame.draw.rect(screen, (200,0,0),beat_indicator_bottom)
    pygame.draw.rect(screen, (200,0,0),beat_indicator_top)
    pygame.draw.rect(screen, (200,0,0),beat_indicator_left)
    pygame.draw.rect(screen, (200,0,0),beat_indicator_right)
    beat_indicator_bottom.move_ip(0,-1*beat_ind_vel*tick_multiplier_debug)
    beat_indicator_bottom.height = 790 - beat_indicator_bottom.y
    beat_indicator_right.move_ip(-1*beat_ind_vel*tick_multiplier_debug,0)
    beat_indicator_right.width = 1540 - beat_indicator_right.x
    beat_indicator_left.width += beat_ind_vel*tick_multiplier_debug
    beat_indicator_top.height += beat_ind_vel*tick_multiplier_debug
    beat_ind_vel-=0.1*tick_multiplier_debug
    if beat_indicator_bottom.height < 5:
        beat_indicator_bottom.resetInitialPosition()
        beat_indicator_right.resetInitialPosition()
        beat_indicator_left.resetInitialPosition()
        beat_indicator_top.resetInitialPosition()
        beat_ind_vel = 0
        beat_indicator_bottom.height = 5
        beat_indicator_top.height = 5
        beat_indicator_right.width = 5
        beat_indicator_left.width = 5

    #health,damage,time_between_hits,ranged,attack_duration,origin

    for asum in summons:
        if asum.health > 0:
            if asum.cooldown < 0:
                asum.cooldown = asum.time_between_hits
                if asum.ranged == False:
                    arrow = projectile(asum.x-30,asum.centery,asum.right - asum.x + 30,10,0,0,10,asum.origin,asum.damage)
                    projectiles.append(arrow)
                else:
                    i = 0
                    for aplay in player_list:
                        if aplay.x < asum.x:
                            i-=1
                        else:
                            i+=1
                    if i > 0:
                        i = 1
                    else:
                        i = -1
                    arrow = projectile(asum.centerx,asum.centery,30,10,3*i,0,asum.attack_duration,asum.origin,asum.damage)
                    projectiles.append(arrow)
        else:
            summons.remove(asum)
    pygame.draw.line(screen, (0,0,0), (0,(750)), (3000,(750)), 4)
    text = tutorialfont.render(str(beatspassedplayer1),True,(0,0,0),(255,255,255))
    screen.blit(text,(700,500))
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
            pygame.draw.line(screen, (0,0,0), (40,((60*i)-25)), (40,((60*i)+25)), 4)
            pygame.draw.line(screen, (0,0,0), (80,((60*i)-25)), (80,((60*i)+25)), 4)
        i+=1
    for abeat in beats:
        pygame.draw.circle(screen, abeat.color, (abeat.point_in_song, (abeat.player * 60)), 12)
        abeat.point_in_song -= 0.3*tick_multiplier_debug
        if abeat.point_in_song < 30:
            rems.append(abeat)
    for arem in rems:
        beats.remove(arem)
    rems.clear()
    for aplayer in player_list:
        aplayer.beat_count = len(aplayer.beats)
        i = 0
        for abeat in aplayer.beats:
            # if abeat in aplayer.beats:
                if abeat.point_in_song < 80 and abeat.point_in_song > 40:
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
                    if aplayer.beat_ind == True:
                        pygame.draw.circle(screen, abeat.color, (abeat.point_in_song, (abeat.player * 60)), round(12 + (abeat.point_in_song - 50)/3))
                        if abeat.point_in_song < 40:
                            aplayer.beat_ind = False
                    if abeat.rachet == True:
                        aplayer.beat_on = True
                        abeat.rachet = False
                        aplayer.beat_ind = True
                        for asum in summons:
                            asum.cooldown -= 1
                        if abeat in player1.beats:
                            beatspassedplayer1 += 1
                        for aplayer in player_list:
                            aplayer.heal_block -= 1
                            aplayer.heal_block -= 1
                            aplayer.beat_shown -= 1
                            aplayer.health -= aplayer.toxin
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
                            beat_ind_vel = 2
                else:
                    aplayer.beat_count -= 1
                    i += 1
        if aplayer.beat_count <= 0:
            aplayer.beat_type = 0
        if not i < len(aplayer.beats):
            aplayer.beat_on = False
            aplayer.beat_type = 0
    for aplayer in player_list:
        if aplayer.armour > 0:
            aplayer.armour -= 0.2
        elif aplayer.armour < 0:
            aplayer.armour = 0
    # if aplayer.beat_count == len(aplayer.beats):
    #     aplayer.beat_type = 0
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
                arrow = projectile(aplayer.centerx-100,aplayer.top-10,200,aplayer.height + 10,0,0,10,aplayer,30)
                projectiles.append(arrow)
            if aplayer.player_type == 1 and aplayer.beat_on == True:
                if key[aplayer.player_keybinds[0]]:
                    aplayer.last_key_pressed = 0
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        for aplay in player_list:
                            if aplayer.centerx < aplay.centerx + 70 and aplayer.centerx > aplay.centerx - 70 and aplayer.bottom < aplay.bottom - 40:
                                aplay.xmom *= -0.1
                                aplay.attack_moving_damage = 0
                        arrow = projectile(aplayer.centerx-70,aplayer.centery,140,10,0,0,10,aplayer,10)
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
                        arrow = projectile(aplayer.centerx,aplayer.centery,30,10,3*i,0,400,aplayer,10)
                        projectiles.append(arrow)
                    elif aplayer.beat_type == 3:
                        if aplayer.heal_block < 0:
                            aplayer.armour = 50
                elif key[aplayer.player_keybinds[1]]:
                    aplayer.last_key_pressed = 1
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
                        aplayer.beats[1].color = (0,0,200)
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
                        arrow = projectile(aplayer.centerx-70,aplayer.centery,140,10,0,0,10,aplayer,20)
                        projectiles.append(arrow)
                elif key[aplayer.player_keybinds[2]]:
                    aplayer.last_key_pressed = 2
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        arrow = projectile(aplayer.centerx-80,aplayer.centery,160,10,0,0,10,aplayer,15)
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
                    elif aplayer.beat_type == 3:
                        for aplay in player_list:
                            if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                aplay.toxin += 3
                        arrow = projectile(aplayer.centerx-50,aplayer.centery,100,10,0,0,10,aplayer,0)
                        projectiles.append(arrow)
                if key[aplayer.player_keybinds[3]]:
                    aplayer.last_key_pressed = 3
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        for aplay in player_list:
                            if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                stagger(1,aplay)
                        arrow = projectile(aplayer.centerx-50,aplayer.centery,100,10,0,0,10,aplayer,10)
                        projectiles.append(arrow)
                    elif aplayer.beat_type == 2:
                        arrow = projectile(aplayer.centerx-10,aplayer.centery,20,10,random.randint(-1,1),0,200,aplayer,50)
                        projectiles.append(arrow)
                    elif aplayer.beat_type == 3:
                        for aplay in player_list:
                            if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                aplay.lost_healt_per_miss += 5
                                stagger(3,aplay)
                        arrow = projectile(aplayer.centerx-50,aplayer.centery,100,10,0,0,10,aplayer,0)
                        projectiles.append(arrow)
            elif aplayer.player_type == 2 and aplayer.beat_on == True:
                print("yum")
                if aplayer.insanity > 30:
                    aplayer.depravity+=1
                    aplayer.insanity = 0
                    for aplay in player_list:
                        if aplay.centerx < aplayer.centerx + 100 and aplay.centerx > aplayer.centerx - 100 and aplay.bottom < aplayer.bottom - 70:
                            if aplayer.transformed == 0:
                                aplayer.transformed = 1
                            else:
                                aplayer.transformed = 0
                    arrow = projectile(aplayer.centerx-100,aplayer.top-10,200,aplayer.height + 10,0,0,10,aplayer,30)
                    projectiles.append(arrow)
                elif key[aplayer.player_keybinds[0]]:
                    aplayer.beat_on = False
                    aplayer.insanity += aplayer.depravity
                    if aplayer.beat_type == 1:
                        if aplayer.transformed == 0:
                            if aplayer.heal_block < 0:
                                aplayer.health += 30
                            aplayer.beats[1].color = (200,0,200)
                        else:
                            for aplay in player_list:
                                if aplay.centerx < aplayer.centerx + 50 and aplay.centerx > aplayer.centerx - 50 and aplay.bottom < aplayer.bottom - 40:
                                    aplay.heal_block = 5
                            arrow = projectile(aplayer.centerx-50,aplayer.top-10,100,aplayer.height + 10,0,0,10,aplayer,10)
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
                            arrow = projectile(aplayer.centerx-50,aplayer.top-10,100,aplayer.height + 10,0,0,10,aplayer,aplayer.insanity*3)
                            projectiles.append(arrow)
                        else:
                            aplay.multiply = [1.1,2]
                            truant(2,aplay)
                elif key[aplayer.player_keybinds[1]]:
                    aplayer.beat_on = False
                    aplayer.insanity += aplayer.depravity
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
                    aplayer.insanity += aplayer.depravity
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
                            arrow = projectile(aplayer.centerx-70,aplayer.top-10,140,aplayer.height + 10,0,0,10,aplayer,10)
                            projectiles.append(arrow)
                    elif aplayer.beat_type == 3:
                        if aplayer.tranformed == 0:
                            aplayer.insanity -= 10
                            aplayer.health += 10
                        else:
                            deal_dammage(5,aplayer)
                            aplayer.insanity += 10
                if key[aplayer.player_keybinds[3]]:
                    aplayer.beat_on = False
                    aplayer.insanity += aplayer.depravity
                    if aplayer.beat_type == 1:
                        if aplayer.transformed == 0:
                            deal_dammage(5,aplayer)
                            aplayer.insanity += 10
                        else:
                            for aplayer in player_list:
                                if aplayer.centerx < aplayer.centerx + 80 and aplayer.centerx > aplayer.centerx - 80 and aplayer.bottom < aplayer.bottom - 40:
                                    deal_dammage(15,aplay)
                            arrow = projectile(aplayer.centerx-80,aplayer.top-10,160,aplayer.height + 10,0,0,10,aplayer,15)
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
            elif aplayer.player_type == 2 and aplayer.beat_on == True:
                if key[aplayer.player_keybinds[0]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        tomb_thumb = summon(aplayer.x,730,20,60,20,5,1,False,5,aplayer)
                    elif aplayer.beat_type == 2:
                        bearded_lady = summon(aplayer.x,710,50,80,50,0,1,False,0,aplayer)
                    elif aplayer.beat_type == 3:
                        strongman = summon(aplayer.x,700,50,90,50,20,1,False,5,aplayer)
                        aplayer.health-=5
                elif key[aplayer.player_keybinds[1]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        
                    elif aplayer.beat_type == 2:

                    elif aplayer.beat_type == 3:
                        i = 0
                        for aplay in player_list:
                            if aplay.x < aplayer.x:
                                i-=1
                            else:
                                i+=1
                        if i > 0:
                            aplayer.xmom = -8
                            i = 1
                        else:
                            aplayer.xmom = 8
                            i = -1
                        a = -1
                        while a < 1:
                            arrow = projectile(aplayer.centerx - a*50,aplayer.centery,30,10,5*i,a,200,aplayer,10)
                            projectiles.append(arrow)
                            a+=1
                elif key[aplayer.player_keybinds[2]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        i = 0
                        for aplay in player_list:
                            if aplay.x < aplayer.x:
                                i-=1
                            else:
                                i+=1
                        if i > 0:
                            aplayer.xmom = -9
                        else:
                            aplayer.xmom = 9
                        aplayer.attack_moving_damage = 10
                    elif aplayer.beat_type == 2:

                    elif aplayer.beat_type == 3:

                elif key[aplayer.player_keybinds[3]]:
                    aplayer.beat_on = False
                    if aplayer.beat_type == 1:
                        
                    elif aplayer.beat_type == 2:

                    elif aplayer.beat_type == 3:

    text = bossfont.render('tps ' + str(round(tps)),True,(0,0,0),(200,200,200))
    screen.blit(text,(50,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if timestep == True:
        pygame.display.update()
pygame.quit()