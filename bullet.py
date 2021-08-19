from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
import os
from attack_strategy import *
from setting import IMAGE_PATH,SOUND_PATH
from math import *
if TYPE_CHECKING:
    from attack_strategy import AttackStrategy
HCLO_IMAGE=pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "hclo.png")), (25, 15))
ALCOHOL_IMAGE=pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "alcohol.png")), (150, 150))

class Bullet:
    def __init__(self,x:int,y:int,x2:int,y2:int, image, attack_strategy : AttackStrategy):
        self.speed=None #控制子彈移動的速度
        self.max_move=None#子彈的最大移動次數，用於控制移動距離
        self.dmg=None#子彈傷害
        self.del_x=None #del_x,del_y為子彈的向量數據
        self.del_y=None
        self.image=image
        self.attack_strategy = attack_strategy #子彈的攻擊模式
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.count_move=0
        self.bullet_del=False#用於刪除子彈

        
    @classmethod #次氯酸水
    def HCLO(cls,x,y,x2,y2):
        hclo=cls(x,y,x2,y2,HCLO_IMAGE,SingleAttack())
        hclo.speed=20
        hclo.max_move=20
        hclo.dmg=80
        hclo.del_x=round(hclo.speed*x2)
        hclo.del_y=round(hclo.speed*y2)       
        return hclo
    
    @classmethod #酒精
    def Alcohol(cls,x,y,x2,y2):
        alcohol = cls(x,y,x2,y2,ALCOHOL_IMAGE,AOE())
        alcohol.speed = 60
        alcohol.max_move = 10
        alcohol.dmg = 100
        alcohol.del_x=round(alcohol.speed*x2)
        alcohol.del_y=round(alcohol.speed*y2)             
        return alcohol    
                
    def draw(self,win):
        win.blit(self.image,self.rect)

    def move(self):
        '''
        控制子彈移動的function，在BulletGroup.update里呼叫
        '''
        self.rect.centerx+=self.del_x
        self.rect.centery+=self.del_y
        self.count_move+=1
        if (self.count_move>=self.max_move):
            self.bullet_del=True#當子彈達到最大移動次數時標記為可移除
    def attack(self,virus_group:list):
        '''
        根據子彈類型進行不同的攻擊方式
        '''
        self.attack_strategy.attack(virus_group,self)
    
    def del_bullet(self) -> bool:
        '''
        會在BulletGroup.update里呼叫，用於移除子彈
        '''
        if (self.bullet_del):
            return True
        else:
            return False
    
        
    
class BulletGroup:
        def __init__(self):
            self.__bullet=[]#保存畫面上的子彈所用的list
        
        def add(self,x,y,x2,y2):
            '''
            根據滑鼠和玩家的位置計算出發射的角度，再找出子彈的向量
            ''' 
            if((x2-x)!=0):           
                self.rad=atan((y2-y)/(x2-x))
                self.del_x=cos(self.rad)
                self.del_y=sin(self.rad)
                if((x2-x)<0):#因為cos（）和sin（）只計算出第一象限和第四象限的角度，所以當發射方向朝左時需把向量乘以-1
                    self.del_x*=-1
                    self.del_y*=-1
                self.bl=Bullet.HCLO(x,y,self.del_x,self.del_y)
                self.__bullet.append(self.bl)
        def alcohol_shot(self,x,y,x2,y2):#用於發射酒精彈藥
            if((x2-x)!=0):#以下邏輯與一般攻擊一樣
                self.rad=atan((y2-y)/(x2-x))
                self.del_x=cos(self.rad)
                self.del_y=sin(self.rad)
                if((x2-x)<0):
                    self.del_x*=-1
                    self.del_y*=-1
                self.bl=Bullet.Alcohol(x,y,self.del_x,self.del_y)        
                self.__bullet.append(self.bl)            
        def draw(self,win):     
            if(self.__bullet):        
                for bu in self.__bullet: #畫出子彈
                    bu.draw(win)                    
            
        def update(self,virusgroup : list):
            for bu in self.__bullet:
                bu.attack(virusgroup)
            if(self.__bullet):        
                for bu in self.__bullet:           
                    bu.move()
                    if(bu.del_bullet()==True):
                        self.__bullet.remove(bu)
        def get(self):
            return self.__bullet

