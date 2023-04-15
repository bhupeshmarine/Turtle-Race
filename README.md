# Turtle-Race-Game

This is a simple game built using Python and the Turtle graphics library. The objective of the game is to move a turtle around the screen and collect as many coins as possible while avoiding obstacles.

# Getting Started
To run the game, you will need Python 3.x installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

You will also need to install the Turtle graphics library. To do this, open a terminal or command prompt and enter the following command:

# Copy code
pip install turtle
Once you have installed Python and the Turtle graphics library, you can run the game by opening a terminal or command prompt, navigating to the directory where the game files are located, and entering the following command:

# css
Copy code
python main.py
How to Play
When you start the game, you will see a turtle and several coins on the screen. To move the turtle, use the arrow keys on your keyboard. To collect a coin, simply move the turtle over the coin.

If you collide with an obstacle, such as a wall or a moving enemy, you will lose a life. You start the game with three lives, and if you lose all your lives, the game will end.

Your score is displayed at the top of the screen, and it increases each time you collect a coin. The game ends when you have collected all the coins on the screen.

# Customization
If you want to customize the game, you can modify the following variables in the config.py file:

WINDOW_WIDTH and WINDOW_HEIGHT: The width and height of the game window, in pixels.
TURTLE_SPEED and ENEMY_SPEED: The speed of the turtle and the enemies, respectively.
COIN_COUNT and ENEMY_COUNT: The number of coins and enemies on the screen, respectively.
COIN_VALUE: The number of points you earn for collecting a coin.
You can also modify the images used in the game by replacing the .gif files in the images folder.
