# Importing modules
import pygame
import constants as c
import base_game_cls as base

class Game:

    def main():
        # --- Main loop ---
        pygame.init()

        # Window
        window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        # Game loop
        dice_set = True
        running = True
        while running:
            # --- Event loop ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the window with white
            window.fill(c.LIGHT_CYAN_BLUE)

            # Draw the hexagon grid
            base.HexagonTile.create_hexagon_grid(window, c.HEXAGON_X_AXIS, c.HEXAGON_Y_AXIS)


            # Draw the dice
            base.Dice.dice(window)
            base.Dice.dice(window,c.DICE_X_AXIS + 90)


            if dice_set:
                pygame.display.update()
                dice_set = False


        pygame.quit()



    if __name__ == "__main__":
        main()