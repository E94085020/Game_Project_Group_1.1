import pygame
import os
from setting import IMAGE_PATH,SOUND_PATH
from defense_strategy import*

MASK = pygame.image.load(os.path.join(IMAGE_PATH, "mask.png"))
N95 =  pygame.image.load(os.path.join(IMAGE_PATH, "N95.png"))
VACCINE = pygame.image.load(os.path.join(IMAGE_PATH, "vaccine.png"))
    
class Not_activated:
    def use(self,player,bullet,virus):
        pass
    
    def draw(self,win):
        pass
    
    def update(self):
        pass
    
class Alcohol_atk:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 30)
        self.charged=1500#初期提供100%充能
        self.cd=30
        self.max_cd=30
        self.max_charger=1500
        self.charger_time=300#一發酒精子彈所需的充能時間
        self.count_bullet=5#當前酒精子彈的數量
    def cd_count(self):
        '''
        用於計算酒精攻擊的冷卻與及充能，在BUlletGroup.update里進行呼叫
        '''
        self.count_bullet=int(self.charged/self.charger_time)
        if(self.charged<self.max_charger):
            self.charged+=1
        if(self.cd<self.max_cd):
            self.cd+=1
 
    def draw(self,win):
        text = self.font.render(f"Alcohol: {self.count_bullet}", True, (255, 255, 255))
        win.blit(text, (5, 15))
        pygame.draw.rect(win, (255,255,255), [5, 50, (self.charged%self.charger_time)/3, 5])
        
    def use(self,player,bullet,virus):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player.shot(mouse_x)
        if(self.count_bullet!=0 and self.cd==self.max_cd):
         #先判斷酒精是否有彈藥和酒精攻擊是否在冷卻
            bullet.alcohol_shot(player.get_pos_x(),player.get_pos_y(),mouse_x,mouse_y)
            self.charged-=self.charger_time#重置充能時間
            self.cd=0#發射后進入冷卻
            for en in virus:
                en.pass_dmg=False
    
    def update(self):
        self.cd_count()

        
class HCLO:
    def use(self,player,bullet,virus):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player.shot(mouse_x)
        bullet.add(player.get_pos_x(),player.get_pos_y(),mouse_x,mouse_y)
        for en in virus:
            en.pass_dmg=False
    def update(self):
        pass
                                        
        
class Mask:
    def __init__(self):
        self.image=None
        self.used_time=0
        self.active_time=None
        self.active=True
        self.defense_tpye=None
    @classmethod 
    def N95(cls):
        n95=cls()
        n95.image=pygame.transform.scale(N95,(60,60))
        n95.active_time=5000
        n95.defense_tpye=A_lucky()
        return n95
    
    @classmethod 
    def surgical_mask(cls):
        surgicalmask=cls()
        surgicalmask.image=pygame.transform.scale(MASK,(80,80))
        surgicalmask.active_time=3500
        surgicalmask.defense_tpye=B_lucky()
        return surgicalmask
    
    def draw(self,win):
        win.blit(self.image,(360,0))
        pygame.draw.rect(win, (255,255,255), [450, 50, (self.active_time-self.used_time)/self.active_time*300, 5])
        
        
    def use(self):
        if self.used_time<=self.active_time:
            self.used_time+=1
        else: 
            self.active=False
    def defense(self,dmg):
         return self.defense_tpye.defense(dmg,self)
    
    def is_active(self):
        return self.active

class Vaccine:
    def __init__(self):
        self.image=pygame.transform.scale(VACCINE,(60,60))
        self.used_time=0
        self.active_time=2500
        self.cd=100
        self.heal_value=8
        self.active=True
        self.using=False
    def draw(self,win):
        win.blit(self.image,(760,8))
        #pygame.draw.rect(win, (255,255,255), [760, 45, (self.active_time-self.used_time)/self.active_time*40, 5]) 
    def update(self,player):
        if self.used_time <=self.active_time:
            if self.used_time%self.cd==0:
                player.heal(self.heal_value)
            self.used_time+=1
        else:
            self.active=False

        
        