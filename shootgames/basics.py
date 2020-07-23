"""
Basic construction of a game that is a horizontal
shooting game.
A fish eventually will shoot bubbles at enemies
To kill them.
This is just the frame work without graphics etc.
"""
import pygame
import random

#Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# ---- Classes

class Enemy(pygame.sprite.Sprite):
    """This class represents the ememies"""
    def __init__(self, color, height, width, screen_width, screen_height):
        super().__init__()

        self.image = pygame.Surface([height,width])
        self.image.fill(color)
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 5

        if self.rect.x < 0:
            self.rect.x = self.screen_width + 5
            self.rect.y = random.randrange(0,self.screen_height)

class Player(pygame.sprite.Sprite):
    """ The sprite that the player controls
    This will eventually be a fish I think"""
    def __init__(self, color, height, width, screen_width, screen_height):
        super().__init__()

        self.image = pygame.Surface([height,width])
        self.image.fill(color)
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = screen_height // 2

    def moveup(self):
        self.rect.y = +5

    def movedown(self):
        self.rect.y = -5


def main():
    """ Main function for the game. """
    #Initialize pygame
    pygame.init()

    # Set the width and height of the screen [width,height]
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])

    #Set widow name
    pygame.display.set_caption("My Game")

    # ----- Sprite lists

    #All the sprites in the game
    all_spites_list = pygame.sprite.Group()

    #All the ememies
    enemy_list = pygame.sprite.Group()

    # ----- Create the sprites
    for i in range(20):
        #This represents an ememy
        enemy = Enemy(BLUE, 10, 10, screen_width, screen_height)

        #set a random location at the right of the screen
        #for the ememy to appear.
        enemy.rect.y = random.randrange(screen_height)
        enemy.rect.x = random.randrange(screen_width + 5, screen_width*2)

        #add the enemies to the list of sprites
        #and the list of enemies.
        enemy_list.add(enemy)
        all_spites_list.add(enemy)

    player = Player(RED,15,5,screen_width,screen_height)
    all_spites_list.add(player)

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
        all_spites_list.update()
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        all_spites_list.draw(screen)

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
