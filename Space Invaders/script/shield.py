#Fabian Santiago 2020

import pygame
from pygame.locals import *
from script import resources
pygame.init()

Texture_pack = resources.sprite_sheet

def init(all_sprites1, shield_sprites1, bullet_sprites1):
    global all_sprites
    global shield_sprites
    global bullet_sprites
    
    all_sprites = all_sprites1
    shield_sprites = shield_sprites1
    bullet_sprites = bullet_sprites1
    

def Generate_Shield(pos_x, pos_y):                      # 6 = 15, 5 = 13     x*2.5  y*3
    sheet       = [ ( (87, 20, 6, 6), (93, 20, 6, 6), (99, 20, 6, 6), (105, 20, 6, 6) ), #15      
                    ( (91, 28, 5, 6), (96, 28, 5, 6), (101, 28, 5, 6), (106, 28, 5, 6) ), #13
                    ( (86, 36, 5, 6), (92, 36, 5, 6), (98, 36, 5, 6), (104, 36, 5, 6) ), #13
                    ( (84, 44, 6, 6), (91, 44, 6, 6), (98, 44, 6, 6), (105, 44, 6, 6) ), #15
                    ( (80, 52, 7, 4), (88, 52, 7, 4), (96, 52, 7, 4), (104, 52, 7, 4) ), 
                    ( (87, 57, 8, 4), (96, 57, 8, 4), (87, 62, 8, 4), (96, 62, 8, 4) )]
    
    sprite_list = (sheet[0], sheet[2], sheet[3], sheet[1], 
                   sheet[3], sheet[2], sheet[3], sheet[2],
                   sheet[4],                     sheet[5])
    
    scale_width = 15
    scale_height = 18
                   
    posicion_list = ( (pos_x, pos_y), (pos_x+15, pos_y), (pos_x+28, pos_y), (pos_x+43, pos_y), 
                      (pos_x, pos_y+18), (pos_x+15, pos_y+18), (pos_x+28, pos_y+18), (pos_x+43, pos_y+18),
                      (pos_x, pos_y+36), (pos_x+36, pos_y+36) )
    
    for n in range(10):
        if sprite_list[n] == sheet[0]:
            scale_width = 15
            scale_height = 18
            
        if sprite_list[n] == sheet[1]:
            scale_width = 13
            scale_height = 18
            
        if sprite_list[n] == sheet[2]:
            scale_width = 13
            scale_height = 18
            
        if sprite_list[n] == sheet[3]:
            scale_width = 15
            scale_height = 18
            
        if sprite_list[n] == sheet[4]:
            scale_width = 18
            scale_height = 12
            
        if sprite_list[n] == sheet[5]:
            scale_width = 20
            scale_height = 12
            
        shield_part = Shield_Part(sprite_list[n],
                                  (scale_width, scale_height),           
                                  posicion_list[n][0], posicion_list[n][1] )
                                  
        all_sprites.add(shield_part)
        shield_sprites.add(shield_part)


class Shield_Part(pygame.sprite.Sprite): # Una de la parte de el escudo
    def __init__(self, textute_list, img_scale, x, y):
        super().__init__()
        self.textute_list = textute_list
        
        self.img_scale = img_scale
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.textute_list[0]))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (self.img_scale)) # x*2.5    y*3
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.live = 4
        
        
        
    def update(self):
        collide_list = pygame.sprite.groupcollide(shield_sprites, bullet_sprites, False, True)
        for collide in collide_list:
            collide.live -= 1
               
        if self.live == 3:
            self.sheet.set_clip(pygame.Rect(self.textute_list[1]))  # x, y, ancho+1, alto+1
     
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image.set_colorkey((0, 0, 0))
            
            self.image = pygame.transform.scale(self.image, (self.img_scale)) # x*2.5    y*3
            
            
        if self.live == 2:
            self.sheet.set_clip(pygame.Rect(self.textute_list[2]))  # x, y, ancho+1, alto+1
     
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image.set_colorkey((0, 0, 0))
            
            self.image = pygame.transform.scale(self.image, (self.img_scale)) # x*2.5    y*3
            
            
        if self.live == 1:
            self.sheet.set_clip(pygame.Rect(self.textute_list[3]))  # x, y, ancho+1, alto+1
     
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image.set_colorkey((0, 0, 0))
            
            self.image = pygame.transform.scale(self.image, (self.img_scale)) # x*2.5    y*3
            
            
        if self.live <= 0:
            self.kill()
