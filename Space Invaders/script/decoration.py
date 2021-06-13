#Fabian Santiago 2020

import pygame, datetime
from pygame.locals import *
from script import resources
pygame.init()

Texture_pack = resources.sprite_sheet

def init(all_sprites1, decoration_sprites1):
    global all_sprites
    global Decoration_sprites
    
    all_sprites = all_sprites1
    Decoration_sprites = decoration_sprites1


def Generate_Decoration(message, x, y, identifier):
    message = message.lower()
    banned_characters = [".", ",", '"', "/", "(", ")", "\\", "'", "¿", "¡", "|", "°", "¬", "´", "¨", "~", "{", "[", "^", "}", "]", "`", "_"]
    space = 18
    
    for banned in banned_characters:
        message = message.replace(banned, "")
        
    
    letters = list()
    for n in message:
        if n == "a":
            n = 0
        if n == "b":
            n = 1
        if n == "c":
            n = 2
        if n == "d":
            n = 3
        if n == "e":
            n = 4
        if n == "f":    
            n = 5
        if n == "g":
            n = 6
        if n == "h":
            n = 7
        if n == "i":
            n = 8
        if n == "j":
            n = 9
        if n == "k":
            n = 10
        if n == "l":
            n = 11
        if n == "m":
            n = 12
        if n == "n":
            n = 13
        if n == "o":
            n = 14
        if n == "p":
            n = 15
        if n == "q":
            n = 16
        if n == "r":
            n = 17
        if n == "s":
            n = 18
        if n == "t":
            n = 19
        if n == "u":
            n = 20
        if n == "v":
            n = 21
        if n == "w":
            n = 22
        if n == "x":
            n = 23
        if n == "y":
            n = 24
        if n == "z":
            n = 25
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
        if n == "<":
            n = 36
        if n == ">":
            n = 37
        if n == "=":
            n = 38
        if n == "*":
            n = 39
        if n == "?":
            n = 40
        if n == "-":
            n = 41
        if n == " ":
            n = 42
            
        #"#", "$", "%", "&", "!", 
        
        if n == "#":
            n = 43    
        if n == "$":
            n = 44      
        if n == "%":
            n = 45
            space = 38
        if n == "&":
            n = 46
            space = 38
        if n == "!":
            n = 47
            space = 38
        if n == "+":
            n = 48
            space = 38
        letters.append(n)

    message = letters
    
    for letter in message:
        Decoration_letter = Decoration_part(letter, x, y, identifier)
        all_sprites.add(Decoration_letter)
        Decoration_sprites.add(Decoration_letter)
        x += space


def Kill_Identifier(identifier):
    # kill_identifier = pygame.sprite.groupcollide(Decoration_sprites, Decoration_sprites, False, False)
    # for kill in kill_identifier:
        # try:
            # if kill.identifier == identifier:
                # kill.kill()
        
        # except:
            # pass
            
    for decoration in Decoration_sprites:
        try:
            if decoration.identifier == identifier:
                decoration.kill()
                
        except:
            pass


def Kill_All_Decoration():    
    pygame.sprite.groupcollide(Decoration_sprites, Decoration_sprites, True, True)
  
  
class Decoration_part(pygame.sprite.Sprite): 
    def __init__(self, symbol, x, y, identifier):
        super().__init__()
        self.identifier = identifier
        
        self.symbol = symbol
        
        if self.symbol <= 42:
            self.wh = (8, 8)
            self.conv = (18, 24)
        
        if self.symbol == 43:
            self.wh = (16, 8)
            self.conv = (40, 24)
            
        if self.symbol == 44:
            self.wh = (16, 8)
            self.conv = (40, 24)
        
        if self.symbol == 45:
            self.wh = (8, 8)
            self.conv = (21, 24)
        
        if self.symbol == 46:
            self.wh = (11, 8)
            self.conv = (27, 24)
        
        if self.symbol == 47:
            self.wh = (12, 8)
            self.conv = (30, 24)
            
        if self.symbol == 48:
            self.wh = (11, 8)
            self.conv = (27, 24)
        
        
                        #      A         B         C          D         E         F         G         H
        self.symbol_sheet = [(1, 69), (11, 69), (21, 69), (31, 69), (41, 69), (51, 69), (61, 69), (71, 69), 
        
                        # I         J          k          L        M         N         O         P
                        (1, 79), (11, 79), (21, 79), (31, 79), (41, 79), (51, 79), (61, 79), (71, 79),
                        
                        # Q         R          S          T         U        V         W        X
                        (1, 89), (11, 89), (21, 89), (31, 89), (41, 89), (51, 89), (61, 89), (71, 89),
                        
                        # Y         Z         0          1        2         3         4          5        
                        (1, 99), (11, 99), (21, 99), (31, 99), (41, 99), (51, 99), (61, 99), (71, 99),
                        
                        # 6           7         8           9          <          >          =          *
                        (1, 109), (11, 109), (21, 109), (31, 109), (41, 109), (51, 109), (61, 109), (71, 109),
                        
                        # ?           -        space     player   rand     en30     en20     en10
                        (1, 119), (11, 119), (21, 119), (1, 49), (1, 39), (5, 1), (22, 11), (39, 1), (22, 1)]
                          
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(self.symbol_sheet[self.symbol]+self.wh))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, self.conv)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y


class Explosion(pygame.sprite.Sprite): 
    def __init__(self, center, IMG_BASE, IMG_SPRITES, frame_rate, CONV):
        super().__init__()
        self.CONV = CONV
        
        self.sheet = pygame.image.load(Texture_pack).convert() #La imagen base
        self.sheet.set_clip(pygame.Rect(IMG_BASE)) #indicando la posicion de la nave en la imagen
        
        self.image = self.sheet.subsurface(self.sheet.get_clip()) #Obteniendo la posicion
        self.image.set_colorkey((000, 000, 000)) #Retirando el negro
        
        self.image =  pygame.transform.scale(self.image, self.CONV)
        
        self.rect = self.image.get_rect()
        
        self.explosition_sprites = IMG_SPRITES
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = frame_rate
        
        self.rect.center = center
        
        self.IMG_BASE = IMG_BASE
        

    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosition_sprites):
                self.kill()
                
                
            else:
                self.sheet.set_clip(pygame.Rect(self.explosition_sprites[self.frame]))
                        
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((000, 000, 000))  
                
                self.image =  pygame.transform.scale(self.image, self.CONV)
           
    def update(self):
        self.Animation()
    

class Chronometer(pygame.sprite.Sprite):
    def __init__(self, frame_rate):
        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(1, 119, 8, 8))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.image = pygame.transform.scale(self.image, (18, 24))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 0
        
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = frame_rate
        
        
    def Play(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.kill()
            return True


class Black_Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, large, speed_X, speed_Y, frame_rate, identifier):
        super().__init__()
        self.identifier = identifier
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(21, 119, 8, 8))  # x, y, ancho+1, alto
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.image = pygame.transform.scale(self.image, large)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.speed_X = speed_X
        self.speed_Y = speed_Y

        
          
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = frame_rate
        
    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
        
            self.rect.x += self.speed_X #El movimiemto va acorde la animación 
            self.rect.y += self.speed_Y
            self.last_update = now
            
            
        
    def update(self): 
        self.Animation()

    
class Black_Rect_flicker(pygame.sprite.Sprite):
    def __init__(self, x, y, large, speed_X, speed_Y, frame_rate, identifier):
        self.identifier = identifier
        self.INIT_P_Y = y
    
        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(21, 119, 8, 8))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.image = pygame.transform.scale(self.image, large)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.speed_X = speed_X
        self.speed_Y = speed_Y
        
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = frame_rate
        
        
    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
                
            self.rect.x += self.speed_X
            self.rect.y += self.speed_Y
            
            self.speed_Y *= -1

           
    def update(self):
        self.Animation()


def Write_Message(message, x, y, speed_X, speed_Y, frame_rate, identifier):
    reazon = 18

    if "$" in message:
        reazon = 40
        
    if "%" in message:
        reazon = 38
        
    if "&" in message:
        reazon = 38
        
    if "+" in message:
        reazon = 38
        
    if "!" in message:
        reazon = 38
    
    Generate_Decoration(message, x, y, identifier)
    black = Black_Rect(x, y, (len(message)*reazon, 24), speed_X, speed_Y,frame_rate, identifier)
    all_sprites.add(black)
    Decoration_sprites.add(black)
    
    
def Flicker_Message(message, x, y, speed_X, speed_Y, frame_rate, identifier):
    Generate_Decoration(message, x, y, identifier)
    black = Black_Rect_flicker(x, y, (len(message)*18, 24), speed_X, speed_Y, frame_rate, identifier)
    all_sprites.add(black)
    Decoration_sprites.add(black)
    