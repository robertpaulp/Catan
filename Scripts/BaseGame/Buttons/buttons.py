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
        self.hover = False

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
        button = Button("settlement", SCREEN_WIDTH - 750, SCREEN_HEIGHT - 70, button_img, 1)
        return button

    @staticmethod
    def create_road_button():
        button_img = pygame.image.load(ROAD_BUTTON_SPRITE).convert_alpha()
        button = Button("road", SCREEN_WIDTH - 570, SCREEN_HEIGHT - 70, button_img, 1)
        return button
    
    @staticmethod
    def show_pressed_settlement_button(window):
        button_img = pygame.image.load(PRESSED_SETTLEMENT_BUTTON_SPRITE).convert_alpha()
        button = Button("settlement", SCREEN_WIDTH - 750, SCREEN_HEIGHT - 70, button_img, 1)
        window.blit(button_img, (button.rect.x, button.rect.y))

    @staticmethod
    def show_pressed_road_button(window):
        button_img = pygame.image.load(PRESSED_ROAD_BUTTON_SPRITE).convert_alpha()
        button = Button("road", SCREEN_WIDTH - 570, SCREEN_HEIGHT - 70, button_img, 1)
        window.blit(button_img, (button.rect.x, button.rect.y))

    # Hovering feature
    @staticmethod
    def show_settlement_info(window):
        image = pygame.image.load(PAPIRUS_SETTLEMENT_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (SCREEN_WIDTH - 753, SCREEN_HEIGHT - 190))

    @staticmethod
    def show_road_info(window):
        image = pygame.image.load(PAPIRUS_ROAD_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (SCREEN_WIDTH - 573, SCREEN_HEIGHT - 190))

    @staticmethod
    def create_end_turn_button():
        button_img = pygame.image.load(END_TURN_BUTTON_SPRITE).convert_alpha()
        button = Button("end_turn", SCREEN_WIDTH - 390, SCREEN_HEIGHT - 70, button_img, 1)
        return button
    
    @staticmethod
    def show_pressed_end_turn_button(window):
        button_img = pygame.image.load(PRESSED_END_TURN_BUTTON_SPRITE).convert_alpha()
        button = Button("end_turn", SCREEN_WIDTH - 390, SCREEN_HEIGHT - 70, button_img, 1)
        window.blit(button_img, (button.rect.x, button.rect.y))
    
    def show_pressed_trade_button(self, window, card):
        if(card == "Bricks"):
            image = pygame.image.load(TRADE_BUTTON_BRICKS_PRESSED_SPRITE)
        if(card == "Lumber"):
            image = pygame.image.load(TRADE_BUTTON_LUMBER_PRESSED_SPRITE)
        if(card == "Ore"):
            image = pygame.image.load(TRADE_BUTTON_ORE_PRESSED_SPRITE)
        if(card == "Grain"):
            image = pygame.image.load(TRADE_BUTTON_GRAIN_PRESSED_SPRITE)
        if(card == "Wool"):
            image = pygame.image.load(TRADE_BUTTON_WOOL_PRESSED_SPRITE)

        image = pygame.transform.scale_by(image, 1)
        window.blit(image, self.rect)


class Trade:
    trade_rect = pygame.Rect(TRADE_PROMPT_X_AXIS, TRADE_PROMPT_Y_AXIS, TRADE_PROMPT_WIDTH, TRADE_PROMPT_HEIGHT)

    card_color = {
      "Lumber": (3, 75, 3),
      "Grain": (240, 215, 49),
      "Wool": (242, 240, 235),
      "Bricks": (188, 74, 60),
      "Ore": (144, 144, 144)
    } 

    card_sprite = {
      "Lumber": LUMBER_SPRITE,
      "Grain": GRAIN_SPRITE,
      "Wool": WOOL_SPRITE,
      "Bricks": BRICKS_SPRITE,
      "Ore": ORE_SPRITE
    } 

    pygame.font.init()
    font = pygame.font.SysFont('Segoe UI Black', 25)
    font2 = pygame.font.SysFont('Segoe UI Black', 22)
    font_numbers = pygame.font.SysFont('Arial', 25)
    small_font = pygame.font.SysFont('Segoe UI Black', 15)
    medium_font = pygame.font.SysFont('Segoe UI Black', 18)

    def show_trade(self, window, player):
        # Draw prompt scroll
        image = pygame.image.load(SCROLL_SPRITE)
        image = pygame.transform.scale_by(image, 1)
        window.blit(image, (TRADE_PROMPT_X_AXIS - 120, TRADE_PROMPT_Y_AXIS - 50))
        
        # Draw bank icon
        image = pygame.image.load(BANK_ICON_SPRITE)
        image = pygame.transform.scale_by(image, 0.85)
        window.blit(image, (TRADE_PROMPT_X_AXIS + 135, TRADE_PROMPT_Y_AXIS + 65))

        # Write text
        text = Trade.medium_font.render("TRADE", True, GRAY)
        text_rect = pygame.Rect(TRADE_PROMPT_X_AXIS + 128, TRADE_PROMPT_Y_AXIS + 110, TRADE_PROMPT_WIDTH, TRADE_PROMPT_HEIGHT)
        window.blit(text, text_rect)

        player.trade_counter = 0
        for card in player.cards:
            if player.possible_trade[card] == True:

                # Draw the trade button
                if(card == "Bricks"):
                    image = pygame.image.load(TRADE_BUTTON_BRICKS_SPRITE)
                if(card == "Lumber"):
                    image = pygame.image.load(TRADE_BUTTON_LUMBER_SPRITE)
                if(card == "Ore"):
                    image = pygame.image.load(TRADE_BUTTON_ORE_SPRITE)
                if(card == "Grain"):
                    image = pygame.image.load(TRADE_BUTTON_GRAIN_SPRITE)
                if(card == "Wool"):
                    image = pygame.image.load(TRADE_BUTTON_WOOL_SPRITE)

                image = pygame.transform.scale_by(image, 1)
                window.blit(image, (TRADE_BUTTON_X_AXIS, TRADE_BUTTON_Y_AXIS + 30 + player.trade_counter * (TRADE_BUTTON_HEIGHT)))

                new_button = Button(card, TRADE_BUTTON_X_AXIS, TRADE_BUTTON_Y_AXIS + 30 + player.trade_counter * (TRADE_BUTTON_HEIGHT), image, 1)
                new_button.card = card
                player.trade_button.append(new_button)

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
			"Lumber": Button,
			"Grain": Button,
			"Wool": Button,
			"Bricks": Button,
			"Ore": Button,
            "Exit": Button
		} 

    def create_trade_prompt_buttons(self):
        # Bricks trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Bricks", TRADE_POSITION_X_RIGHT - 10, TRADE_POSITION_Y_DOWN - 7, button_img, 1)

        self.trade_2_buttons["Bricks"] = button
        
        # Lumber trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Lumber", TRADE_POSITION_X_RIGHT + CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7, button_img, 1)
        
        self.trade_2_buttons["Lumber"] = button

        # Ore trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Ore", TRADE_POSITION_X_RIGHT + 2 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7, button_img, 1)

        self.trade_2_buttons["Ore"] = button

        # Grain trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Grain", TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7, button_img, 1)

        self.trade_2_buttons["Grain"] = button

        # Wool trade from bank button
        button_img = pygame.image.load(SMALL_BUTTON_SPRITE)
        button = Button("Wool", TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 8, TRADE_POSITION_Y_DOWN - 7, button_img, 1)

        self.trade_2_buttons["Wool"] = button

        # Exit trade from bank button
        button_img = pygame.image.load(EXIT_BUTTON_SPRITE)
        button = Button("Exit", TRADE_POSITION_X + 360, TRADE_POSITION_Y + 30, button_img, 0.7)

        self.trade_2_buttons["Exit"] = button


    def show_trade_prompt(self, window, player, trade_button):
        # Draw prompt rectangle

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

        elif button_name == "Bricks":
            # Draw Brick Card
            image = pygame.image.load(PRESSED_SMALL_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT - 10, TRADE_POSITION_Y_DOWN - 7))

            image = pygame.image.load(PRESSED_BRICKS_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT - 5, TRADE_POSITION_Y_DOWN))

        elif button_name == "Lumber":
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

        elif button_name == "Grain":
            # Draw pressed Grain Card
            image = pygame.image.load(PRESSED_SMALL_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER - 5, TRADE_POSITION_Y_DOWN - 7))

            image = pygame.image.load(PRESSED_GRAIN_SPRITE)
            image = pygame.transform.scale_by(image, 0.9)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 3 * CARDS_SPACING_HELPER + 3, TRADE_POSITION_Y_DOWN + 7))

        elif button_name == "Wool":
            # Draw pressed Wool Card
            image = pygame.image.load(PRESSED_SMALL_BUTTON_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 8, TRADE_POSITION_Y_DOWN - 7))

            image = pygame.image.load(PRESSED_WOOL_SPRITE)
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, (TRADE_POSITION_X_RIGHT + 4 * CARDS_SPACING_HELPER - 3, TRADE_POSITION_Y_DOWN + 3))

trade_prompt = TradePrompt()