#Fabian Santiago 2020, El puto de pygame solo admite sonidos de 16 bits

import pygame, random
from pygame.locals import *
from script import decoration, resources
pygame.init()


Texture_pack = resources.sprite_sheet
Inavder_Dead_Sound = resources.Inavder_Dead_Sound


score = 0
score_list = list()

ran_enemy = pygame.sprite.Group()
ch_ran =  pygame.sprite.Group()

def init(all_sprites1, enemy_sprites1, bullet_sprites1, bullet_pl_sprites1, limit_in_l1, limit_in_r1, enemy_pos1, shield_sprites1, bullet_en_sprites1, pl_sprites1):
    global all_sprites
    global enemy_sprites
    global bullet_sprites
    global bullet_pl_sprites
    global limit_in_l
    global limit_in_r
    global en_pos
    global shield_sprites
    global bullet_en_sprites
    global pl_sprites
    
    all_sprites = all_sprites1
    enemy_sprites = enemy_sprites1
    bullet_sprites = bullet_sprites1
    bullet_pl_sprites = bullet_pl_sprites1
    limit_in_l = limit_in_l1
    limit_in_r = limit_in_r1
    en_pos = enemy_pos1
    shield_sprites = shield_sprites1
    bullet_en_sprites = bullet_en_sprites1
    pl_sprites = pl_sprites1

 
def Generate_Enemy(pos_x, pos_y, enemy_type, enemy_y, bullet_probl):
    decoration.init(all_sprites, all_sprites)
    enemy_sheet = [ ( (5, 1, 8, 8), (5, 11, 8, 8) ), # 30 puntos
                    ( (22, 1, 11, 8), (22, 11, 11, 8) ), #20 puntos
                    ( (39, 1, 12, 8), (39, 11, 12, 8) ), ] #10 puntos
    #pos_x += 380
    
    if enemy_type == 30:
        number = 0
        IMG_CONV = (21, 24)
        #pos_x += 6
        
    if enemy_type == 20:
        number = 1
        IMG_CONV = (27, 24)
        #pos_x += 3
        
    if enemy_type == 10:
        number = 2
        IMG_CONV = (30, 24)
        
    for n in range(11):      
        enemy =  Enemy(enemy_sheet[number], IMG_CONV, pos_x, pos_y, enemy_y, bullet_probl)
        
        #pygame.time.wait(20) #Esto es lo que hace que se generen con retardo :D
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

        pos_x += 38
        
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, IMG_SPRITES, IMG_CONV, x, y, enemy_y, bullet_probl):
        super().__init__()
        self.INIT_P_X = x
        self.INIT_P_Y = y 
        
        self.IMG_SPRITES = IMG_SPRITES
        self.IMG_CONV = IMG_CONV
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.IMG_SPRITES[0]))
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, self.IMG_CONV)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.speed_X = 6
        
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1600
        self.frame_rev = True
        
        self.rev = True
        self.down = 24
        
        self.phase = 1
        self.rev_count_phase = True
        self.rev_phase = 1
        
        #42+33+42+33+42+33+42....
        self.limit = [42, 75, 117, 150, 192, 225, 267, 300, 342, 375, 417, 450, 492]
        self.enemy_y =  enemy_y
        
        self.bullet_probl =  bullet_probl

    
    def Shoot(self, center, y, number):
        bullet = En_Bullet(center, y, number) 
        all_sprites.add(bullet)
        
        bullet_sprites.add(bullet)
        bullet_en_sprites.add(bullet)
    
    
    def Ratio_Control(self): #Esta muy injusto !!!!!        
        number_list = [55, 54, 53, 52, 51,
                       50, 49, 48, 47, 46, 
                       45, 44, 43, 42, 41, 
                       40, 39, 38, 37, 36, 
                       35, 34, 33, 32, 31, 
                       30, 29, 28, 27, 26, 
                       25, 24, 23, 22, 21, 
                       20, 19, 18, 17, 16, 
                       15, 14, 13, 12, 11, 
                       10, 9, 8, 7, 6, 
                       5, 4, 3, 2, 1]
                       
        rate_list = [1630, 1600, 1570, 1540, 1510,
                     1480, 1450, 1420, 1390, 1360, 
                     1330, 1300, 1270, 1240, 1210, 
                     1180, 1150, 1120, 1090, 1060, 
                     1030, 1000, 970, 940, 910, 
                     880, 850, 820, 790, 760, 
                     730, 700, 670, 640, 610,
                     580, 550, 520, 490, 460, 
                     430, 400, 370, 340, 310, 
                     280, 250, 220, 190, 160, 
                     130, 100, 70, 40, 10]
         
        for l in range(55):
            if len(enemy_sprites) == number_list[l]: self.frame_rate = rate_list[l]


    def Animation(self):
        v =  random.randrange(0, 100)
        if self.rev == True:
            if self.rect.x >= self.INIT_P_X + self.limit[limit_in_r]: #+33+42+33: #+33
                self.rev = False
                self.rect.y += self.down
                self.speed_X *= -1
                

        if self.rev == False:
            if self.rect.x <= self.INIT_P_X - self.limit[limit_in_l]: #-33
                self.rev = True
                self.rect.y += self.down
                self.speed_X *= -1
                

                    
        for enemy in enemy_sprites:
            if enemy.rect.y >= 550:
                self.down = 0
                
                
            else:
                self.down = 24

      
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
        
            self.rect.x += self.speed_X #El movimiemto va acorde la animación 
            self.last_update = now
            self.frame += 1
            
            if self.frame >= 2:
                self.frame = 0        
                if v < self.bullet_probl:
                    self.Shoot(self.rect.center, self.rect.y, random.randrange(0, 3))

            self.sheet.set_clip(pygame.Rect(self.IMG_SPRITES[self.frame]))
                    
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image.set_colorkey((000, 000, 000))
            
            self.image =  pygame.transform.scale(self.image, self.IMG_CONV)


    def Dead(self):
        global score
        decoration.init(all_sprites, all_sprites)
        
        dead_list = pygame.sprite.groupcollide(enemy_sprites, bullet_pl_sprites, True, True)
        for enemy in dead_list:
            Inavder_Dead_Sound.play()
            Inavder_Dead_Sound.set_volume(0.1)
            explosion = decoration.Explosion(enemy.rect.center, (56, 1, 13, 8), ((56, 1, 13, 8), (56, 1, 13, 8)), 300, (33, 24))
            all_sprites.add(explosion)
            
            self.Tester(enemy, self.enemy_y[0], 0, 10)
                
            self.Tester(enemy, self.enemy_y[1], 11, 10)
                
            self.Tester(enemy, self.enemy_y[2], 22, 20)
                
            self.Tester(enemy, self.enemy_y[3], 33, 20)
                
            self.Tester(enemy, self.enemy_y[4], 44, 30)


    def Tester(self, enemy, number_y, raw_point, s):
        global score
        if enemy.INIT_P_Y == number_y:
            score += s
            if enemy.INIT_P_X == 60:
                en_pos[raw_point] = 0
                
            if enemy.INIT_P_X == 98:
                en_pos[raw_point+1] = 0
                
            if enemy.INIT_P_X == 136:
                en_pos[raw_point+2] = 0
            
            if enemy.INIT_P_X == 174:
                en_pos[raw_point+3] = 0
                
            if enemy.INIT_P_X == 212:
                en_pos[raw_point+4] = 0
            
            if enemy.INIT_P_X == 250:
                en_pos[raw_point+5] = 0
                
            if enemy.INIT_P_X == 288:
                en_pos[raw_point+6] = 0
            
            if enemy.INIT_P_X == 326:
                en_pos[raw_point+7] = 0
                
            if enemy.INIT_P_X == 364:
                en_pos[raw_point+8] = 0
            
            if enemy.INIT_P_X == 402:
                en_pos[raw_point+9] = 0
                
            if enemy.INIT_P_X == 440:
                en_pos[raw_point+10] = 0


    def Collide_Control(self):
        if self.Collide_RAW(0, 0, 1) == True:
            if self.Collide_RAW(0, 1, 2) == True:
                if self.Collide_RAW(0, 2, 3) == True:
                    if self.Collide_RAW(0, 3, 4) == True:
                        if self.Collide_RAW(0, 4, 5) == True:
                            if self.Collide_RAW(0, 5, 6) == True:
                                if self.Collide_RAW(0, 6, 7) == True:
                                    if self.Collide_RAW(0, 7, 8) == True:
                                        if self.Collide_RAW(0, 8, 9) == True:
                                            if self.Collide_RAW(0, 9, 10) == True:
                                                pass
            
            
        if self.Collide_RAW(1, 10, 1) == True:
            if self.Collide_RAW(1, 9, 2) == True:
                if self.Collide_RAW(1, 8, 3) == True:
                    if self.Collide_RAW(1, 7, 4) == True:
                        if self.Collide_RAW(1, 6, 5) == True:
                            if self.Collide_RAW(1, 5, 6) == True:
                                if self.Collide_RAW(1, 4, 7) == True:
                                    if self.Collide_RAW(1, 3, 8) == True:
                                        if self.Collide_RAW(1, 2, 9) == True:
                                            if self.Collide_RAW(1, 1, 10) == True:
                                                pass


    def Collide_RAW(self, limit, pos, number):
        global limit_in_l
        global limit_in_r
        if limit == False:
        
            if en_pos[pos] == 0:
            
                if en_pos[pos+11] == 0:
                
                    if en_pos[pos+22] == 0:
                    
                        if en_pos[pos+33] == 0:
                        
                            if en_pos[pos+44] == 0:
                                limit_in_l = number
                                
                                return True
                                
        if limit == True:
        
            if en_pos[pos] == 0:
            
                if en_pos[pos+11] == 0:
                
                    if en_pos[pos+22] == 0:
                    
                        if en_pos[pos+33] == 0:
                        
                            if en_pos[pos+44] == 0:
                                limit_in_r = number
                                
                                return True

   
    def Pause(self):
        for pl in pl_sprites:
            if pl.pause == True:
                self.frame_rev = False
                self.frame_rate = 12000
                
            if pl.pause == False:
                self.frame_rev = True

    
    def update(self):
        self.Collide_Control()
        self.Animation()
        self.Dead()
        self.Pause()
        
        if self.frame_rev == True:
            self.Ratio_Control()



class Sound_Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()       
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(1, 1, 1, 1))
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (1, 1))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 0
        
        self.phase = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1600
        self.frame_rev = True
        
        self.rev = True
        
        self.chronometer1 = decoration.Chronometer(32000)
        self.rand_rev = -2
        
    
    def Ratio_Control(self): #Esta muy injusto !!!!!
        number_list = [55, 54, 53, 52, 51,
                       50, 49, 48, 47, 46, 
                       45, 44, 43, 42, 41, 
                       40, 39, 38, 37, 36, 
                       35, 34, 33, 32, 31, 
                       30, 29, 28, 27, 26, 
                       25, 24, 23, 22, 21, 
                       20, 19, 18, 17, 16, 
                       15, 14, 13, 12, 11, 
                       10, 9, 8, 7, 6, 
                       5, 4, 3, 2, 1]
                       
        rate_list = [1630, 1600, 1570, 1540, 1510,
                     1480, 1450, 1420, 1390, 1360, 
                     1330, 1300, 1270, 1240, 1210, 
                     1180, 1150, 1120, 1090, 1060, 
                     1030, 1000, 970, 940, 910, 
                     880, 850, 820, 790, 760, 
                     730, 700, 670, 640, 610,
                     580, 550, 520, 490, 460, 
                     430, 400, 370, 340, 310, 
                     280, 250, 220, 190, 160, 
                     130, 100, 70, 40, 10]
         
        for l in range(55):
            if len(enemy_sprites) == number_list[l]: self.frame_rate = rate_list[l]


    def Sound(self):
        fastinvader1 =  resources.fastinvader1
        fastinvader2 =  resources.fastinvader2
        fastinvader3 =  resources.fastinvader3
        fastinvader4 =  resources.fastinvader4
        
        fast = [fastinvader1, fastinvader2, fastinvader3, fastinvader4]
    
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:

            self.last_update = now
            self.phase += 1
            
            if self.phase >= 4:
                self.phase = 0
            
            fast[self.phase-1].stop()
            fast[self.phase].play()
            
            if len(ran_enemy) == 0:
                fast[self.phase].set_volume(0.3)
                
            if len(ran_enemy) > 0:
                fast[self.phase].set_volume(0.0)


    def Pause(self):
        for pl in pl_sprites:
            if pl.pause == True:
                self.frame_rev = False
                self.frame_rate = 12000
                
            if pl.pause == False:
                self.frame_rev = True
                
                
    def update(self):
        self.Pause()
        
        if self.frame_rev == True:
            self.Ratio_Control()
            
        if len(enemy_sprites) == 0:
            self.kill()
             
        self.Sound()
        
        if self.chronometer1.Play() == True:
            if len(ran_enemy) == 0:
                self.rand_rev *= -1
                random_enemy = Rand_Enemy(self.rand_rev)
                all_sprites.add(random_enemy)
                ran_enemy.add(random_enemy)


class Rand_Enemy(pygame.sprite.Sprite):
    def __init__(self, rev):
        super().__init__()
        self.IMG_SPRITES = ((1, 39, 16, 8), (19, 39, 24, 8))
        self.IMG_CONV = ((40, 24), (60, 24))
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.IMG_SPRITES[0]))
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, self.IMG_CONV[0])
        
        self.rect = self.image.get_rect()
        
        self.ufo_highpitch =  resources.ufo_highpitch
        self.ufo_lowpitch =  resources.ufo_lowpitch
        
        if rev == 2:
            self.rect.x = 9
            self.speed_X = 2
            self.s = 2
            self.ufo_highpitch.play()
            self.ufo_highpitch.set_volume(0.1)
            
            
        if rev == -2:
            self.rect.x = 471
            self.speed_X = -2
            self.s = -2
            self.ufo_lowpitch.play()
            self.ufo_lowpitch.set_volume(0.1)
            
            
        self.rect.y = 100
        

    def Dead(self):
        global score
        bullet_n_ship = pygame.sprite.groupcollide(ran_enemy, bullet_pl_sprites, True, True)
        for ship in bullet_n_ship:
            self.ufo_highpitch.stop()
            self.ufo_lowpitch.stop()
            explosion = decoration.Explosion(ship.rect.center, (19, 39, 24, 8), ((19, 39, 24, 8), (19, 39, 24, 8), (19, 39, 24, 8)), 300, (60, 24))
            all_sprites.add(explosion)
            score += random.randrange(30, 110, 10)
    
    def Pause(self):
        for pl in pl_sprites:
            if pl.pause == True:
                self.speed_X = 0
                self.ufo_highpitch.set_volume(0.0)
                self.ufo_lowpitch.set_volume(0.0)
       
                    
            if pl.pause == False:
                self.speed_X = self.s
                self.ufo_highpitch.set_volume(0.1)
                self.ufo_lowpitch.set_volume(0.1)
        
    def update(self):
        self.Dead()
        self.Pause()
        self.rect.x += self.speed_X
        if self.rect.x < 8:
            self.ufo_highpitch.stop()
            self.ufo_lowpitch.stop()
            self.kill()
        
        if self.rect.x > 472:
            self.ufo_highpitch.stop()
            self.ufo_lowpitch.stop()
            self.kill()


class En_Bullet(pygame.sprite.Sprite):
    def __init__(self, center, y, rannomber):
    
        self.IMG_SPRITES = [((1, 21), (6, 21), (11, 21), (16, 21)),
                            ((21, 21), (26, 21), (31, 21), (36, 21)),
                            ((41, 21), (46, 21), (51, 21), (56, 21)),]
        
        
        self.IMG_CONV = (8, 21)
        
        self.no_bullet = rannomber

        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(  self.IMG_SPRITES[0][0] +(3, 7) ))
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, self.IMG_CONV)
        
        self.rect = self.image.get_rect()
        
        self.rect.center =  center
        self.rect.y = y
        
        self.speed_Y = 5
        
        self.frame = 0      
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60
        
    def Animation_N_Movement(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
                
            if self.frame >= 4:
                self.frame = 0

            self.sheet.set_clip(pygame.Rect( self.IMG_SPRITES[self.no_bullet][self.frame] +(3, 7)))
                    
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image.set_colorkey((000, 000, 000))
            
            self.image =  pygame.transform.scale(self.image, self.IMG_CONV)
            
           
    def Dead(self):
        
    
        if self.rect.y >= 607:
            explosion = decoration.Explosion(self.rect.center, (61, 21, 6, 8), ((61, 21, 6, 8), (61, 21, 6, 8)), 300, (15, 24))
            all_sprites.add(explosion)
            self.kill()
            
            
        bullet_n_bullet =  pygame.sprite.groupcollide(bullet_en_sprites, bullet_pl_sprites, True, True)
        for bullet in bullet_n_bullet:
            explosion = decoration.Explosion(bullet.rect.center, (61, 21, 6, 8), ((61, 21, 6, 8), (61, 21, 6, 8)), 300, (15, 24))
            all_sprites.add(explosion)
        
        
        bullet_n_shield = pygame.sprite.groupcollide(bullet_sprites, shield_sprites, False, False)
        for bullet in bullet_n_shield:
            explosion = decoration.Explosion(bullet.rect.center, (61, 21, 6, 8), ((61, 21, 6, 8), (61, 21, 6, 8)), 300, (15, 24))
            all_sprites.add(explosion)
            
            
    def update(self):
        self.Animation_N_Movement()
    
        self.Dead()
    
        self.rect.y += 5


class Score_Part(decoration.Decoration_part):
    def __init__(self, pos, pos_x):
        decoration.Decoration_part.__init__(self, 0, 57, 62, "s")
        self.pos = pos
        self.pos_x = pos_x
    
    def update(self):
        local_score = str(score)
        if len(local_score) == 1:
            local_score = "000"+local_score
            
        if len(local_score) == 2:
            local_score = "00"+local_score
            
        if len(local_score) == 3:
            local_score = "0"+local_score
            
        v = list()
        for n in local_score:
            if n == "0":
                n = 26
            if n == "1":
                n = 27
            if n == "2":
                n = 28
            if n == "3":
                n = 29
            if n == "4":
                n = 30
            if n == "5":
                n = 31
            if n == "6":
                n = 32
            if n == "7":
                n = 33
            if n == "8":
                n = 34
            if n == "9":
                n = 35
            
            v.append(n)
            
        local_score = v
        
        self.sheet.set_clip(pygame.Rect(self.symbol_sheet[local_score[self.pos]]+(8, 8)))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (18, 24))
        
        self.rect.x = self.pos_x


def Score():
    x = 57
    for n in range(4):
        score_a = Score_Part(n, x)
        all_sprites.add(score_a)
        x += 18


def Restart_Score():
    global score
    score = 0


def Hi_Score():
    global score_list
    score_list.append(score)
    
    score_list = sorted(score_list)
    score_list = score_list[::-1]

    if len(str(score_list[0])) == 1:
        #print("000" + str(score_list[0]))
        return "000" + str(score_list[0])
        
    if len(str(score_list[0])) == 2:
        #print("00" + str(score_list[0]))
        return "00" + str(score_list[0])
        
    if len(str(score_list[0])) == 3:
        #print("0" + str(score_list[0]))
        return "0" + str(score_list[0])
        
    if len(str(score_list[0])) == 4:
        return str(score_list[0])
        
    else:
        return "ERROR"


def rev():
    pass
        

   