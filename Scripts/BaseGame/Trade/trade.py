import pygame
import pygame.freetype
from constants import *

class Trade:
    trade_rect = pygame.Rect(TRADE_PROMPT_X_AXIS, TRADE_PROMPT_Y_AXIS, TRADE_PROMPT_WIDTH, TRADE_PROMPT_HEIGHT)

    card_color = {
			"Wood": (3, 75, 3),
			"Wheat": (240, 215, 49),
			"Sheep": (242, 240, 235),
			"Brick": (188, 74, 60),
			"Ore": (144, 144, 144)
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
                button_rect = pygame.Rect(TRADE_BUTTON_X_AXIS, TRADE_BUTTON_Y_AXIS + trades_counter * (TRADE_BUTTON_HEIGHT + 25), TRADE_BUTTON_WIDTH, TRADE_BUTTON_HEIGHT)
                pygame.draw.rect(window, WHITE, button_rect)
                
                # Draw the button images
                card1_rect = pygame.Rect(TRADE_BUTTON_X_AXIS + 57, TRADE_BUTTON_Y_AXIS + trades_counter * (TRADE_BUTTON_HEIGHT + 25), CARD_WIDTH, CARD_HEIGHT)
                pygame.draw.rect(window, Trade.card_color[card], card1_rect)
                card1_rect = pygame.Rect(TRADE_BUTTON_X_AXIS + 60, TRADE_BUTTON_Y_AXIS + 7 + trades_counter * (TRADE_BUTTON_HEIGHT + 25), CARD_WIDTH, CARD_HEIGHT)
                pygame.draw.rect(window, Trade.card_color[card], card1_rect)
                card1_rect = pygame.Rect(TRADE_BUTTON_X_AXIS + 63, TRADE_BUTTON_Y_AXIS + 14 + trades_counter * (TRADE_BUTTON_HEIGHT + 25), CARD_WIDTH, CARD_HEIGHT)
                pygame.draw.rect(window, Trade.card_color[card], card1_rect)

                # Draw the explaining text 
                text = Trade.small_font.render("Trade 3 " + card + " cards for any card", True, BROWN)
                window.blit(text, (TRADE_BUTTON_X_AXIS - 10, TRADE_BUTTON_Y_AXIS + 60 + trades_counter * (TRADE_BUTTON_HEIGHT + 25)))
			
                trades_counter += 1
        """
        # Draw Brick Card
        pygame.draw.rect(window, BRICK_COLOR, (CARDS_POSITION_X, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT))
        brick_text = CardsPrompt.small_font.render('Bricks', True, BROWN)
        window.blit(brick_text, (CARDS_POSITION_X - 3, CARDS_POSITION_Y + CARD_HEIGHT))
        
        # Brick Cards Number
        brick_number = CardsPrompt.font_numbers.render(str(player.cards["Brick"]), True, BROWN)
        window.blit(brick_number, (CARDS_POSITION_X + 10, CARDS_POSITION_Y + CARD_HEIGHT + 16))

        # Draw Lumber Card
        pygame.draw.rect(window, LUMBER_COLOR, (CARDS_POSITION_X + CARDS_SPACING_HELPER, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT), 0)
        lumber_text = CardsPrompt.small_font.render('Lumber', True, BROWN)
        window.blit(lumber_text, (CARDS_POSITION_X + CARDS_SPACING_HELPER - 7, CARDS_POSITION_Y + CARD_HEIGHT))
        
        # Lumber Cards Number
        lumber_number = CardsPrompt.font_numbers.render(str(player.cards["Wood"]), True, BROWN)
        window.blit(lumber_number, (CARDS_POSITION_X + 10 + CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT + 16))

        # Draw Ore Card
        pygame.draw.rect(window, ORE_COLOR, (CARDS_POSITION_X + 2 * CARDS_SPACING_HELPER, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT), 0)
        grain_text = CardsPrompt.small_font.render('Ore', True, BROWN)
        window.blit(grain_text, (CARDS_POSITION_X + 2 * CARDS_SPACING_HELPER + 3, CARDS_POSITION_Y + CARD_HEIGHT))

        # Ore Cards Number
        ore_number = CardsPrompt.font_numbers.render(str(player.cards["Ore"]), True, BROWN)
        window.blit(ore_number, (CARDS_POSITION_X + 10 + 2 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT + 16))

        # Draw Grain Card
        pygame.draw.rect(window, GRAIN_COLOR, (CARDS_POSITION_X + 3 * CARDS_SPACING_HELPER, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT), 0)
        grain_text = CardsPrompt.small_font.render('Grain', True, BROWN)
        window.blit(grain_text, (CARDS_POSITION_X + 3 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT))

        # Grain Cards Number
        grain_number = CardsPrompt.font_numbers.render(str(player.cards["Wheat"]), True, BROWN)
        window.blit(grain_number, (CARDS_POSITION_X + 10 + 3 *CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT + 16))

        # Draw Wool Card
        pygame.draw.rect(window, WOOL_COLOR, (CARDS_POSITION_X + 4 * CARDS_SPACING_HELPER, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT), 0)
        wool_text = CardsPrompt.small_font.render('Wool', True, BROWN)
        window.blit(wool_text, (CARDS_POSITION_X + 4 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT))

        # Wool Cards Number
        wool_number = CardsPrompt.font_numbers.render(str(player.cards["Sheep"]), True, BROWN)
        window.blit(wool_number, (CARDS_POSITION_X + 10 + 4 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT + 16))
        """
trade = Trade()