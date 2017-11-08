import pygame
import sys
import math
from pygame.locals import*
from random import*
import traceback



class Shell(pygame.sprite.Sprite):
    def __init__(self,image,speed_x,speed_y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = speed_x,speed_y
        


def jiasudu(g,m,speed_x,speed_y,fengsu_x,fengsu_y,zizhuan):
    sulv = math.sqrt(math.pow(speed_x,2)+math.pow(speed_y,2))
    
    B2 = m*(0.0039+(0.0058/(1+math.exp((sulv-35)/5))))
    F_dragx = -B2*math.sqrt(\
        math.pow(speed_x - fengsu_x,2)+math.pow(speed_y - fengsu_y,2))\
                            *(speed_x - fengsu_x)
    
    F_dragy= -B2*math.sqrt(\
        math.pow(speed_x - fengsu_x,2)+math.pow(speed_y - fengsu_y,2))\
                            *(speed_y - fengsu_y)
                            
       
    jiasudu_x =F_dragx/m
    
        
    jiasudu_y =F_dragy/m-g
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    return jiasudu_x,jiasudu_y


def main():
    pygame.init()
    shell_image = "images/shell.png"
    bg_image = "images/bg.png"
    pao_image = "images/pao.png"  
    lan_image = "images/lan.png"
    win_image = "images/WIN.png"
    dang_image = "images/dang.png"
    bg_size = width,height = 1000,700
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("shell")
    backgrand = pygame.image.load(bg_image).convert_alpha()
    pao = pygame.image.load(pao_image).convert_alpha()
    lan = pygame.image.load(lan_image).convert_alpha() 
    win = pygame.image.load(win_image).convert_alpha()
    dang = pygame.image.load(dang_image).convert_alpha()
    clock = pygame.time.Clock()

    
    running = True
    position = [45,623]
    m = 0.149
    g =9.8
    zizhuan =100 
    dt =0.04
    speed_x,speed_y = 0,0         
    fengsu_x,fengsu_y = [randint(-15,15),randint(-10,10)]
    a=False             
    b = True
    c=False
    
    
    
    
    while running:
        screen.blit(backgrand,(0,0))
        screen.blit(pao,(25,529))
        screen.blit(lan,(700,531))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN: 
                m_position = pygame.mouse.get_pos()
                
                speed_x,speed_y =m_position[0]*0.8,700-m_position[1]
                a = not a 
                b = not b
        if a:   
            jiasudu_x ,jiasudu_y =jiasudu(g,m,speed_x,speed_y,fengsu_x,fengsu_y,zizhuan)   
            
            speed_x = speed_x +jiasudu_x*dt
            speed_y = speed_y +jiasudu_y*dt
           
            shell =Shell(shell_image,speed_x,speed_y,position)    
            screen.blit(shell.image,shell.rect)
            
       
            if 680<position[0]<830  and  531<position[1]<700:
                screen.blit(win,(250,300))
                c = not c
                
                
            if 675<position[0]<678 and   529<position[1]<700:
                screen.blit(dang,(678,531))
                speed_x = -speed_x
                
            
            if 114<position[0]<253 and 144<position[1]<146 and speed_y > 0:
                speed_y =  - speed_y
            
            if 360<position[0]<588 and 258<position[1]<260 and speed_y > 0:
                speed_y = -speed_y
                
        if b:
            fengsu_x,fengsu_y = [randint(-15,15),randint(-10,10)]
            speed_x,speed_y = 0,0
            position = [45,623]            
        if c:
            shell.speed = 0,0
            running = False
        
            
        if position[1] > 623:
            position = position
           

        else:
            position = [position[0]+speed_x*dt,position[1]-speed_y*dt]
        
        pygame.display.flip()    
        clock.tick(80)
        while not running:
            pygame.time.delay(3000)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
   
    
    
if __name__ == "__main__" :
    try:
        main()
        
    except SystemExit:
        pass
    except :
        traceback.print_exc()
        pygame.quit()
        input()
        