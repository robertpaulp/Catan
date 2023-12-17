import pygame
import pygame.freetype
from constants import *

class CardsPrompt:
    cards_prompt_rect = pygame.Rect(CARDS_PROMPT_X_AXIS, CARDS_PROMPT_Y_AXIS + 29, CARDS_PROMPT_WIDTH - 4, CARDS_PROMPT_HEIGHT - 21)

    pygame.font.init()
    font = pygame.font.SysFont('Segoe UI Black', 25)
    font_numbers = pygame.font.SysFont('Arial', 25)
    small_font = pygame.font.SysFont('Segoe UI Black', 15)

    def show_cards(self, window, player):
        # Draw prompt rectangle
        pygame.draw.rect(window, WHITE, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 4, CARDS_PROMPT_WIDTH + 4, CARDS_PROMPT_HEIGHT + 14))
        surface = pygame.Surface((CARDS_PROMPT_WIDTH + 4, CARDS_PROMPT_HEIGHT + 14))
        image = pygame.image.load(SIGN_SPRITE)
        image = pygame.transform.scale(image, (CARDS_PROMPT_WIDTH + 4, CARDS_PROMPT_HEIGHT + 20))
        pygame.draw.rect(window, BRASS, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 4, CARDS_PROMPT_WIDTH + 4, 35))
        window.blit(image, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 10))
        pygame.draw.rect(window, player.color, (CARDS_PROMPT_X_AXIS + 23, CARDS_PROMPT_Y_AXIS + 25, CARDS_PROMPT_WIDTH - 47, 5), 4)
        # pygame.draw.rect(window, player.color, CardsPrompt.cards_prompt_rect, 10)
        # pygame.draw.rect(window, WHITE, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 4, CARDS_PROMPT_WIDTH + 4, 35))
        # pygame.draw.rect(window, BROWN, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 4, CARDS_PROMPT_WIDTH + 4, 35), 4)
        # pygame.draw.rect(window, BROWN, (CARDS_PROMPT_X_AXIS - 4, CARDS_PROMPT_Y_AXIS - 4, CARDS_PROMPT_WIDTH + 4, CARDS_PROMPT_HEIGHT + 14), 4)

        # Write prompt text
        text = CardsPrompt.font.render(player.name + " Resources", True, BROWN)
        text_rect = pygame.Rect(CARDS_PROMPT_X_AXIS + 130, CARDS_PROMPT_Y_AXIS - 5, CARDS_PROMPT_WIDTH, CARDS_PROMPT_HEIGHT)
        window.blit(text, text_rect)

        # Draw Brick Card
        #pygame.draw.rect(window, BRICK_COLOR, (CARDS_POSITION_X, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT))
        image = pygame.image.load(BRICKS_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (CARDS_POSITION_X - 5, CARDS_POSITION_Y))

        brick_text = CardsPrompt.small_font.render('Bricks', True, BROWN)
        window.blit(brick_text, (CARDS_POSITION_X - 3, CARDS_POSITION_Y + CARD_HEIGHT))
        
        # Brick Cards Number
        brick_number = CardsPrompt.font_numbers.render(str(player.cards["Bricks"]), True, BROWN)
        window.blit(brick_number, (CARDS_POSITION_X + 15, CARDS_POSITION_Y + CARD_HEIGHT + 16))

        # Draw Lumber Card
       # pygame.draw.rect(window, LUMBER_COLOR, (CARDS_POSITION_X + CARDS_SPACING_HELPER, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(LUMBER_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (CARDS_POSITION_X + CARDS_SPACING_HELPER, CARDS_POSITION_Y))

        lumber_text = CardsPrompt.small_font.render('Lumber', True, BROWN)
        window.blit(lumber_text, (CARDS_POSITION_X - 5 +CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT))

        # Lumber Cards Number
        lumber_number = CardsPrompt.font_numbers.render(str(player.cards["Lumber"]), True, BROWN)
        window.blit(lumber_number, (CARDS_POSITION_X + 15 + CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT + 16))

        # Draw Ore Card
        #pygame.draw.rect(window, ORE_COLOR, (CARDS_POSITION_X + 2 * CARDS_SPACING_HELPER, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(ORE_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (CARDS_POSITION_X + 2 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + 5))

        grain_text = CardsPrompt.small_font.render('Ore', True, BROWN)
        window.blit(grain_text, (CARDS_POSITION_X + 6 +  2 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT))

        # Ore Cards Number
        ore_number = CardsPrompt.font_numbers.render(str(player.cards["Ore"]), True, BROWN)
        window.blit(ore_number, (CARDS_POSITION_X + 15 + 2 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT + 16))

        # Draw Grain Card
       # pygame.draw.rect(window, GRAIN_COLOR, (CARDS_POSITION_X + 3 * CARDS_SPACING_HELPER, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(GRAIN_SPRITE)
        image = pygame.transform.scale_by(image, 0.9)
        window.blit(image, (CARDS_POSITION_X + 3 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + 5))

        grain_text = CardsPrompt.small_font.render('Grain', True, BROWN)
        window.blit(grain_text, (CARDS_POSITION_X + 3 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT))

        # Grain Cards Number
        grain_number = CardsPrompt.font_numbers.render(str(player.cards["Grain"]), True, BROWN)
        window.blit(grain_number, (CARDS_POSITION_X + 15 + 3 *CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT + 16))

        # Draw Wool Card
        #pygame.draw.rect(window, WOOL_COLOR, (CARDS_POSITION_X + 4 * CARDS_SPACING_HELPER, CARDS_POSITION_Y, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(WOOL_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (CARDS_POSITION_X + 4 * CARDS_SPACING_HELPER - 3, CARDS_POSITION_Y + 3))

        wool_text = CardsPrompt.small_font.render('Wool', True, BROWN)
        window.blit(wool_text, (CARDS_POSITION_X + 4 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT))

        # Wool Cards Number
        wool_number = CardsPrompt.font_numbers.render(str(player.cards["Wool"]), True, BROWN)
        window.blit(wool_number, (CARDS_POSITION_X + 15 + 4 * CARDS_SPACING_HELPER, CARDS_POSITION_Y + CARD_HEIGHT + 16))

cards_prompt = CardsPrompt()
