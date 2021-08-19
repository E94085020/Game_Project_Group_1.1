import pygame
from setting import GRAY
class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = False
        self.radius = (width/2)+(width/10)
        self.x_pos = x + (width/2)
        self.y_pos = y + (height/2)

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False
    
    def create_frame(self, x: int, y: int):
        """if cursor position is on the button, create button frame"""
        if self.clicked(x, y):
            self.frame = True
        else:
            self.frame = False


    def draw_frame(self, win):
        if self.frame == True:
            pygame.draw.circle(win, GRAY, (self.x_pos, self.y_pos), self.radius, 5)

