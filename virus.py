import pygame
import math
import os
import random
from setting import WIN_WIDTH, WIN_HEIGHT, FPS,IMAGE_PATH,SOUND_PATH

virus_image = pygame.image.load(os.path.join(IMAGE_PATH, "virus.png"))
ultimate_virus_image = pygame.image.load(os.path.join(IMAGE_PATH, "ultimate virus.png"))

class Virus:
    def __init__(self):
        self.image = pygame.transform.scale(virus_image, (100, 100))
        self.rect = self.image.get_rect()
        self.health = 300
        self.max_health = 300
        self.dmg=10
        self.dx =None
        self.dy = None
        self.start = 1
        self.atk_cd=0
        self.atk_max_cd=60
        self.pass_dmg=False
    
    def move(self):
        """
        敵人移動路徑
        """
        if self.start == 1:
            self.dx = -2
            self.dy = random.randrange(-3,3,2)
            self.rect.centerx,self.rect.centery = (random.choice([0, WIN_WIDTH - 100]), random.randint(0, WIN_HEIGHT - 100))
            self.dx = random.randint(-4,4)
            self.dy = random.randint(-4,4)
            self.start = 0
        if self.rect.centerx >= WIN_WIDTH-100 :
            self.dx = random.randint(-4,-1)
        elif self.rect.centerx <= 0:
            self.dx = random.randint(1,4)
        if self.rect.centery >= WIN_HEIGHT-100 :
            self.dy = random.randint(-4,-1)
        elif self.rect.centery <= 200:
            self.dy = random.randint(1,4)
            
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        
    def is_cd(self):
        if self.atk_cd<self.atk_max_cd:
            self.atk_cd+=1
            return True
        else:
            return False
 
    def attack(self,player):
        if(player.get_attack(self.rect.center) and self.is_cd()==False):
            player.get_hurt(self.dmg)
            self.atk_cd=0
        
         
    def is_hitted(self,bullet_pos):
        if self.rect.collidepoint(bullet_pos):
            return True
        else:
            return False    
            
    def get_hurt(self,dmg):
        self.health-=dmg
        self.pass_dmg=True
        

    def draw(self, win):
        win.blit(self.image,self.rect)
        current_health_ratio = self.health / self.max_health
        pygame.draw.rect(win, (255, 0, 0), [self.rect.centerx -25 , self.rect.centery - 50, 65, 10])
        pygame.draw.rect(win, (0, 255, 0), [self.rect.centerx -25 , self.rect.centery - 50, 65 * current_health_ratio, 10])

class Ultvirus:
    def __init__(self):
        self.image = pygame.transform.scale(ultimate_virus_image, (500, 200))
        self.rect = self.image.get_rect()
        self.health = 500
        self.max_health = 500
        self.dmg = 30
        self.dx = None
        self.dy = None
        self.start = 1
        self.atk_cd = 0
        self.atk_max_cd=60
        self.shoot_cd = 0
        self.bullet_dx = -5
        self.pass_dmg = False
    
    def move(self):
        """
        敵人移動路徑
        """
        if self.start == 1:
            self.dx = random.choice([-5,5])
            self.dy = random.choice([-5,5])
            self.rect.centerx,self.rect.centery = (random.choice([0, WIN_WIDTH - 500]), random.randint(200, WIN_HEIGHT - 200))
            self.start = 0
        if self.rect.centerx >= WIN_WIDTH - 500:
            self.dx = -8
            
        if self.rect.centerx <= 0:
            self.dx = 8
            
        if self.rect.centery >= WIN_HEIGHT - 200:
            self.dy = -8
            
        if self.rect.centery <= 200 :
            self.dy = 8
            
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        
    def is_cd(self):
        if self.atk_cd<self.atk_max_cd:
            self.atk_cd+=1
            return True
        else:
            return False
        
    def shoot(self, x, y):
        if self.shoot_cd == 120:
            self.shoot_cd = 0
            
    def attack(self,player):
        if(player.get_attack(self.rect.center) and self.is_cd()==False):
            player.get_hurt(self.dmg)
            self.atk_cd=0
        
         
    def is_hitted(self,bullet_pos):
        if self.rect.collidepoint(bullet_pos):
            return True
        else:
            return False    
            
        self.self.shoot_cd += 1
    def get_hurt(self,dmg):
        self.health-=dmg
        self.pass_dmg=True
        

    def draw(self, win):
        win.blit(self.image,self.rect)
        current_health_ratio = self.health / self.max_health
        pygame.draw.rect(win, (255, 0, 0), [self.rect.centerx -25 , self.rect.centery - 100, 65, 10])
        pygame.draw.rect(win, (0, 255, 0), [self.rect.centerx -25 , self.rect.centery - 100, 65 * current_health_ratio, 10])
        
class Virusgroup:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 30)
        self.campaign_count = 0
        self.campaign_max_count = 30
        self.__reserved_members = []
        self.__expedition = []
        self.kill_amount = 0
        

    def draw(self, win,target):
        for en in self.__expedition:
            en.draw(win)
        if self.kill_amount < target:
            text = self.font.render(f"Kill: {self.kill_amount}/{target}", True, (255, 255, 255)) # 畫出擊殺病毒數量
            win.blit(text, (1000, 15))
        else:
            text_2 = self.font.render(f"Please clean the virus", True, (255, 255, 255))
            win.blit(text_2, (900, 15))   
            
    
    def campaign(self):
        """
        Enemy go on an expedition.
        """
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1        

    def add(self, num):
        """
        Generate the enemies for next wave
        """
        self.__reserved_members = [Virus() for _ in range(num)]
        
    def addult(self, num):
        self.__reserved_members = [Ultvirus() for _ in range(num)]

    def get(self):
        """
        Get the enemy list
        """
        return self.__expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.__reserved_members or self.__expedition else True
    def update(self,player):
        for en in self.__expedition:
             en.is_cd()
             en.move()
             en.attack(player)
             if(en.health<=0):
                self.__expedition.remove(en)
                self.kill_amount += 1 # 擊殺病毒數量
        self.campaign()        
        
    def touch(self, virus):
        return self.__expedition
    
    
    
        