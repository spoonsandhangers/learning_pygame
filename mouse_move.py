"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def snowman(screen,x,y):
    pygame.draw.ellipse(screen,WHITE,[x -25 ,y -25, 50, 50])
    pygame.draw.ellipse(screen,WHITE, [x - 50, y +22, 100, 100])
    pygame.draw.ellipse(screen,BLACK,[x -10 ,y -10, 5,5])
    pygame.draw.ellipse(screen,BLACK,[x +10 ,y -10, 5,5])
    pygame.draw.line(screen,BLACK,[x-10,y+10],[x+10, y+10],3)

"""
Find the smallest x value, and the smallest y value. Then subtract that value from each x and y in the function. Don't mess with the height and width values. Here's an example where we subtracted the smallest x and y values:

Third attempt at stickfigure function
smallest values were 95 for x and 83 for y.
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK,[96-95+x,83-83+y,10,10],0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [100-95+x,100-83+y], [105-95+x,110-83+y], 2)
    pygame.draw.line(screen, BLACK, [100-95+x,100-83+y], [95-95+x,110-83+y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [100-95+x,100-83+y], [100-95+x,90-83+y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [100-95+x,90-83+y], [104-95+x,100-83+y], 2)
    pygame.draw.line(screen, RED, [100-95+x,90-83+y], [96-95+x,100-83+y], 2)
Or, to make a program simpler, do the subtraction yourself:
"""
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)

    # Legs
    pygame.draw.line(screen, BLACK ,[5+x,17+y], [10+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)

    # Body
    pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
    pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)

def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        pygame.mouse.set_visible(False)
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        draw_stick_figure(screen, x, y)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT



        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == "__main__":
    main()
