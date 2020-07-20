
"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

#set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sarah's interesting game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Screen-clearing code goes here


    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # --- Drawing code should go here

    # Draw on the screen a green line from (0, 0) to (100, 100)
    # that is 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0,0],[100,100],5)

    # Draw on the screen several lines from (0, 10) to (100, 110)
    # 5 pixels wide using a while loop
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
        y_offset = y_offset + 10

    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen,BLACK,[110, 110+y_offset],[210,110+y_offset],5)


    # For this code, make sure to have a line that says
    # "import math" at the top of your program. Otherwise
    # it won't know what math.sin is.

    for i in range(200):

        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200

        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)
        pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
