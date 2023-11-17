# Importing modules
import pygame
import constants as c
import base_game_cls as base
import game


class Menu:
    def button(window, x, y, width, height, text, text_color, color, font_size, font_type):
        button  = pygame.draw.rect(window, color, (x, y, width, height))
        font = pygame.font.Font(font_type, font_size)
        text = font.render(text, True, text_color)
        text_rect = text.get_rect(center=(x + width / 2, y + height / 2))
        window.blit(text, text_rect)

        return button


    def text(window, text, text_color, color, font_size, font_type):
        font = pygame.font.Font(font_type, font_size)
        text = font.render(text, True, text_color)
        window.blit(
            text,
            (
                c.SCREEN_WIDTH / 2 - text.get_width() / 2,
                c.SCREEN_HEIGHT / 2 - text.get_height() / 2 - 200,
            ),
        )


    # --- Main loop ---
    def main():
        window = game.Game.window_setup(Menu)

        # --- Background ---
        background = pygame.image.load("../Assets/Catan_1920x1080.jpg")
        background = pygame.transform.scale(background, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        window.blit(background, (0, 0))

        # --- Title ---
        Menu.text(window, c.TITLE_TEXT, c.WHITE, c.BLACK, 100, c.FONT_PATH)

        # -- Short description ---
        Menu.text(window, "A game of wonders...", c.WHITE, c.BLACK, 50, c.FONT_PATH)

        # Game loop variables
        running = True

        while running:
            # --- Event loop ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            # --- Buttons ---
            # Play button
            Menu.button(window, c.PLAY_BTN_X_AXIS, c.PLAY_BTN_Y_AXIS, c.PLAY_BTN_WIDTH, c.PLAY_BTN_HEIGHT, c.PLAY_TEXT, c.WHITE, c.TRANSPARENT, c.PLAY_SIZE, c.FONT_PATH)
            # Options button
            
            # Quit button
            

            pygame.display.update()


if __name__ == "__main__":
    Menu.main()
