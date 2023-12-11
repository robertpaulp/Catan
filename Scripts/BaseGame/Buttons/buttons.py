import pygame
import pygame.freetype
from constants import *

class Button:
    def __init__(self, name, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.name = name
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
    def create_settlement_button():
        button_img = pygame.image.load(SETTLEMENT_BUTTON_SPRITE).convert_alpha()
        button = Button("settlement", SCREEN_WIDTH - 750, SCREEN_HEIGHT - 100, button_img, 1)
        return button

    @staticmethod
    def create_road_button():
        button_img = pygame.image.load(ROAD_BUTTON_SPRITE).convert_alpha()
        button = Button("road", SCREEN_WIDTH - 570, SCREEN_HEIGHT - 100, button_img, 1)
        return button
    
    @staticmethod
    def create_special_card_button():
        button_img = pygame.image.load(SPECIAL_CARD_BUTTON_SPRITE).convert_alpha()
        button = Button("special_card", SCREEN_WIDTH - 390, SCREEN_HEIGHT - 100, button_img, 1)
        return button
    
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

        player.trade_counter = 0
        for card in player.cards:
            if player.possible_trade[card] == True:

                # Draw the trade button
                # button_rect = pygame.Rect(TRADE_BUTTON_X_AXIS, TRADE_BUTTON_Y_AXIS + trades_counter * (TRADE_BUTTON_HEIGHT + 25), TRADE_BUTTON_WIDTH, TRADE_BUTTON_HEIGHT)
                # pygame.draw.rect(window, WHITE, button_rect)
                image = pygame.image.load(TRADE_BUTTON_SPRITE)
                image = pygame.transform.scale_by(image, 1)
                window.blit(image, (TRADE_BUTTON_X_AXIS + 35, TRADE_BUTTON_Y_AXIS + player.trade_counter * (TRADE_BUTTON_HEIGHT + 25)))

                new_button = Button("trade", TRADE_BUTTON_X_AXIS + 35, TRADE_BUTTON_Y_AXIS + player.trade_counter * (TRADE_BUTTON_HEIGHT + 25), image, 1)
                player.trade_button.append(new_button)
                # Draw the button images
               # card1_rect = pygame.Rect(TRADE_BUTTON_X_AXIS + 70, TRADE_BUTTON_Y_AXIS + 7 + trades_counter * (TRADE_BUTTON_HEIGHT + 25), CARD_WIDTH, CARD_HEIGHT)
               # pygame.draw.rect(window, Trade.card_color[card], card1_rect)
                image = pygame.image.load(Trade.card_sprite[card])
                image = pygame.transform.scale_by(image, 1)
                window.blit(image, (TRADE_BUTTON_X_AXIS + 70, TRADE_BUTTON_Y_AXIS + 7 + player.trade_counter * (TRADE_BUTTON_HEIGHT + 25)))

                """
                # Draw the explaining text 
                text = Trade.small_font.render("Trade 3 " + card + " cards for any card", True, BROWN)
                window.blit(text, (TRADE_BUTTON_X_AXIS - 10, TRADE_BUTTON_Y_AXIS + 60 + trades_counter * (TRADE_BUTTON_HEIGHT + 25)))
                """
                player.trade_counter += 1


trade = Trade()

class TradePrompt:
    trade_prompt_rect = pygame.Rect(TRADE_POSITION_X, TRADE_POSITION_Y, 450, 200)

    pygame.font.init()
    font = pygame.font.SysFont('Segoe UI Black', 25)
    font_numbers = pygame.font.SysFont('Arial', 25)
    small_font = pygame.font.SysFont('Segoe UI Black', 15)

    def show_trade_prompt(self, window, player):
        # Draw prompt rectangle
        pygame.draw.rect(window, BRASS, TradePrompt.trade_prompt_rect)

        # Draw Brick Card
        #pygame.draw.rect(window, BRICK_COLOR, (TRADE_POSITION_X, TRADE_POSITION_Y, CARD_WIDTH, CARD_HEIGHT))
        image = pygame.image.load(BRICKS_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT - 5, TRADE_POSITION_Y_DOWN))

        brick_text = TradePrompt.small_font.render('Bricks', True, BROWN)
        window.blit(brick_text, (TRADE_POSITION_X_RIGHT - 3, TRADE_POSITION_Y_DOWN + CARD_HEIGHT))
        
        # Brick Cards Number
        brick_number = TradePrompt.font_numbers.render(str(player.cards["Brick"]), True, BROWN)
        window.blit(brick_number, (TRADE_POSITION_X_RIGHT + 15, TRADE_POSITION_Y_DOWN + CARD_HEIGHT + 16))

        # Draw Lumber Card
       # pygame.draw.rect(window, LUMBER_COLOR, (TRADE_POSITION_X_RIGHT + CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(LUMBER_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN))

        lumber_text = TradePrompt.small_font.render('Lumber', True, BROWN)
        window.blit(lumber_text, (TRADE_POSITION_X_RIGHT - 5 +CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + CARD_HEIGHT))

        # Lumber Cards Number
        lumber_number = TradePrompt.font_numbers.render(str(player.cards["Wood"]), True, BROWN)
        window.blit(lumber_number, (TRADE_POSITION_X_RIGHT + 15 + CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + CARD_HEIGHT + 16))

        # Draw Ore Card
        #pygame.draw.rect(window, ORE_COLOR, (TRADE_POSITION_X_RIGHT + 2 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(ORE_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 2 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + 5))

        grain_text = TradePrompt.small_font.render('Ore', True, BROWN)
        window.blit(grain_text, (TRADE_POSITION_X_RIGHT + 6 +  2 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + CARD_HEIGHT))

        # Ore Cards Number
        ore_number = TradePrompt.font_numbers.render(str(player.cards["Ore"]), True, BROWN)
        window.blit(ore_number, (TRADE_POSITION_X_RIGHT + 15 + 2 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + CARD_HEIGHT + 16))

        # Draw Grain Card
       # pygame.draw.rect(window, GRAIN_COLOR, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(GRAIN_SPRITE)
        image = pygame.transform.scale_by(image, 0.9)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + 5))

        grain_text = TradePrompt.small_font.render('Grain', True, BROWN)
        window.blit(grain_text, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + CARD_HEIGHT))

        # Grain Cards Number
        grain_number = TradePrompt.font_numbers.render(str(player.cards["Wheat"]), True, BROWN)
        window.blit(grain_number, (TRADE_POSITION_X_RIGHT + 15 + 3 *CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + CARD_HEIGHT + 16))

        # Draw Wool Card
        #pygame.draw.rect(window, WOOL_COLOR, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(WOOL_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 3, TRADE_POSITION_Y_DOWN + 3))

        wool_text = TradePrompt.small_font.render('Wool', True, BROWN)
        window.blit(wool_text, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + CARD_HEIGHT))

        # Wool Cards Number
        wool_number = TradePrompt.font_numbers.render(str(player.cards["Sheep"]), True, BROWN)
        window.blit(wool_number, (TRADE_POSITION_X_RIGHT + 15 + 4 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN + CARD_HEIGHT + 16))

trade_prompt = TradePrompt()