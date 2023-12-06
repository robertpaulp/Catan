import pygame

from Scripts.constants import *
from Scripts.base_game_cls import HexagonTile, Board, Dice
from Scripts.board_elements.settlement import Settlement, settlements, sprites
from Scripts.board_elements.road import Road, roads
from Scripts.player.player import Player, players


def redraw_board(window, roll, current_player=players[0]):  # TODO: maybe turn static
    """ Redraw assets in case of necessary board changes

    :return:
    """

    window.fill(LIGHT_CYAN_BLUE)

    dice_btn = Board.roll_dice_btn(window)

    if roll == [0, 0]:
        Dice.dices(window, [1, 1])

    Dice.dices(window, roll)

    # Remove robber
    HexagonTile.create_hexagon_grid(window, HEXAGON_X_AXIS, HEXAGON_Y_AXIS, False)
    # TODO: Move robber

    # Replace roads
    for road in roads:
        if road.is_placed is True:
            road.draw_road(window, road.color)

    # Replace settlements
    for settlement in settlements:
        if settlement.is_placed is True:
            settlement.draw_settlement(window, settlement.color)

            window.blit(settlement.image,
                        (settlement.position[0] - SETTLEMENT_SPRITE, settlement.position[1] - SETTLEMENT_SPRITE))
            pygame.display.update()

    # sprites.draw(window)
    # pygame.display.update()

    # Update player's resources
    current_player.draw_player(window)

