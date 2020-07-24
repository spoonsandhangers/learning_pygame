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
GREEN = (66, 245, 96)

screen_width = 800
screen_height = 533



# ---- Classes
class Enemy(pygame.sprite.Sprite):
    """ This class is the enemy parent class"""
    def __init__(self):
        super().__init__()
        # self.screen_width = screen_width
        # self.screen_height = screen_height
        # self.width = 10
        # self.height = 10
        # self.color = BLACK
        self.speed = 5
        self.image = pygame.transform.flip(pygame.image.load("fishTile_074s.png").convert(),True,False)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= self.speed

        if self.rect.x < 0:
            self.rect.x = screen_width + 5
            self.rect.y = random.randrange(0,screen_height)

class Enemy_common(Enemy):
    """This class represents the ememies"""
    def __init__(self, speed):
        super().__init__()
        # self.image = pygame.image.load("fishTile_074.png").convert()
        # self.image.set_colorkey(BLACK)
        # self.rect = self.image.get_rect()
        #self.image = pygame.Surface([height,width])
        #self.image.fill(color)
        self.speed = speed

        #self.rect = self.image.get_rect()



class Rand_enemy(Enemy):

    def __init__(self):
        super().__init__()
        # self.height = random.randrange(5,20)
        # self.width = random.randrange(5,20)
        self.speed = random.randrange(2,10)
        # self.image = pygame.image.load("fishTile_074.png").convert()
        # self.image.set_colorkey(BLACK)
        # self.rect = self.image.get_rect()
        #self.image = pygame.Surface([self.height,self.width])
        #self.image.fill(color)

        #self.rect = self.image.get_rect()







class Treasure(pygame.sprite.Sprite):
    """These sprites should be collected so that you score points"""
    def __init__(self, color, height, width, speed):
        super().__init__()
        self.image = pygame.Surface([height,width])
        self.image.fill(color)
        self.speed = speed

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= self.speed

        if self.rect.x < 0:
            self.rect.x = screen_width + 5
            self.rect.y = random.randrange(0,screen_height)





class Player(pygame.sprite.Sprite):
    """ The sprite that the player controls
    This will eventually be a fish I think"""
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("fishTile_080.png").convert()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.x = 20
        self.rect.y = screen_height // 2


def main():
    """ Main function for the game. """
    #Initialize pygame
    pygame.init()

    # Set the width and height of the screen [width,height]
    screen = pygame.display.set_mode([screen_width, screen_height])

    background_image = pygame.image.load("Underwater_bubbles.jpg").convert()


    click_sound = pygame.mixer.Sound("pop.ogg")

    #Set widow name
    pygame.display.set_caption("My Game")

    #set score to 0
    score = 0

    # ----- Sprite lists

    #All the sprites in the game
    all_spites_list = pygame.sprite.Group()

    #All the ememies
    enemy_list = pygame.sprite.Group()

    #All the treasure
    treasure_list = pygame.sprite.Group()

    # ----- Create the sprites
    for i in range(5):
        #This represents an ememy
        enemy = Enemy_common(3)

        #set a random location at the right of the screen
        #for the ememy to appear.
        enemy.rect.y = random.randrange(screen_height)
        enemy.rect.x = random.randrange(screen_width + 5, screen_width*2)

        #add the enemies to the list of sprites
        #and the list of enemies.
        enemy_list.add(enemy)
        all_spites_list.add(enemy)

    for i in range(5):
        #This represents an ememy with random height, width and speed
        rand_enemy = Rand_enemy()

        #set a random location at the right of the screen
        #for the ememy to appear.
        rand_enemy.rect.y = random.randrange(screen_height)
        rand_enemy.rect.x = random.randrange(screen_width + 5, screen_width*2)

        #add the enemies to the list of sprites
        #and the list of enemies.
        enemy_list.add(rand_enemy)
        all_spites_list.add(rand_enemy)

    for i in range(3):
        #This represents treasure
        treasure = Treasure(GREEN, 10, 10, 2)

        #set a random location at the right of the screen
        #for the ememy to appear.
        treasure.rect.y = random.randrange(screen_height)
        treasure.rect.x = random.randrange(screen_width + 5, screen_width*2)

        #add the treasure to the list of sprites
        #and the list of treasure.
        treasure_list.add(treasure)
        all_spites_list.add(treasure)

    player = Player()
    all_spites_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    #player starting speed
    y_speed = 0

    # Player starting position
    y_coord = screen_height // 2

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an up or down arrow key. If so
                # adjust speed.

                if event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3

            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        #update player y speed
        y_coord += y_speed
        #update payer y coordinate
        if (y_coord > 10) and (y_coord < screen_height):
            player.rect.y = y_coord


        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        screen.blit(background_image, [0, 0])
        #screen.blit(player_image, [player.rect.x -15, player.rect.y -25])
        #player_image.set_colorkey(BLACK)

        all_spites_list.update()

        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
        treasure_hit_list = pygame.sprite.spritecollide(player,treasure_list,True)

        if len(blocks_hit_list) > 0:
            done = True
            print("Your enemies have triumphed!")

        # Check the list of collisions.
        for block in treasure_hit_list:
            score += 1
            print(score)

        if len(treasure_list) == 0:
            print("You have collected all the treasure!")
            done = True

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT




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
