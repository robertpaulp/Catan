# Importing modules
import pygame
import constants as c
import menu

class Options:
    
    # --- Main loop ---
    @staticmethod
    def main(window):

        # Game loop variables
        dice_first_dsp = True
        running = True
        roll = [0, 0]

        # --- Background ---
        background = pygame.image.load(c.BACKGROUND_PATH)
        background = pygame.transform.scale(background, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        window.blit(background, (0, 0))

        # --- Buttons ---
        music_btn_pos = (c.MUSIC_BTN_X_AXIS, c.MUSIC_BTN_Y_AXIS)
        music_btn = menu.Menu.button(window, c.MUSIC_BTN_X_AXIS, c.MUSIC_BTN_Y_AXIS, c.MUSIC_TEXT, c.BLACK, c.TRANSPARENT_WHITE, c.MUSIC_SIZE, c.FONT_PATH)

        # Back Button
        back_btn_pos = (c.BACK_BTN_X_AXIS, c.BACK_BTN_Y_AXIS)
        back_btn = menu.Menu.button(window, c.BACK_BTN_X_AXIS, c.BACK_BTN_Y_AXIS, c.BACK_TEXT, c.BLACK, c.TRANSPARENT_WHITE, c.BACK_SIZE, c.FONT_PATH)
        
        while running:
            # --- Event loop ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_btn.get_rect(topleft=back_btn_pos).collidepoint(mouse_pos):
                        menu.Menu.main()
                        exit()
                    elif music_btn.get_rect(topleft=music_btn_pos).collidepoint(mouse_pos):
                        if c.MUSIC:
                            c.MUSIC = False
                            pygame.mixer.music.pause()
                        else:
                            c.MUSIC = True
                            pygame.mixer.music.unpause()

            pygame.display.update()

        pygame.quit()
