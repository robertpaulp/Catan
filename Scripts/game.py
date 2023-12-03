# Importing modules
import pygame
import constants as c
import base_game_cls as base
from base_game_cls import *
from board_elements.settlement import *
import random
from events import *

window = None


def redraw_board(window):  # TODO: maybe turn static
    """ Redraw assets in case of necessary board changes

    :return:
    """

    window.fill(c.LIGHT_CYAN_BLUE)

    # Remove robber
    base.HexagonTile.create_hexagon_grid(window, c.HEXAGON_X_AXIS, c.HEXAGON_Y_AXIS, False)
    # TODO: Move robber

    for settlement in Settlement.settlements:
        if settlement.is_placed is True:
            settlement.draw_settlement(window)

            window.blit(settlement.image,
                        (settlement.position[0] - SETTLEMENT_SPRITE, settlement.position[1] - SETTLEMENT_SPRITE))
            pygame.display.update()


class Game:
    @staticmethod
    def window_setup():
        pygame.init()

        window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Catan")
        icon = pygame.image.load("../Assets/icon.png")
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)

        return window

    # --- Main loop ---
    def main(window):

        # Game loop variables
        dice_first_dsp = True
        running = True
        roll = [0, 0]

        opacity = 255

        # --- Background ---
        window.fill(c.LIGHT_CYAN_BLUE)

        # --- Hexagon grid ---
        base.HexagonTile.create_hexagon_grid(window, c.HEXAGON_X_AXIS, c.HEXAGON_Y_AXIS)

        print(base.HexagonTile.resourcesArray)
        print(base.HexagonTile.center_points)

        while running:
            # --- Settlement ---
            settlement_locations = Settlement.prepare_board_surfaces(window, HexagonTile.hexagon_points, 0)

            # --- Event loop ---

            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if dice_btn.collidepoint(mouse_pos):
                        roll = [base.Dice.dice_roll(), base.Dice.dice_roll()]

                        if sum(roll) == 7:
                            print("Robber")
                            redraw_board(window)

                    # Place settlement event
                    SettlementEventHandler.handle_settlement_placement(window)

                # elif event.type == pygame.MOUSEMOTION: # TODO: rethink hover mode / work with sprites!
                # SettlementHover.trigger(window)



            # --- Dice ---

            dice_btn = base.Board.roll_dice_btn(window)

            if dice_first_dsp:
                base.Robber.create_robber(window, c.HEXAGON_X_AXIS, c.HEXAGON_Y_AXIS)
                base.Dice.dices(window, [1, 1])
                dice_first_dsp = False

            base.Dice.dices(window, roll)

            pygame.display.update()

        pygame.quit()

    # TODO: remove this after testing
    if __name__ == "__main__":
        window = window_setup()
        main(window)
        exit()