# Catan - Pygame Implementation

Welcome to the Pygame implementation of the classic board game Catan! This project aims to bring the joy of Catan to your computer screen using the Pygame library. Feel free to explore the code and contribute to the development.

## Table of Contents

- [Catan - Pygame Implementation](#catan---pygame-implementation)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Description](#description)
  - [Work done so far](#work-done-so-far)

## Installation

1. Clone the repository
2. Install the dependencies using `pip install -r requirements.txt`
3. Enter the `Scripts` directory
4. Run the game using `python menu.py`
5. Enjoy!

## Description

This project aims to bring the joy of Catan to your computer screen using the Pygame library.

- Creating the board
    - The board is created using a hexagonal grid system. Each hexagon is a separate object, which is stored in a list. The hexagons are then drawn on the screen using the coordinates of their center. Each hexagon has a type (wood, brick, sheep, wheat, stone, desert) and a number (2-12, excluding 7). The hexagons are randomly generated. The hexagons have a surface, which is used to stretch the image of the hexagon to the desired size.

- Creating the dice
    - The dice respects the same concept. They are drawn on the screen and randomly generated. They also have a button event handler, which is used to roll the dice.

- Creating the menu
    - The menu is simplstic one. It has 3 buttons: Play, Options and Quit. The Play button starts the game, the Options button opens the settings menu and the Quit button quits the game. Also pygame.mixer is used to play the background music.

- Creating the robber
    - The robber gets the position of the desert hexagon and is placed on it. It uses the sum roll of the dice to move to the next hexagon. It has a separate event handler, which forces the player to move the robber beside the current possition. After the robber is moved, all the players lose half of their resources.


## Work done so far

-> Robert
- [x] Created the template for the project
- [x] Added some TODOs
- [x] Created the dice class
- [x] Created the hexagon class
- [x] Created the menu class
- [x] Added the constants for each class I worked on
- [x] Created the robber class
- [x] Restructured the project

-> Anca

-> 🐝 Trifu
- [x] Implemented Settlement class & Event Handler
- [x] Implemented Road class & Event Handler
- [x] Implemented Card system
