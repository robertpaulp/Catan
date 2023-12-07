# Importing modules
import pygame
import constants as c
import game
import options


class Menu:
    def button(window, x, y, text, text_color, bg_color, font_size, font_type):

        font = pygame.font.Font(font_type, font_size)
        text_surface = font.render(text, True, text_color)

        width = text_surface.get_width() + 20
        height = text_surface.get_height() + 10

        button = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(button, bg_color, (0, 0, width, height))

        text_rect = text_surface.get_rect(center=(width / 2, height / 2))

        button.blit(text_surface, text_rect)
        window.blit(button, (x, y))

        return button


    def text(window, text, text_color, font_size, font_type, x, y):
        font = pygame.font.Font(font_type, font_size)
        text = font.render(text, True, text_color)
        window.blit(
            text,
            (x - text.get_width() / 2, y - text.get_height() / 2
            ),
        )



    # --- Main loop ---
    def main():
 
        # --- Window setup ---
        window = game.Game.window_setup()

        # --- Background ---
        background = pygame.image.load(c.BACKGROUND_PATH)
        background = pygame.transform.scale(background, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        window.blit(background, (0, 0))

        # --- Background Music ---
        pygame.mixer.music.load(c.MUSIC_PATH)
        pygame.mixer.music.play(-1)

        # --- Title ---
        Menu.text(window, c.TITLE_TEXT, c.BLACK, 100, c.FONT_PATH, c.TITLE_X_AXIS, c.TITLE_Y_AXIS)

        # -- Short description ---
        Menu.text(window, c.SHORT_DESCRIPTION_TEXT, c.BLACK, 35, c.FONT_PATH, c.TITLE_X_AXIS + 200, c.TITLE_Y_AXIS + 70)

        # --- Buttons ---

        # Play button
        btn_play_pos = (c.PLAY_BTN_X_AXIS, c.PLAY_BTN_Y_AXIS)
        btn_play = Menu.button(window, c.PLAY_BTN_X_AXIS, c.PLAY_BTN_Y_AXIS, c.PLAY_TEXT, c.BLACK, c.TRANSPARENT_WHITE, c.PLAY_SIZE, c.FONT_PATH)
        # Options button
        btn_options_pos = (c.OPTIONS_BTN_X_AXIS, c.OPTIONS_BTN_Y_AXIS)
        btn_options = Menu.button(window, c.OPTIONS_BTN_X_AXIS, c.OPTIONS_BTN_Y_AXIS, c.OPTIONS_TEXT, c.BLACK, c.TRANSPARENT_WHITE, c.OPTIONS_SIZE, c.FONT_PATH)
        # Quit button
        btn_quit_pos = (c.QUIT_BTN_X_AXIS, c.QUIT_BTN_Y_AXIS)
        btn_quit = Menu.button(window, c.QUIT_BTN_X_AXIS, c.QUIT_BTN_Y_AXIS, c.QUIT_TEXT, c.BLACK, c.TRANSPARENT_WHITE, c.QUIT_SIZE, c.FONT_PATH)

        # Game loop variables
        running = True

        while running:
            # --- Event loop ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if btn_play.get_rect(topleft=btn_play_pos).collidepoint(mouse_pos):
                        pygame.mixer.music.stop()
                        game.Game.main(window)
                        exit()
                    elif btn_options.get_rect(topleft=btn_options_pos).collidepoint(mouse_pos):
                        options.Options.main(window)
                        exit()
                    elif btn_quit.get_rect(topleft=btn_quit_pos).collidepoint(mouse_pos):
                        running = False


            pygame.display.update()


if __name__ == "__main__":
    Menu.main()
