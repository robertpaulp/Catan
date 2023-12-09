import pygame
import pygame.freetype
from constants import *

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.clicked_up = False

    def hover(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            print('HOVER')

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    
    @staticmethod
    def create_road_button():
        button_img = pygame.image.load(BUTTON_SPRITE).convert_alpha()
        button = Button(SCREEN_WIDTH - 500, SCREEN_HEIGHT - 100, button_img, 0.8)
        return button
    
    @staticmethod
    def create_settlement_button():
        button_img = pygame.image.load(BUTTON_SPRITE).convert_alpha()
        button = Button(SCREEN_WIDTH - 400, SCREEN_HEIGHT - 100, button_img, 0.8)
        return button
    
    @staticmethod
    def create_special_card_button():
        button_img = pygame.image.load(BUTTON_SPRITE).convert_alpha()
        button = Button(SCREEN_WIDTH - 300, SCREEN_HEIGHT - 100, button_img, 0.8)
        return button