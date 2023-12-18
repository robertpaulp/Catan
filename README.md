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

- Creating the buttons
    - Some of the buttons used in the game's interface are:
        -> The settlement button - by clicking it, the player demands to purchase a settlement.
        -> The road button - by clicking it, the player demands to purchase a road.
        -> The end turn button - by clicking it, the turn switches from the current player to the next one.
    - The buttons darken after being clicked.
    - The settlement button and the Road button have a hovering feature. By hovering over each of them, the player is reminded what resources are needed for buying a settlement or a road.

- Creating the Cards Prompt
    - The cards prompt, located at the bottom of the board, shows the number of each of the resources that the current player has. It updates every time the amount of resources changes (buying, trading, acquiring).

- Creating the Trade station
    - The Trade station, located at the left of the board, shows the possible trades the current player can make with the bank. If the current player has three cards the same type of resource, a trade button will appear.

- Creating the Trade Prompt
    - The trade prompt appears after the current player pushes one of the trade button. By doing so, the player can choose to trade three cards of the same type for another card of a chosen type.
    - The trade prompt gives the player the possibility to choose the card to get from the bank, or to end the transaction by clicking the Exit button.

- Creating the Errors
    - The implemented errors are:
        - "Insufficient error!" - appears if the current player does not have enough resources to buy a settlement or a road.
        - "Move the robber!" - appears if the current player gets 7 after rolling the dice and tries clicking buttons before moving the robber.
        - "Roll the dice!" - appears if the current player tries to end the turn without rolling the dice first.
        - "Place your settlements!" / "Place your roads!" / "Place yout settlements and roads!" - appear if the current player tries rolling the dice without placing two settlements and two roads in the Starting Round.
        - "You have already rolled the dice!" - appears if the current player tries rolling the dice a second time.

- Creating the Pop Ups
    - The pop ups implemented are: 
        -> The "Starting Round" pop up - appears at the beginning of the game.
        -> The Round number pop up that appears after every player has gotten a turn.
        -> The "Victory!" pop up that appears after a player has acquired a certain number of win points, winning the game. 

- Creating the Rounds
    - At the beginning, every player gets to place two settlements and two roads for free.

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
- [x] Implemented the "draw_players" method that creates the players'
total cards and win points display.
- [x] Implemented the Buttons class.
- [x] Implemented the Trade class.
- [x] Implemented the TradePrompt class.
- [x] Implemented the CardsPrompt class.
- [x] Implemented the Error class.
- [x] Implemented the Popup class.
- [x] Updated the User Interface design.
- [x] Implemented the "Rounds" feature

-> 🐝 Trifu
- [x] Implemented Settlement class
- [x] Implemented Road class
- [x] Implemented Card system
- [x] Implemented Event Handlers
- [x] Sketched initial Error behaviours 
- [x] Refactored code; added base class constructors
