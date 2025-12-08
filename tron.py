"""
Tron Legacy - A two-player light cycle game
Requires: pip install freegames pygame

Controls:
- Player 1 (Red): 'a' to turn left, 's' to turn right
- Player 2 (Blue): 'i' to turn left, 'o' to turn right
- Press Space to start the game
"""

from turtle import *
from freegames import square, vector
import pygame

pygame.mixer.init()
pygame.mixer.music.load("tron legacy.mp3")
pygame.mixer.music.play(-1)

# Screen dimensions
screen_width = 1080
screen_height = 800

# Player 1 settings
p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

# Player 2 settings
p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()


def inside(head):
    """Return True if head inside screen."""
    x_inside = -screen_width / 2 < head.x < screen_width / 2
    y_inside = -screen_height / 2 < head.y < screen_height / 2
    return x_inside and y_inside


def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body:
        game_over('Player blue wins!')
        return

    if not inside(p2head) or p2head in p1body:
        game_over('Player red wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)


def draw_border():
    """Draw border according to screen size."""
    penup()
    goto(-screen_width / 2, -screen_height / 2)
    pendown()
    color('white')
    for _ in range(4):
        forward(screen_width)
        left(90)


def start_game():
    """Start the game."""
    clear()  # Clear the previous game state
    draw_border()  # Draw border
    draw()   # Start the game


def new_game():
    """Bind a key to start a new game."""
    listen()
    onkey(start_game, 'space')  # Bind the space key to start a new game
    onkey(lambda: p1aim.rotate(90), 'a')
    onkey(lambda: p1aim.rotate(-90), 's')
    onkey(lambda: p2aim.rotate(90), 'i')
    onkey(lambda: p2aim.rotate(-90), 'o')

    # Display instructions
    penup()  # Lift the pen up to prevent drawing
    goto(0, 100)  # Move to the desired position
    pendown()  # Put the pen down to start drawing
    color('blue')
    write('Player red: Press "a" to turn left, "d" to turn right', align='center', font=('Arial', 14, 'bold'))
    penup()
    goto(0, 70)
    pendown()
    color('red')
    write('Player blue: Press "j" to turn left, "l" to turn right', align='center', font=('Arial', 14, 'bold'))
    penup()
    goto(0, 40)
    pendown()
    color('blue')
    write('To start, press the space bar', align='center', font=('Arial', 14, 'bold'))


def game_over(message):
    """Display Game Over message."""
    clear()
    penup()
    goto(0, 0)
    pendown()
    color('white')
    write(message, align='center', font=('Arial', 40, 'bold'))


setup(screen_width, screen_height, 370, 0)
hideturtle()
tracer(False)
bgcolor('black')

new_game()  # Bind the new game function to the space key

done()  # Add this to keep the window open after the game ends
