# Fabian Santiago 2020
# 24 jun / 11 jul

import pygame
from pygame.locals import *
from script import decoration, player, shield, enemy

all_sprites = pygame.sprite.Group()
shield_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
bullet_pl_sprites = pygame.sprite.Group()
bullet_en_sprites = pygame.sprite.Group()
Decoration_sprites = pygame.sprite.Group()
pl_sprites = pygame.sprite.Group()


class Game(object):
    def __init__(self):
        self.hi_score = "0000"

        player.init(all_sprites, bullet_sprites, bullet_pl_sprites, bullet_en_sprites, pl_sprites, shield_sprites)
        shield.init(all_sprites, shield_sprites, bullet_sprites)

        self.game_phase = 0
        
        self.Intro_1()
        #self.rev = False
        self.pause = False
        
        
    def Generate_Enemy(self):
        global enemy_pos
        global limit_in_l
        global limit_in_r
        limit_in_l = 0
        limit_in_r = 0

        enemy_pos = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
        
        
        enemy.init(all_sprites, enemy_sprites, bullet_sprites, bullet_pl_sprites, limit_in_l, limit_in_r, enemy_pos, shield_sprites, bullet_en_sprites, pl_sprites)
        
        enemy.Generate_Enemy(60, self.enemy_y[0], 10, self.enemy_y, self.bullet_probl)
        pygame.time.wait(180)
        enemy.Generate_Enemy(60, self.enemy_y[1], 10, self.enemy_y, self.bullet_probl)
        pygame.time.wait(180)
        enemy.Generate_Enemy(60, self.enemy_y[2], 20, self.enemy_y, self.bullet_probl)
        pygame.time.wait(180)
        enemy.Generate_Enemy(60, self.enemy_y[3], 20, self.enemy_y, self.bullet_probl)
        pygame.time.wait(180)
        enemy.Generate_Enemy(60, self.enemy_y[4], 30, self.enemy_y, self.bullet_probl)
        
        if self.rev == True:
            enemy.Score()
            
            
       
        sound_enemy = enemy.Sound_Enemy()
        all_sprites.add(sound_enemy)

  
    def Generate_Shield(self):
        for shield_ in shield_sprites:
            shield_.kill()
    
        shield.Generate_Shield(72, 507)
        shield.Generate_Shield(179, 507)
        shield.Generate_Shield(286, 507)
        shield.Generate_Shield(393, 507)


    def Intro_1(self):
        for sprite in all_sprites:
            sprite.kill()
    
        decoration.init(all_sprites, Decoration_sprites)
        decoration.Generate_Decoration("score<1>", 20, 20, "0") # El "0" nunca se quita
        decoration.Generate_Decoration("hi-score", 186, 20, "0")
        decoration.Generate_Decoration(" v 3*6  ", 352, 20, "0")
        decoration.Generate_Decoration(self.hi_score, 204, 62, "hi-score") # El "0" nunca se quita
        
        decoration.Generate_Decoration("credit", 351, 636, "0")
        decoration.Generate_Decoration("00", 471, 636, "0")
        
        self.Intro_2()

  
    def Intro_2(self):
        self.game_phase = 2
        self.rev = False
        self.key = False
        #[333, 291, 249, 207, 165]
        self.enemy_y = [291, 249, 207, 165, 123]
        self.down_count = 4
        self.bullet_probl = 5
        
        self.chronometer2 = decoration.Chronometer(9344)
        Decoration_sprites.add(self.chronometer2)
    
        decoration.Kill_Identifier("Intro_1")
    
        decoration.Generate_Decoration("0000", 56, 62, "Intro_2") # El "0" nunca se quita
        
    
        decoration.Write_Message("play", 222, 168, 18, 0, 112, "Intro_2")
        decoration.Write_Message("    space  invaders", 60, 230, 18, 0, 112, "Intro_2")
        decoration.Write_Message("*score advance table*", 78, 314, 378, 0, 2576, "Intro_2")
      
        
        decoration.Write_Message("                     =? mystery", -192, 356, 18, 0, 112, "Intro_2")
        decoration.Write_Message("                               =30 points", -372, 398, 18, 0, 112, "Intro_2")
        decoration.Write_Message("                                         =20 points", -552, 440, 18, 0, 112, "Intro_2")
        decoration.Write_Message("                                                   =10 points", -732, 482, 18, 0, 112, "Intro_2")
        
        decoration.Write_Message("$", 150, 356, -40, 0, 2576, "Intro_2")
        decoration.Write_Message("%", 158, 398, -38, 0, 2576, "Intro_2")
        decoration.Write_Message("&", 155, 440, -38, 0, 2576, "Intro_2")
        decoration.Write_Message("!", 152, 482, -38, 0, 2576, "Intro_2")


    def Intro_3(self):
        self.game_phase = 3
        self.chronometer3 = decoration.Chronometer(6050)
        Decoration_sprites.add(self.chronometer3)
    
        decoration.Kill_Identifier("Intro_2")
        
        decoration.Generate_Decoration("0000", 56, 62, "Intro_3") # El "0" nunca se quita
        
        decoration.Write_Message("-k button to shoot-", 86, 262, 18, 0, 90, "Intro_3")
        decoration.Write_Message("                   *a and d button to move*", -292, 314, 18, 0, 90, "Intro_3")


    def Intro_4(self):
        self.game_phase = 4
        self.chronometer4 = decoration.Chronometer(2520)
        Decoration_sprites.add(self.chronometer4)
    
        decoration.Kill_Identifier("Intro_3")
        
        decoration.Flicker_Message("0000", 56, 62, 0, 24, 80, "Intro_4") # El "0" nunca se quita
        
        decoration.Write_Message("play player<1>", 128, 270, 18, 0, 90, "Intro_4")

  
    def Game_intro(self):
        self.chronometer5 = decoration.Chronometer(1300)
        Decoration_sprites.add(self.chronometer5)
        
        self.stop = player.Stop()
        self.stop.stop()
    
        self.game_phase = 5
        
        if self.down_count > 0:
            for n in range(5):
                self.enemy_y[n] += 42
                
        self.bullet_probl += 4
            
        self.down_count -= 1
        
        
        decoration.Kill_Identifier("Intro_4")
       
        if self.rev == False:
            decoration.Generate_Decoration("0000", 56, 62, "Intro_5") # El "0" nunca se quita
        
        decoration.Write_Message("!!!!!!!!!!!", 60, self.enemy_y[0], 38, 0, 10, "Intro_5")
        decoration.Write_Message("           !!!!!!!!!!!", -358, self.enemy_y[1], 38, 0, 10, "Intro_5")
        decoration.Write_Message("                      +++++++++++", -776, self.enemy_y[2], 38, 0, 10, "Intro_5")
        decoration.Write_Message("                                 +++++++++++", -1194, self.enemy_y[3], 38, 0, 10, "Intro_5")
        decoration.Write_Message("                                            %%%%%%%%%%%", -1612, self.enemy_y[4], 38, 0, 10, "Intro_5")
        
        player.Live_Decoration()
        self.player.Restart_live()


    def Game_Start(self):
        self.game_phase = 6
        self.rev = True
        self.player =  player.Player()
        player.Live_Display()
        player.Live_Decoration()
        

    def Game_Over(self):
        self.game_phase = 7
        self.hi_score = enemy.Hi_Score()
        
        self.chronometer7 = decoration.Chronometer(5000)
        Decoration_sprites.add(self.chronometer7)
        
        decoration.Kill_Identifier("hi-score")
            
        decoration.Generate_Decoration(self.hi_score, 204, 62, "h") # El "0" nunca se quita
        
        decoration.Kill_Identifier("Game_Start")
        
        decoration.Write_Message("  Game Over  ", 168, 124, 18, 0, 117, "Game_Over")
    

    def process_events(self, display):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                return True
            
            
            try:
                self.player.Handle(event)
                
            except:
                pass
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_phase == 2:
                        if self.key == True:
                            self.Intro_3()

                if self.game_phase == 6 and event.key == pygame.K_RETURN:
                    self.pause = not self.pause

            if event.type == pygame.VIDEORESIZE:
                display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)


    def run_logic(self):
        if not self.pause:
            all_sprites.update()
        if self.game_phase == 2:
            if self.chronometer2.Play():
                decoration.Flicker_Message("     press space     ", 78, 564, 0, 24, 122, "Intro_2")
                self.key = True
                
        
        if self.game_phase == 3:
            if self.chronometer3.Play():
                self.Intro_4()
                
        if self.game_phase == 4:
            if self.chronometer4.Play():
                self.Game_Start()
                
        if self.game_phase == 5:
            if self.chronometer5.Play():
                self.Generate_Enemy()
                self.game_phase = 6
                decoration.Kill_Identifier("Intro_5")
                self.stop.play()
                
        if self.game_phase == 6:
            if len(enemy_sprites) == 0:
                for bullet in bullet_sprites:
                    bullet.kill()
                self.Generate_Shield()
                self.Game_intro()
                
            if self.player.Live_0():
                self.Game_Over()
                
        if self.game_phase == 7:
            if self.chronometer7.Play():
                self.player.Restart_live()
                enemy.Restart_Score()
                self.Intro_1()

 
    def display_frame(self, display, screen):    
        screen.fill((0, 0, 0))
        
        all_sprites.draw(screen)
        
        if self.game_phase == 5:
            pygame.draw.line(screen, (0, 255, 0), (0, 633), (520, 633), 3)
            
        if self.game_phase == 6:
            pygame.draw.line(screen, (0, 255, 0), (0, 633), (520, 633), 3)
            
        if self.game_phase == 7:
            pygame.draw.line(screen, (0, 255, 0), (0, 633), (520, 633), 3)

        pixels_per_unit = min(display.get_size()[0]/screen.get_size()[0], display.get_size()[1]/screen.get_size()[1])
        w = int(screen.get_size()[0]*pixels_per_unit)
        h = int(screen.get_size()[1]*pixels_per_unit)

        x = int(max((display.get_size()[0]-w)/2, 0))
        y = int(max((display.get_size()[1]-h)/2, 0))
        display.blit(pygame.transform.scale(screen, (w, h)), (x, y))
        
        pygame.display.flip()

def main():
    pygame.init()
    
    screen = pygame.Surface((520, 688))
    display = pygame.display.set_mode((260, 344), pygame.RESIZABLE)

    pygame.display.set_caption("SPACE INVADERS")
    clock = pygame.time.Clock()
    game = Game()
    
    done = False
    while not done:
        done = game.process_events(display)       
        game.run_logic()
        game.display_frame(display, screen)      
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
 
