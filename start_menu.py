import pygame
import os
from stage import *
from setting import WIN_WIDTH, WIN_HEIGHT, FPS, GRAY,IMAGE_PATH,SOUND_PATH
from button import*

pygame.init()
pygame.mixer.init()


class StartMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "start_menu.png")), (WIN_WIDTH, WIN_HEIGHT))
        # button
        self.start_btn = Buttons(575, 506, 100, 100)  # x, y, width, height
        self.sound_btn = Buttons(34.5, 15.5, 55, 55)
        self.mute_btn = Buttons(118.5, 15.5, 55, 55)
        self.music_buttons = [self.start_btn,self.sound_btn,self.mute_btn]

    def play_music(self):
        pygame.mixer.music.load("./sound/Under_The_Radar.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def menu_run(self):
        run = True
        clock = pygame.time.Clock()
        pygame.display.set_caption("Drive Out The Virus")
        self.play_music()
        while run:
            clock.tick(FPS)
            self.menu_win.blit(self.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.start_btn.clicked(x, y):
                        game = Mainmenu()
                        game.run()
                        #run = False
                        
                    if self.mute_btn.clicked(x, y):         # 當 mute 這個 button 被按下的時候，將音樂停止
                         pygame.mixer.music.pause()
                    elif self.sound_btn.clicked(x, y):      # 當 sound 這個 button 被按下的時候，播放音樂
                        pygame.mixer.music.unpause()

            for btn in self.music_buttons:
                btn.create_frame(x, y)
                btn.draw_frame(self.menu_win)


            pygame.display.update()
        pygame.quit()


