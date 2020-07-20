"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
snow_list = []

for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    #This for loop draws each snowflake in the list.
    #for each cannot be used as the positions in the list
    #need to be modified
    for i in range(len(snow_list)):
       #Draw the snowflake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)

        #move the snow flake down one pixel
        snow_list[i][1] += 1

        #if the snow lake moves off the bottom of the screen
        if snow_list[i][1] > 400:
            #Reset it just above the top of the screen
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            #give it a new x position.
            x = random.randrange(0,400)
            snow_list[i][0]



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
