import pygame
from start_menu import StartMenu

if __name__ == '__main__':
    # initialization
    pygame.init()
  
    covid_game = StartMenu()
    covid_game.menu_run()