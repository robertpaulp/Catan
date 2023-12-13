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
        self.card = " "
    """
    def hover_settlement(self, window, robber_pos, roll, current_player, GAME_START):
        #get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            image = pygame.image.load(PAPIRUS_SETTLEMENT_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (SCREEN_WIDTH - 755, SCREEN_HEIGHT - 300))
        while self.rect.collidepoint(pos):
            pos = pygame.mouse.get_pos()
        Board.redraw_board(window, robber_pos, roll, current_player, GAME_START)
        """

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
    def show_pressed_settlement_button(window):
        button_img = pygame.image.load(PRESSED_SETTLEMENT_BUTTON_SPRITE).convert_alpha()
        button = Button("settlement", SCREEN_WIDTH - 750, SCREEN_HEIGHT - 100, button_img, 1)
        window.blit(button_img, (button.rect.x, button.rect.y))

    @staticmethod
    def show_pressed_road_button(window):
        button_img = pygame.image.load(PRESSED_ROAD_BUTTON_SPRITE).convert_alpha()
        button = Button("road", SCREEN_WIDTH - 570, SCREEN_HEIGHT - 100, button_img, 1)
        window.blit(button_img, (button.rect.x, button.rect.y))
    
    """
    @staticmethod
    def create_special_card_button():
        button_img = pygame.image.load(SPECIAL_CARD_BUTTON_SPRITE).convert_alpha()
        button = Button("special_card", SCREEN_WIDTH - 390, SCREEN_HEIGHT - 100, button_img, 1)
        return button
    """
    @staticmethod
    def create_end_turn_button():
        button_img = pygame.image.load(END_TURN_BUTTON_SPRITE).convert_alpha()
        button = Button("end_turn", SCREEN_WIDTH - 390, SCREEN_HEIGHT - 100, button_img, 1)
        return button
    
    def show_pressed_trade_button(self, window):
        image = pygame.image.load(PRESSED_TRADE_BUTTON_SPRITE).convert_alpha()
        window.blit(self.image, (self.rect.x, self.rect.y))

    
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
    medium_font = pygame.font.SysFont('Segoe UI Black', 18)

    def show_trade(self, window, player):
        # Draw prompt rectangle
        pygame.draw.rect(window, BRASS, Trade.trade_rect)
        pygame.draw.rect(window, BROWN, (TRADE_PROMPT_X_AXIS - 4, TRADE_PROMPT_Y_AXIS - 4, TRADE_PROMPT_WIDTH + 4, TRADE_PROMPT_HEIGHT + 4), 4)

        """
        image = pygame.image.load(TRADE_TABLE_SPRITE)
        image = pygame.transform.scale(image, (TRADE_PROMPT_WIDTH  - 10, TRADE_PROMPT_HEIGHT - 30))
        window.blit(image, (TRADE_PROMPT_X_AXIS, TRADE_PROMPT_Y_AXIS))
        """
        
        # Write text
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
                image = pygame.image.load(TRADE_BUTTON_SPRITE)
                image = pygame.transform.scale_by(image, 1)
                window.blit(image, (TRADE_BUTTON_X_AXIS + 35, TRADE_BUTTON_Y_AXIS + player.trade_counter * (TRADE_BUTTON_HEIGHT + 25)))

                new_button = Button(card, TRADE_BUTTON_X_AXIS + 35, TRADE_BUTTON_Y_AXIS + player.trade_counter * (TRADE_BUTTON_HEIGHT + 25), image, 1)
                new_button.card = card
                player.trade_button.append(new_button)

                # Draw the button images
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

    def __init__(self):
        self.showing = False
        self.current_trade_button = None

        self.trade_2_buttons = {
			"Wood": Button,
			"Wheat": Button,
			"Sheep": Button,
			"Brick": Button,
			"Ore": Button,
            "Exit": Button
		} 

    def create_trade_prompt_buttons(self):
        # Bricks trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Brick", TRADE_POSITION_X_RIGHT - 10, TRADE_POSITION_Y_DOWN - 7, button_img, 1)

        self.trade_2_buttons["Brick"] = button
        
        # Lumber trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Wood", TRADE_POSITION_X_RIGHT + CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7, button_img, 1)
        
        self.trade_2_buttons["Wood"] = button

        # Ore trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Ore", TRADE_POSITION_X_RIGHT + 2 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7, button_img, 1)

        self.trade_2_buttons["Ore"] = button

        # Grain trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Wheat", TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7, button_img, 1)

        self.trade_2_buttons["Wheat"] = button

        # Wool trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Sheep", TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 8, TRADE_POSITION_Y_DOWN - 7, button_img, 1)

        self.trade_2_buttons["Sheep"] = button

        # Exit trade from bank button
        button_img = pygame.image.load(EXIT_BUTTON_SPRITE)
        button = Button("Exit", TRADE_POSITION_X + 360, TRADE_POSITION_Y + 30, button_img, 0.7)

        self.trade_2_buttons["Exit"] = button


    def show_trade_prompt(self, window, player, trade_button):
        # Draw prompt rectangle
        # pygame.draw.rect(window, BRASS, TradePrompt.trade_prompt_rect)

        image = pygame.image.load(WOOD_TABLE_DARK_SPRITE)
        image = pygame.transform.scale_by(image, 1.2)
        window.blit(image, (TRADE_POSITION_X, TRADE_POSITION_Y + 20))

        # Write prompt text
        text = Trade.medium_font.render("Trade three " + trade_button.card + " cards for one chosen card", True, WHITE)
        text_rect = pygame.Rect(TRADE_POSITION_X + 20, TRADE_POSITION_Y + 80, 40, 20)
        window.blit(text, text_rect)

        # Draw Exit Button
        image = pygame.image.load(EXIT_BUTTON_SPRITE)
        image = pygame.transform.scale_by(image, 0.7)
        window.blit(image, (TRADE_POSITION_X + 360, TRADE_POSITION_Y + 30))


        # Draw Brick Card
        image = pygame.image.load(SMALL_BUTTON_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT - 10, TRADE_POSITION_Y_DOWN - 7))

        image = pygame.image.load(BRICKS_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT - 5, TRADE_POSITION_Y_DOWN))


        # Draw Lumber Card
        image = pygame.image.load(SMALL_BUTTON_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7))

        image = pygame.image.load(LUMBER_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + CARDS_SPACING_HELPER + 2, TRADE_POSITION_Y_DOWN))


        # Draw Ore Card
        image = pygame.image.load(SMALL_BUTTON_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 2 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7))

        image = pygame.image.load(ORE_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 2 * CARDS_SPACING_HELPER + 3, TRADE_POSITION_Y_DOWN + 5))

        
        # Draw Grain Card
        image = pygame.image.load(SMALL_BUTTON_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7))

        image = pygame.image.load(GRAIN_SPRITE)
        image = pygame.transform.scale_by(image, 0.9)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER + 3, TRADE_POSITION_Y_DOWN + 7))


        # Draw Wool Card
        #pygame.draw.rect(window, WOOL_COLOR, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER, TRADE_POSITION_Y_DOWN, CARD_WIDTH, CARD_HEIGHT), 0)
        image = pygame.image.load(SMALL_BUTTON_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 8, TRADE_POSITION_Y_DOWN - 7))

        image = pygame.image.load(WOOL_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 3, TRADE_POSITION_Y_DOWN + 3))

    @staticmethod
    def show_pressed_trade_2_button(window, button_name):
        if button_name == "Exit":
            # Draw pressed Exit Button
            image = pygame.image.load(PRESSED_EXIT_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 0.7)
            window.blit(image, (TRADE_POSITION_X + 360, TRADE_POSITION_Y + 30))

        elif button_name == "Brick":
            # Draw Brick Card
            image = pygame.image.load(PRESSED_SMALL_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT - 10, TRADE_POSITION_Y_DOWN - 7))

            image = pygame.image.load(PRESSED_BRICKS_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT - 5, TRADE_POSITION_Y_DOWN))

        elif button_name == "Wood":
            # Draw Lumber Card
            image = pygame.image.load(PRESSED_SMALL_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7))

            image = pygame.image.load(PRESSED_LUMBER_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + CARDS_SPACING_HELPER + 2, TRADE_POSITION_Y_DOWN))

        elif button_name == "Ore":
            # Draw Ore Card
            image = pygame.image.load(PRESSED_SMALL_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 2 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7))

            image = pygame.image.load(PRESSED_ORE_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 2 * CARDS_SPACING_HELPER + 3, TRADE_POSITION_Y_DOWN + 5))

        elif button_name == "Wheat":
            # Draw pressed Grain Card
            image = pygame.image.load(PRESSED_SMALL_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7))

            image = pygame.image.load(PRESSED_GRAIN_SPRITE)
            image = pygame.transform.scale_by(image, 0.9)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER + 3, TRADE_POSITION_Y_DOWN + 7))

        elif button_name == "Sheep":
            # Draw pressed Wool Card
            image = pygame.image.load(PRESSED_SMALL_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 8, TRADE_POSITION_Y_DOWN - 7))

            image = pygame.image.load(PRESSED_WOOL_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 3, TRADE_POSITION_Y_DOWN + 3))

trade_prompt = TradePrompt()