"""
Basic construction of a game that is a horizontal
shooting game.
A fish eventually will shoot bubbles at enemies
To kill them.
This is just the frame work without graphics etc.
"""
import pygame
import random
import time

# Define colours
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


class EnemyCommon(Enemy):
    """This class represents the enemies"""
    def __init__(self, speed):
        super().__init__()
        self.speed = speed


class RandEnemy(Enemy):
    """This is an enemy with random speed"""
    def __init__(self):
        super().__init__()
        self.speed = random.randrange(2,10)


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
        self.image = pygame.transform.flip(pygame.image.load("fishTile_080.png").convert(),False,True)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        # Initial player position
        self.rect.x = 20
        self.rect.y = screen_height // 2


class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    def __init__(self):
        self.score = 0
        self.game_over = False
        #player starting speed
        self.y_speed = 0
        # Player starting position
        self.y_coord = screen_height // 2

        #Create sprite lists
        #All the sprites in the game
        self.all_sprites_list = pygame.sprite.Group()
        #All the enemies
        self.enemy_list = pygame.sprite.Group()
        #All the treasure
        self.treasure_list = pygame.sprite.Group()

        # player sprite
        self.player = Player()
        self.all_sprites_list.add(self.player)

        # ----- Create the sprites
        for i in range(5):
            enemy = EnemyCommon(4)
            #set a random location at the right of the screen
            # #for the ememy to appear.
            enemy.rect.y = random.randrange(screen_height)
            enemy.rect.x = random.randrange(screen_width + 5, screen_width*2)
            self.enemy_list.add(enemy)
            self.all_sprites_list.add(enemy)

        for i in range(5):
            rand_enemy = RandEnemy()
            rand_enemy.rect.y = random.randrange(screen_height)
            rand_enemy.rect.x = random.randrange(screen_width + 5, screen_width*2)
            self.enemy_list.add(rand_enemy)
            self.all_sprites_list.add(rand_enemy)

        for i in range(3):
            treasure = Treasure(GREEN, 10, 10, 2)
            treasure.rect.y = random.randrange(screen_height)
            treasure.rect.x = random.randrange(screen_width + 5, screen_width*2)
            self.treasure_list.add(treasure)
            self.all_sprites_list.add(treasure)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an up or down arrow key. If so
                # adjust speed.

                if event.key == pygame.K_UP:
                    self.y_speed = -3
                elif event.key == pygame.K_DOWN:
                    self.y_speed = 3

            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.y_speed = 0

        self.y_coord += self.y_speed
        # update payer y coordinate
        if (self.y_coord > 10) and (self.y_coord < screen_height):
            self.player.rect.y = self.y_coord

        return False

    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            self.all_sprites_list.update()

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, False)
            treasure_hit_list = pygame.sprite.spritecollide(self.player,self.treasure_list,True)

            if len(blocks_hit_list) > 0:

                print("Your enemies have triumphed!")
                self.game_over = True

            # Check the list of collisions.
            for block in treasure_hit_list:
                self.score += 1
                print(self.score)

            if len(self.treasure_list) == 0:
                print("You have collected all the treasure!")
                self.game_over = True

    def display_frame(self, screen):
        screen.fill(WHITE)
        background_image = pygame.image.load("Underwater_bubbles.jpg").convert()
        screen.blit(background_image, [0, 0])

        if self.game_over:
            font = pygame.font.SysFont("serif", 35)
            text = font.render("Game Over", True, BLACK)
            center_x = (screen_width // 2) - (text.get_width() // 2)
            center_y = (screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
            done = True

        if not self.game_over:
            self.all_sprites_list.draw(screen)
            done = False

        pygame.display.flip()
        if done:
            time.sleep(6)
        return done


def main():
    """ Main function for the game. """
    # Initialize pygame
    pygame.init()

    # Set the width and height of the screen [width,height]
    screen = pygame.display.set_mode([screen_width, screen_height])

    # click_sound = pygame.mixer.Sound("pop.ogg")

    # Set widow name
    pygame.display.set_caption("My Game")

    # Create objects and set the data
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # create an instance of the Game class
    game = Game()

    # Main game loop
    while not done:
        # process events
        done = game.process_events()

        # update object positions and check for collisions
        game.run_logic()

        # draw the current frame
        done = game.display_frame(screen)

        # pause for next frame
        clock.tick(60)
    # close window and exit
    pygame.quit()


# Call the main function start up the game
if __name__ == "__main__":
    main()
