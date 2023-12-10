import pygame
import pygame.freetype
from constants import *

class CardsPrompt:
    cards_prompt_rect = pygame.Rect(CARDS_PROMPT_X_AXIS, CARDS_PROMPT_Y_AXIS, CARDS_PROMPT_WIDTH, CARDS_PROMPT_HEIGHT)

    pygame.font.init()
    font = pygame.font.SysFont('Segoe UI Black', 25)
    font_numbers = pygame.font.SysFont('Arial', 25)
    small_font = pygame.font.SysFont('Segoe UI Black', 15)

    def __init__(self):
        self.card_type = {
            "Brick": 0,
            "Lumber": 0,
            "Ore": 0,
            "Grain": 0,
            "Wool": 0
        }

    def show_cards(self, window, player):
        # Draw prompt rectangle
        pygame.draw.rect(window, player.color, CardsPrompt.cards_prompt_rect)
        pygame.draw.rect(window, BRASS, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 4, CARDS_PROMPT_WIDTH + 4, 35))
        pygame.draw.rect(window, BROWN, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 4, CARDS_PROMPT_WIDTH + 4, 35), 4)
        pygame.draw.rect(window, BROWN, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 4, CARDS_PROMPT_WIDTH + 4, CARDS_PROMPT_HEIGHT + 4), 4)

        # Write prompt text
        text = CardsPrompt.font.render(player.name + " Resources", True, BROWN)
        text_rect = pygame.Rect(CARDS_PROMPT_X_AXIS + 130, CARDS_PROMPT_Y_AXIS - 5, CARDS_PROMPT_WIDTH, CARDS_PROMPT_HEIGHT)
        window.blit(text, text_rect)

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

cards_prompt = CardsPrompt()