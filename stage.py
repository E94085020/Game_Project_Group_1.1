import pygame
import os
from player import Player_action
from setting import WIN_HEIGHT, WIN_WIDTH,FPS,IMAGE_PATH,SOUND_PATH
from bullet import BulletGroup
from virus import Virusgroup
from item import *

# 失敗圖
LOSE = pygame.image.load(os.path.join(IMAGE_PATH, "lose.png"))
# 背景圖
BACKGROUND_IMAGE_1 = pygame.image.load(os.path.join(IMAGE_PATH, "level_1_background.png"))
BACKGROUND_IMAGE_2 = pygame.image.load(os.path.join(IMAGE_PATH, "level_2_background.png"))
BACKGROUND_IMAGE_3 = pygame.image.load(os.path.join(IMAGE_PATH, "level_3_background.png"))
BACKGROUND_IMAGE_4 = pygame.image.load(os.path.join(IMAGE_PATH, "level_4_background.png"))
BACKGROUND_IMAGE_5 = pygame.image.load(os.path.join(IMAGE_PATH, "level_5_background.png"))
BACKGROUND_IMAGE_6 = pygame.image.load(os.path.join(IMAGE_PATH, "level_6_background.png"))
BACKGROUND_IMAGE_7 = pygame.image.load(os.path.join(IMAGE_PATH, "level_7_background.png"))
BACKGROUND_IMAGE_8 = pygame.image.load(os.path.join(IMAGE_PATH, "level_8_background.png"))
# 故事圖
PROLEGOMENON = pygame.image.load(os.path.join(IMAGE_PATH, "prolegomenon.png"))
STORY_1 =pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "story1.png")), (WIN_WIDTH, WIN_HEIGHT))
STORY_2 =pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "story2.png")), (WIN_WIDTH, WIN_HEIGHT))
STORY_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "story3.png")), (WIN_WIDTH, WIN_HEIGHT))
STORY_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "story4.png")), (WIN_WIDTH, WIN_HEIGHT))
STORY_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "story5.png")), (WIN_WIDTH, WIN_HEIGHT))
STORY_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "story6.png")), (WIN_WIDTH, WIN_HEIGHT))
STORY_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "story7.png")), (WIN_WIDTH, WIN_HEIGHT))
STORY_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "story8.png")), (WIN_WIDTH, WIN_HEIGHT))
EPILOGUE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "epilogue.png")), (WIN_WIDTH, WIN_HEIGHT))
# 通關圖
CONG_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "congratulations1.png")), (WIN_WIDTH, WIN_HEIGHT))
CONG_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "congratulations2.png")), (WIN_WIDTH, WIN_HEIGHT))
CONG_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "congratulations3.png")), (WIN_WIDTH, WIN_HEIGHT))
CONG_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "congratulations4.png")), (WIN_WIDTH, WIN_HEIGHT))
CONG_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "congratulations5.png")), (WIN_WIDTH, WIN_HEIGHT))
CONG_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "congratulations6.png")), (WIN_WIDTH, WIN_HEIGHT))
CONG_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "congratulations7.png")), (WIN_WIDTH, WIN_HEIGHT))
CONG_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "congratulations8.png")), (WIN_WIDTH, WIN_HEIGHT))
# 防疫資訊圖
INF_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information1.png")), (WIN_WIDTH, WIN_HEIGHT))
INF_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information2.png")), (WIN_WIDTH, WIN_HEIGHT))
INF_3_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information3_1.png")), (WIN_WIDTH, WIN_HEIGHT))
INF_3_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information3_2.png")), (WIN_WIDTH, WIN_HEIGHT))
INF_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information4.png")), (WIN_WIDTH, WIN_HEIGHT))
INF_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information5.png")), (WIN_WIDTH, WIN_HEIGHT))
INF_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information6.png")), (WIN_WIDTH, WIN_HEIGHT))
INF_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information7.png")), (WIN_WIDTH, WIN_HEIGHT))
INF_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "information8.png")), (WIN_WIDTH, WIN_HEIGHT))
# 其他圖
UNLOCK = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "unlock.png")), (WIN_WIDTH, WIN_HEIGHT))
MASK = pygame.image.load(os.path.join(IMAGE_PATH, "mask.png"))
N95 =  pygame.image.load(os.path.join(IMAGE_PATH, "N95.png"))
VACCINE = pygame.image.load(os.path.join(IMAGE_PATH, "vaccine.png"))

class Stage:
    def __init__(self):
        self.image=None
        self.story_image=None
        self.pic_set=None
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.lose = pygame.transform.scale(LOSE, (WIN_WIDTH, WIN_HEIGHT))
        self.clear = pygame.mixer.Sound("./sound/sucess.mp3")
        self.fail = pygame.mixer.Sound("./sound/failure.mp3")
        self.next_stage=None
        self.target=None
        self.pass_1=False
        self.player = Player_action()
        self.bullet = BulletGroup()
        self.virus = Virusgroup()
        self.weapon_1=HCLO()
        self.weapon_2=Not_activated()
        self.vaccine=None
        self.mask_get=0
        self.n95_get=0
        self.vaccine_get=0
        self.summon=0
        self.summon_cd=350
        self.summon_num=4
     
    @classmethod        
    def stage_1(cls):
        stage1=cls()
        stage1.image= pygame.transform.scale(BACKGROUND_IMAGE_1, (WIN_WIDTH, WIN_HEIGHT))
        stage1.story_image=STORY_1
        stage1.target=10
        stage1.pic_set=[CONG_1,INF_1]
        stage1.mask_get=10
        return stage1
    
    @classmethod     
    def stage_2(cls):
        stage2=cls()
        stage2.image= pygame.transform.scale(BACKGROUND_IMAGE_2, (WIN_WIDTH, WIN_HEIGHT))
        stage2.story_image=STORY_2        
        stage2.target=20
        stage2.pic_set=[CONG_2,INF_2]
        stage2.summon_num=5
        return stage2
     
    @classmethod
    def stage_3(cls):
        stage3=cls()
        stage3.image= pygame.transform.scale(BACKGROUND_IMAGE_3, (WIN_WIDTH, WIN_HEIGHT))
        stage3.story_image=STORY_3        
        stage3.target=30
        stage3.pic_set=[CONG_3,INF_3_1,INF_3_2]
        stage3.summon_num=5
        return stage3  
       
    @classmethod
    def stage_4(cls):
        stage4=cls()
        stage4.image= pygame.transform.scale(BACKGROUND_IMAGE_4, (WIN_WIDTH, WIN_HEIGHT))
        stage4.story_image=STORY_4        
        stage4.target=40
        stage4.pic_set=[CONG_4,INF_4]
        stage4.weapon_2=Alcohol_atk()
        stage4.n95_get=5
        stage4.summon_cd=350
        stage4.summon_num=5
        return stage4
    
    @classmethod
    def stage_5(cls):
        stage5=cls()
        stage5.image= pygame.transform.scale(BACKGROUND_IMAGE_5, (WIN_WIDTH, WIN_HEIGHT))
        stage5.story_image=STORY_5        
        stage5.target=50
        stage5.pic_set=[CONG_5,INF_5]
        stage5.weapon_2=Alcohol_atk()
        stage5.vaccine_get=2
        stage5.summon_cd=350
        stage5.summon_num=5
        return stage5
        
    @classmethod
    def stage_6(cls):
        stage6=cls()
        stage6.image= pygame.transform.scale(BACKGROUND_IMAGE_6, (WIN_WIDTH, WIN_HEIGHT))
        stage6.story_image=STORY_6        
        stage6.target=60
        stage6.pic_set=[CONG_6,INF_6]
        stage6.weapon_2=Alcohol_atk()
        stage6.summon_cd=350
        stage6.summon_num=6
        return stage6
        
    @classmethod
    def stage_7(cls):
        stage7=cls()
        stage7.image= pygame.transform.scale(BACKGROUND_IMAGE_7, (WIN_WIDTH, WIN_HEIGHT))
        stage7.story_image=STORY_7        
        stage7.target=80
        stage7.pic_set=[CONG_7,INF_7]
        stage7.weapon_2=Alcohol_atk()
        stage7.summon_cd=350
        stage7.summon_num=6
        return stage7
        
    @classmethod
    def stage_8(cls):
        stage8=cls()
        stage8.image= pygame.transform.scale(BACKGROUND_IMAGE_8, (WIN_WIDTH, WIN_HEIGHT))
        stage8.story_image=STORY_8        
        stage8.target=100
        stage8.pic_set=[CONG_8,INF_8,UNLOCK,EPILOGUE]
        stage8.weapon_2=Alcohol_atk()
        stage8.summon_cd=350
        stage8.summon_num=5
        return stage8          
            
    def run(self,beg):
        self.quit_game=False
        if self.story()==True:
            return True
        self.virus.add(10) 
        while not self.quit_game:
            pygame.time.Clock().tick(FPS)
            pl=self.player.get()
            if pl.hp<=0 :
                if self.fail is not None:
                    self.fail.play()
                    self.fail=None
                pygame.init()
                self.win.blit(self.lose, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit_game = True
                        return True
                pygame.display.update()  
            elif(self.virus.is_empty() and self.virus.kill_amount >= self.target):# if擊殺病毒數量超過x隻
                 self.quit_game = True
            else:
                if self.virus.kill_amount < self.target:
                    self.summon=(self.summon+1)%self.summon_cd  
                    if (self.summon==self.summon_cd-1):
                        self.virus.add(self.summon_num) 
                self.draw(beg,self.target)
                self.quit_game=self.update(beg)
                if self.quit_game==True:
                    return True
        return self.change_stage(beg)
    
    def update(self,beg):
        pygame.init()
        game_quit = False
        # event loop
        while not game_quit:
            # virus
            #self.virus.campaign()                                            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    return game_quit
                # player press action
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_w):
                        self.player.jump()
                    if(event.key == pygame.K_1):
                        if beg.mask_count>0:
                            beg.mask_count-=1
                            self.player.use_mask(Mask.surgical_mask())
                    if(event.key == pygame.K_2):
                        if beg.n95_count>0:
                            beg.n95_count-=1
                            self.player.use_mask(Mask.N95())                            
                    if(event.key == pygame.K_3):
                        if beg.vaccine_count>0:
                            beg.vaccine_count-=1                        
                            self.vaccine=Vaccine()
                    if(event.key == pygame.K_F4):
                        pygame.mixer.music.pause()
                    if(event.key == pygame.K_F5):
                        pygame.mixer.music.unpause()                       
                key_pressed= pygame.key.get_pressed()   #因為考慮同時按下三個按鍵的情況，所以設置三個key_pressed     
                key_pressed_2= pygame.key.get_pressed()
                key_pressed_3 = pygame.key.get_pressed()
                if (key_pressed[pygame.K_u] or key_pressed_2[pygame.K_u] or key_pressed_3[pygame.K_u]):
                    self.player.turn_L()
                elif (key_pressed[pygame.K_i] or key_pressed_2[pygame.K_i] or key_pressed_3[pygame.K_i]):
                      self.player.turn_R()                
                if (key_pressed[pygame.K_a] or key_pressed_2[pygame.K_a] or key_pressed_3[pygame.K_a]):
                    self.player.move_L()
                elif (key_pressed[pygame.K_d] or key_pressed_2[pygame.K_d] or key_pressed_3[pygame.K_d]):
                      self.player.move_R()
                if(key_pressed[pygame.K_s] or key_pressed_2[pygame.K_s] or key_pressed_3[pygame.K_s]):
                    self.player.down=True
                else:
                    self.player.down=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.weapon_1.use(self.player,self.bullet,self.virus.get())
                if (key_pressed[pygame.K_SPACE]):
                    self.weapon_2.use(self.player,self.bullet,self.virus.get())
   
            self.weapon_2.update()        
            self.player.update()
            self.bullet.update(self.virus.get())
            self.virus.update(self.player)
            if self.vaccine is not None:
                self.vaccine.update(self.player)
                if self.vaccine.active==False:
                    self.vaccine = None
            return game_quit        
        
    
    def draw(self,beg,target):
        # draw background
        self.win.blit(self.image, (0, 0))
        # draw player
        beg.draw(self.win) 
        self.player.draw(self.win)
        self.bullet.draw(self.win)
        self.virus.draw(self.win,target)
        self.weapon_2.draw(self.win)
        if self.vaccine is not None:
            self.vaccine.draw(self.win)                        
        pygame.display.update()
    
    def change_stage(self,beg):
        self.clear.play()
        beg.mask_count+=self.mask_get
        beg.n95_count+=self.n95_get
        beg.vaccine_count+=self.vaccine_get
        for pic in self.pic_set:
            self.pass_1=False
            self.wait=0
            while not self.pass_1:
                self.wait+=1
                self.win.blit(pic,(0,0))
                pygame.display.update()
                if self.wait>1200:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            self.pass_1=True
                        if event.type == pygame.QUIT:
                            return True   
        return False
    
    def story(self):
        self.pass_1=False
        self.wait=0
        while not self.pass_1:
            self.wait+=1
            self.win.blit(self.story_image,(0,0))
            pygame.display.update()
            if self.wait>1500:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        self.pass_1=True
                    if event.type == pygame.QUIT:
                        return True   
        return False
class End:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.image=EPILOGUE
    def run(self,beg):
        self.quit=False
        while not self.quit:
            self.win.blit(self.image,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit=True
                    return True          
        
class Stageset:
    def __init__(self):
        self.stage_set=[Stage.stage_1(),Stage.stage_2(),Stage.stage_3(),Stage.stage_4(),Stage.stage_5(),
                        Stage.stage_6(),Stage.stage_7(),Stage.stage_8(),End()]
        
    def get(self):
        return self.stage_set
    
class Mainmenu:
    def __init__(self):
        self.beg=Beg()
        self.stage=Stageset()
        self.stage_set=self.stage.get()  
        
    def run(self):
        for st in self.stage_set:
            self.quit=st.run(self.beg)
            if self.quit:
                break
class Beg:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 30)
        self.mask_image=pygame.transform.scale(MASK,(60,60))
        self.n95_image=pygame.transform.scale(N95,(40,40))
        self.vaccine_image=pygame.transform.scale(VACCINE,(40,40))
        self.mask_count=0
        self.n95_count=0
        self.vaccine_count=0
        
    def draw(self,win):
        text = self.font.render(f"x {self.mask_count}", True, (255, 255, 255))
        win.blit(self.mask_image,(35,640))
        win.blit(text, (100, 650))
        text_2 = self.font.render(f"x {self.n95_count}", True, (255, 255, 255))
        win.blit(self.n95_image,(170,650))
        win.blit(text_2, (220, 650))
        text_3 = self.font.render(f"x {self.vaccine_count}", True, (255, 255, 255))
        win.blit(self.vaccine_image,(270,650))
        win.blit(text_3, (320, 650))         
        