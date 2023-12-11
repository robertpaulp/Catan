import pygame
import pygame.freetype
from constants import *
import time

class Trade:
    trade_rect = pygame.Rect(TRADE_PROMPT_X_AXIS, TRADE_PROMPT_Y_AXIS, TRADE_PROMPT_WIDTH, TRADE_PROMPT_HEIGHT)

    card_color = {
			"Wood": (3, 75, 3),
			"Wheat": (240, 215, 49),
			"Sheep": (242, 240, 235),
			"Brick": (188, 74, 60),
			"Ore": (144, 144, 144)
		} 

    card_sprite = {
			"Wood": LUMBER_SPRITE,
			"Wheat": GRAIN_SPRITE,
			"Sheep": WOOL_SPRITE,
			"Brick": BRICKS_SPRITE,
			"Ore": ORE_SPRITE
		} 

    pygame.font.init()
    font = pygame.font.SysFont('Segoe UI Black', 25)
    font2 = pygame.font.SysFont('Segoe UI Black', 22)
    font_numbers = pygame.font.SysFont('Arial', 25)
    small_font = pygame.font.SysFont('Segoe UI Black', 15)

    def show_trade(self, window, player):
        # Draw prompt rectangle
        pygame.draw.rect(window, BRASS, Trade.trade_rect)
        pygame.draw.rect(window, BROWN, (TRADE_PROMPT_X_AXIS - 4, TRADE_PROMPT_Y_AXIS - 4, TRADE_PROMPT_WIDTH + 4, TRADE_PROMPT_HEIGHT + 4), 4)

        """
        image = pygame.image.load(TRADE_TABLE_SPRITE)
        image = pygame.transform.scale(image, (TRADE_PROMPT_WIDTH  - 10, TRADE_PROMPT_HEIGHT - 30))
        window.blit(image, (TRADE_PROMPT_X_AXIS, TRADE_PROMPT_Y_AXIS))
        """
        
        # Write prompt text
        text = Trade.font.render("TRADE THE BANK", True, BROWN)
        text_rect = pygame.Rect(TRADE_PROMPT_X_AXIS + 30, TRADE_PROMPT_Y_AXIS + 10, TRADE_PROMPT_WIDTH, TRADE_PROMPT_HEIGHT)
        window.blit(text, text_rect)

        text = Trade.font2.render(player.name + " possible trades : ", True, BROWN)
        text_rect = pygame.Rect(TRADE_PROMPT_X_AXIS + 10, TRADE_PROMPT_Y_AXIS + 70, TRADE_PROMPT_WIDTH, TRADE_PROMPT_HEIGHT)
        window.blit(text, text_rect)

        trades_counter = 0
        for card in player.cards:
            if player.possible_trade[card] == True:

                # Draw the trade button
                # button_rect = pygame.Rect(TRADE_BUTTON_X_AXIS, TRADE_BUTTON_Y_AXIS + trades_counter * (TRADE_BUTTON_HEIGHT + 25), TRADE_BUTTON_WIDTH, TRADE_BUTTON_HEIGHT)
                # pygame.draw.rect(window, WHITE, button_rect)
                image = pygame.image.load(TRADE_BUTTON_SPRITE)
                image = pygame.transform.scale_by(image, 1)
                window.blit(image, (TRADE_BUTTON_X_AXIS + 35, TRADE_BUTTON_Y_AXIS + trades_counter * (TRADE_BUTTON_HEIGHT + 25)))

                # Draw the button images
               # card1_rect = pygame.Rect(TRADE_BUTTON_X_AXIS + 70, TRADE_BUTTON_Y_AXIS + 7 + trades_counter * (TRADE_BUTTON_HEIGHT + 25), CARD_WIDTH, CARD_HEIGHT)
               # pygame.draw.rect(window, Trade.card_color[card], card1_rect)
                image = pygame.image.load(Trade.card_sprite[card])
                image = pygame.transform.scale_by(image, 1)
                window.blit(image, (TRADE_BUTTON_X_AXIS + 70, TRADE_BUTTON_Y_AXIS + 7 + trades_counter * (TRADE_BUTTON_HEIGHT + 25)))

                """
                # Draw the explaining text 
                text = Trade.small_font.render("Trade 3 " + card + " cards for any card", True, BROWN)
                window.blit(text, (TRADE_BUTTON_X_AXIS - 10, TRADE_BUTTON_Y_AXIS + 60 + trades_counter * (TRADE_BUTTON_HEIGHT + 25)))
                """
			
                trades_counter += 1
trade = Trade()