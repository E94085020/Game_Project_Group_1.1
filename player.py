import pygame
import os
from setting import WIN_WIDTH,RED,GREEN,IMAGE_PATH,SOUND_PATH

pygame.init()
PLAYER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "1.png")),(150,200))
PLAYER_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "2.png")),(155,190))

class Player:
    def __init__(self):
        self.image_1=PLAYER_IMAGE
        self.image=self.image_1
        self.rect=self.image.get_rect()
        self.x=600 #玩家的初始位置
        self.y=550
        self.rect.center=(self.x,self.y)
        self.hp=100
        self.max_hp=100
        self.jumping=False#用於判斷玩家是否在跳躍中
        self.face_to_right=True
        self.jump_time=0
        self.down=False
    def draw(self, win):
        '''
        輸出玩家的血量與圖像
        '''
        win.blit(self.image,self.rect)
        pygame.draw.rect(win,GREEN,[450,20,3*self.hp,20])
        pygame.draw.rect(win,RED,[450+3*self.hp,20,3*(self.max_hp-self.hp),20])
    def is_jumping(self): #進行跳躍的function
        '''
        跳躍的總時間為51幀
        前半段時間位置會逐漸升高
        後半段時間位置逐漸降低
        '''
        if(self.jumping):
            if(self.jump_time<=25):
                self.rect.centery-=4   
            else:
                self.rect.centery+=4
            self.jump_time+=1    
            if(self.jump_time==51):
                self.jumping = False
                self.jump_time=0 #跳躍完成后重置跳躍時間
    def is_down(self,down):#判斷是否為蹲下
        if(self.jumping==False): 
            if down:
                self.rect.centery=580
                self.image_1=PLAYER_IMAGE_2
            else:
                self.rect.centery=550
                self.image_1=PLAYER_IMAGE
                
    def face_to(self):#判斷玩家當前的面朝向，會跟換圖像
        if (self.face_to_right):
            self.image=self.image_1
        else:
            self.image=pygame.transform.flip(self.image_1,True,False)



class Player_action:  # 控制玩家的動作
    def __init__(self):
        self.down = False
        self.player = Player()
        self.using_mask=None

    def update(self):
        if self.using_mask is not None:
            self.using_mask.use()
            if self.using_mask.is_active()==False:
                self.using_mask=None
        self.player.face_to()
        self.player.is_down(self.down)
        self.player.is_jumping()

    def draw(self, win):
        if self.using_mask is not None:
            self.using_mask.draw(win)        
        self.player.draw(win)

    def move_L(self):  # 往左移動
        if (self.player.rect.centerx >= 10):
            self.player.rect.centerx -=2

    def move_R(self):  # 往右移動
        if (self.player.rect.centerx <= WIN_WIDTH - 10):
            self.player.rect.centerx +=2

    def jump(self):  # 跳躍
        self.player.jumping = True

    def turn_R(self):  # turn_R,turn_l可改變面朝向，但很少用
        self.player.face_to_right = True

    def turn_L(self):
        self.player.face_to_right = False

    def shot(self, x):# 射擊時會改變面朝向
        if ((x - self.player.rect.centerx) >= 0):
            self.player.face_to_right = True
        else:
            self.player.face_to_right = False
            
    def get_attack(self,virus_pos): #判斷玩家是否收到病毒攻擊，virus_pos為病毒的位置
        if self.player.rect.collidepoint(virus_pos):
            return True
        else:
            return False    
            
    def get_hurt(self,dmg):
        if self.using_mask is not None:
            self.player.hp-=self.using_mask.defense(dmg)
        else:    
            self.player.hp-=dmg#根據病毒傷害扣除血量
    
    def get_pos_x(self):
        return self.player.rect.centerx
    
    def get_pos_y(self):
        return self.player.rect.centery
    
    def use_mask(self,mask):
        self.using_mask=mask
        
    def heal(self,hp):
        self.player.hp+=hp
        if self.player.hp>100:
            self.player.hp=100
    
    def get(self):
        return self.player
    