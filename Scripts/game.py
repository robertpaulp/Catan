# Importing modules
import pygame
import constants as c

class Game:

    def main():
        # --- Main loop ---
        pygame.init()

        # Window
        window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        # Game loop
        running = True
        while running:
            # --- Event loop ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the window with white
            window.fill(c.LIGHT_CYAN_BLUE)

            pygame.display.update()


        pygame.quit()



    if __name__ == "__main__":
        main()