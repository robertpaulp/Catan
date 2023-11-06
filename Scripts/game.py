# Importing modules
import pygame
import constants as c
import base_game_cls as base
import random


class Game:
    def main():
        # --- Main loop ---
        pygame.init()

        # Window
        window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        # Game loop
        dice_first_dsp = True
        running = True
        roll = [0, 0]

        # --- Background ---
        window.fill(c.LIGHT_CYAN_BLUE)

        # --- Hexagon grid ---
        hexagon_numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, -1]
        hexagon_numbers.sort(key=lambda x: random.random())
        base.HexagonTile.create_hexagon_grid(
            window, c.HEXAGON_X_AXIS, c.HEXAGON_Y_AXIS, hexagon_numbers
        )

        while running:
            # --- Event loop ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if dice_btn.collidepoint(mouse_pos):
                        roll = [base.Dice.dice_roll(), base.Dice.dice_roll()]

                        if sum(roll) == 7:
                            print("Robber")
                            # TODO: Move robber

            # --- Dice ---
            dice_btn = base.Board.roll_dice_btn(window)

            if dice_first_dsp:
                base.Dice.dices(window, [1, 1])
                dice_first_dsp = False

            base.Dice.dices(window, roll)

            pygame.display.update()

        pygame.quit()

    if __name__ == "__main__":
        main()
