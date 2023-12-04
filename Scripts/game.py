# Importing modules
from constants import *
import base_game_cls as base
from base_game_cls import *
from board_elements.settlement import Settlement
from Scripts.board_elements.road import Road, roads

# Importing player
from Scripts.player.player import Player

# Importing events
from Scripts.events.settlement_events import SettlementEventHandler
from Scripts.events.road_events import RoadEventHandler


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
    @staticmethod
    def main(window):

        # Game loop variables
        dice_first_dsp = True
        running = True
        roll = [0, 0]

        # --- Background ---
        window.fill(c.LIGHT_CYAN_BLUE)

        # --- Hexagon grid ---
        base.HexagonTile.create_hexagon_grid(window, c.HEXAGON_X_AXIS, c.HEXAGON_Y_AXIS)

        print(base.HexagonTile.resourcesArray)
        print(base.HexagonTile.center_points)

        # --- Settlement Surfaces ---
        Settlement.prepare_board_surfaces(window, base.HexagonTile.distinct_vertices, base.HexagonTile.hexagons)

        # --- Roads ---

        # --- Player ---
        player = Player()

        while running:
            # --- Roads ---
            if len(roads) != 0:
                current_road = roads[-1]
            else:
                current_road = Road()
                roads.append(current_road)

            if current_road.is_placed is True:  # If we successfully placed a road, prepare a new one
                roads.append(Road())

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

                    # TODO: after first click
                    for center_point in base.HexagonTile.center_points:
                        if center_point[0] - c.HEXAGON_SIDE / 3 <= mouse_pos[0] <= center_point[0] + c.HEXAGON_SIDE / 3:
                            if center_point[1] - c.HEXAGON_SIDE / 3 <= mouse_pos[1] <= \
                                    center_point[1] + c.HEXAGON_SIDE / 3:
                                print("Trying")
                                if base.Robber.check_move(mouse_pos):
                                    print("Moving")
                                    base.Robber.move_robber(window, center_point[0], center_point[1])
                            # base.HexagonTile.create_hexagon_grid(window, c.HEXAGON_X_AXIS, c.HEXAGON_Y_AXIS, False)
                            # TODO: Move robber

                    # Prepare settlement event
                    SettlementEventHandler.place_settlement(window, Settlement.settlements, player, "prepared")

                    # Place road event
                    RoadEventHandler.place_road(window, event, Settlement.settlements, current_road, player, "press")

                elif event.type == pygame.MOUSEBUTTONUP:
                    # Release road event
                    print("entered")

                    # If placing the road was unsuccessful, remove it from the list
                    if RoadEventHandler.place_road(window, event, Settlement.settlements, current_road, player, "release") == -1:
                        roads.pop()
                    else:
                        print(current_road.is_dragged)

                    # Place settlement event
                    SettlementEventHandler.place_settlement(window, Settlement.settlements, player, "placing")

                elif event.type == pygame.MOUSEMOTION:
                    # Dragging road event
                    RoadEventHandler.place_road(window, event, Settlement.settlements, current_road, player, "dragging")

                    # Hover settlement event TODO
                    # SettlementEventHandler.hover_settlement(window)

            # --- Dice ---

            dice_btn = base.Board.roll_dice_btn(window)

            if dice_first_dsp:
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
