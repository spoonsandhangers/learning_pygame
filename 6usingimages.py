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


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [480, 448]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Fab Fish")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #load the background image outside the game loop
    background_image = pygame.image.load("Underwater_blue_bubbles.jpg").convert()
    player_image = pygame.image.load("fishTile_080.png").convert()
    click_sound = pygame.mixer.Sound("pop.ogg")

    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0

    # Current player position
    x_coord = 20
    y_coord = 224
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
             # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3
                elif event.key == pygame.K_SPACE:
                    click_sound.play()

            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # Move the object according to the speed vector.
        x_coord += x_speed
        y_coord += y_speed
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        #draws the image on the screen
        screen.blit(background_image, [0, 0])
        screen.blit(player_image, [x_coord, y_coord])
        player_image.set_colorkey(BLACK)
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
