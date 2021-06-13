#Fabian Santiago 2020

import pygame
from pygame.locals import *
from script import decoration, resources
pygame.init()

Texture_pack = resources.sprite_sheet
#Texturas y Sonidos\fastinvader1.wav.reapeaks

Shoot_Sound = resources.Shoot_Sound
Pl_Dead_Sound = resources.Pl_Dead_Sound

live = 3
explosion_sprites = pygame.sprite.Group()

def init(all_sprites1, bullet_sprites1, bullet_pl_sprites1, bullet_en_sprites1, pl_sprites1, shield_sprites1):
    global all_sprites
    global bullet_sprites
    global bullet_pl_sprites
    global bullet_en_sprites
    global pl_sprites
    global shield_sprites
    
    all_sprites = all_sprites1
    bullet_sprites =  bullet_sprites1
    bullet_pl_sprites = bullet_pl_sprites1
    bullet_en_sprites = bullet_en_sprites1
    pl_sprites = pl_sprites1
    shield_sprites = shield_sprites1


class Player():
    def __init__(self):
        global player
        player = _Player_()
        all_sprites.add(player)
        pl_sprites.add(player)
        
    def Handle(self, event):
        player.Hadle(event)
        
    def Restart_live(self):
        global live
        live = 3
        
    def Live_0(self):
        global live
        if live <= 0:
            return True


class _Player_(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #13
        decoration.init(all_sprites, all_sprites)
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(1, 49, 16, 8))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (40, 24))
        
        self.rect = self.image.get_rect()
        
        self.speed_X = 0
        
        self.rect.x = 80
        self.rect.y = 574
        
        self.live = 3
        self.pause = False

    def Dead(self):
        global live
    
        player_n_bullet = pygame.sprite.groupcollide(pl_sprites, bullet_en_sprites, False, True)
        for collide in player_n_bullet:
            live -= 1
            self.pause = True
            Pl_Dead_Sound.play()
            Pl_Dead_Sound.set_volume(0.1)
            explosion = decoration.Explosion(self.rect.center, (19, 49, 16, 8), 
            ((19, 49, 16, 8), (37, 49, 16, 8), (19, 49, 16, 8), (37, 49, 16, 8), (19, 49, 16, 8), (37, 49, 16, 8), (19, 49, 16, 8), (37, 49, 16, 8),
             (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1), 
             (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1), (19, 49, 1, 1)),
            100, (40, 24))
            
            all_sprites.add(explosion)
            explosion_sprites.add(explosion)
            self.rect.y = 688
            
            if live == 2:
                decoration.Kill_Identifier("player_live_deco2")
                
            if live == 1:
                decoration.Kill_Identifier("player_live_deco1")

    
    def Shoot(self):
        if len(bullet_pl_sprites) == 0:
            if self.rect.y < 688:
                Shoot_Sound.play()
                Shoot_Sound.set_volume(0.1)
                bullet = Pl_Bullet(self.rect.center)
                all_sprites.add(bullet)
                
                bullet_pl_sprites.add(bullet)
                bullet_sprites.add(bullet)
                
            
    # def Debug_shoot(self):
        # bullet = En_Bullet(self.rect.center, 0, random.randrange(0, 3))
        # all_sprites.add(bullet)
        
        # all_bullet.add(bullet)
        # en_bullet.add(bullet)
        

    
    def Hadle(self, event):    
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_a:
                self.speed_X += -5
                
            if event.key == pygame.K_d:
                self.speed_X += 5
                
            if event.key == pygame.K_k:
                if self.pause == False:
                    self.Shoot()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.speed_X += 5
                
            if event.key == pygame.K_d:
                self.speed_X += -5
            
                
    def update(self):
        global live
    
        self.Dead()
    
        self.rect.x += self.speed_X

        
        if self.rect.x <= 9:
            self.rect.x = 9
            
        if self.rect.x >= 472:
            self.rect.x = 472
        
        if self.pause == True:
            if len(explosion_sprites) == 0:
                if live > 0:
                    self.pause = False
                    self.rect.x = 80
                    self.rect.y = 574
 

class Pl_Bullet(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(55, 53, 1, 4))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (3, 12))
        
        self.rect = self.image.get_rect()
        
        self.rect.center =  center
        
        self.speed_Y = -10
        
        self.INIT_P_Y = 96
        
    
    def Dead(self):
        if self.rect.y <= 100:
            self.kill()
            explosion = decoration.Explosion(self.rect.center, (58, 49, 8, 8), ((58, 49, 8, 8), (58, 49, 8, 8)), 300, (18, 24))
            all_sprites.add(explosion)
            
        if self.rect.y >= 688:
            self.kill()
            
            
        shield_n_bullet = pygame.sprite.groupcollide(bullet_pl_sprites, shield_sprites, False, False)
        
        for bullet in shield_n_bullet:
            explosion = decoration.Explosion(self.rect.center, (58, 49, 8, 8), ((58, 49, 8, 8), (58, 49, 8, 8)), 300, (18, 24))
            all_sprites.add(explosion)
        
        
    
    def update(self):
        self.rect.y += self.speed_Y
        
        self.Dead()

 
class P_Live_Co_part1(decoration.Decoration_part):
    def __init__(self):
        decoration.Decoration_part.__init__(self, 0, 20, 636, "l")
  
    def update(self):
        local_score = str(live)
        
        local_score = "0" + local_score
            
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
        
        try:
            self.sheet.set_clip(pygame.Rect(self.symbol_sheet[local_score[1]]+(8, 8)))  # x, y, ancho+1, alto+1
            
        except:
            self.sheet.set_clip(pygame.Rect(self.symbol_sheet[26]+(8, 8)))
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (18, 24))


def Live_Display():
    live_n = P_Live_Co_part1()
    all_sprites.add(live_n)
    

def Live_Decoration():
    decoration.Generate_Decoration("#", 60, 635, "player_live_deco1")
    decoration.Generate_Decoration("#", 98, 635, "player_live_deco2")

  
class Stop(object):
    def __init__(self):
        self.x = player.rect.x 
    
    def stop(self):
        decoration.Generate_Decoration("#", self.x, 574, "player")
        player.rect.y = 698
        
    def play(self):
        decoration.Kill_Identifier("player")
        player.rect.x = self.x
        player.rect.y = 574
