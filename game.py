import random
import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from screens import Screens
from ship import Ship
from bullet import Bullet
from alien import Alien

class SpaceShooter:
    '''Overall class to manage the game.'''

    def __init__(self):
        '''Initialize the game and the required resourses.'''
        pygame.init() # Initializes the background settings required for pygame.
        self.clock = pygame.time.Clock() # Creates a clock object for limiting frames per second.
        self.settings = Settings() # Creates an instance to access game settings.

        # Creates a window with the specified width and height.
        self.window = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        self.window_rect = self.window.get_rect() # Obtains the rectangle for the window.
        pygame.display.set_caption(self.settings.caption) # Sets game title on the window.
    
        self.stats = GameStats(self) # Create an instance to store game statistics.
        self.scoreboard = Scoreboard(self) # Creates an instance for preparing and displaying the scoreboard.

        # Game Elements
        self.ship = Ship(self) # Creates a ship.
        self.bullets = [] # List to store bullets fired by the ship.
        self.aliens = [] # List to store aliens on screen.

        self._create_alien() # Create aliens.

        self.screens = Screens(self) # Creates an instance to display the start screen and background.

    def run_game(self):
        '''Starts game loop.'''
        while True:
            self._check_events() # Check for any keyboard or mouse interactions.

            if self.stats.game_active: # Checks if the game is an active state.
                self.ship.update() # Updates the position of the ship.
                self._update_bullets() # Updates the position of the bullets on the screen.
                self._update_aliens() # Updates the position of the aliens on the screen.

            self._update_screen() # Redraw each frame on the screen.

    def _start_game(self):
        '''Starts a new game when the game is launched, or if the player has no more ships.'''
        # Reset the game settings.
        self.settings.initialize_dynamic_settings() # Sets dynamic settings for game.
        self.stats.reset_stats() # Reset game statistics.
        self.stats.game_active = True # Starts the game in an active state.
        self.scoreboard.prep_score() # Prepares score to be displayed.
        self.scoreboard.prep_level() # Prepares level number to be displayed.
        self.scoreboard.prep_lives() # Prepapre number of lives to be displayed.
        self.aliens.clear() # Empties the aliens list.
        self.bullets.clear() # Empties the bullets list.

        self._create_alien() # Creates alien.
        self.ship.center_ship() # Centers the ship.

        pygame.mouse.set_visible(False) # Hides the mouse cursor in the window.

    def _check_events(self):
        '''Check for keyboard and mouse events, and responds to them.'''
        for event in pygame.event.get(): # Loops through each event.
                if event.type == pygame.QUIT: # Checks if the player clicks on the close button on the window.
                    pygame.quit() # Uninitializes pygame.
                    sys.exit() # Exits the game.
                elif event.type == pygame.KEYDOWN: # Checks if a key was pressed.
                    self._check_keydown_events(event) 
                elif event.type == pygame.KEYUP: # Checks if a key was released.
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN: # Checks if the mouse button was clicked.
                    mouse_pos = pygame.mouse.get_pos() # Gets the position of the mouse cursor as a tuple.
                    self._check_play_button(mouse_pos) # Checks if the play button was clicked.

    def _check_play_button(self, mouse_pos):
        '''Starts the a new game when the player clicks the Play button.'''
        button_clicked = self.screens.play_button_rect.collidepoint(mouse_pos) # Returns True if the play button was clicked.
        if button_clicked and not self.stats.game_active: # Checks if the play button was clicked and the game is active.
            self._start_game() # Reset the game settings for a new game.
           
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT: # Checks if the right arrow key was pressed.
            self.ship.moving_right = True # Sets the right movement flag to True.
        elif event.key == pygame.K_LEFT: # Checks if the left arrow key was pressed.
            self.ship.moving_left = True # Sets the left movement flag to True.
        elif event.key == pygame.K_UP: # Checks if the up arrow key was pressed.
            self.ship.moving_up = True # Sets the up movement flag to True.
        elif event.key == pygame.K_DOWN:# Checks if the down arrow key was pressed.
            self.ship.moving_down =  True # Sets the down movement flag to True.
        elif event.key == pygame.K_q: # Checks if the 'q' key was pressed.
            pygame.quit() # Uninitialize pygame.
            sys.exit() # Exits the game.
        elif event.key == pygame.K_SPACE: # Checks if the space key was pressed.
            self._fire_bullet() # Fire a bullet from the ship

    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT: # Checks if the right arrow key was released.
            self.ship.moving_right = False # Set the right movement flag to False.
        elif event.key == pygame.K_LEFT: # Checks if the left arrow key was released.
            self.ship.moving_left = False # Set the left movement flag to False.
        elif event.key == pygame.K_UP: # Checks if the up arrow key was released.
            self.ship.moving_up = False # Set the up movement flag to False.
        elif event.key == pygame.K_DOWN: # Checks if the down arrow key was released.
            self.ship.moving_down =  False # Set the down movement flag to False.

    def _check_bullet_alien_collision(self, bullet):
        '''Respond to bullet-alien collisions.'''
        for alien in self.aliens: # Loops through each alien in the list.
            if pygame.Rect.colliderect(bullet.rect, alien.rect): # Checks if an alien is hit by a bullet.
                try:
                    self.aliens.remove(alien) # Remove any alien that have collided with the bullet.
                    self.bullets.remove(bullet) # Remove any bullet that have collided with the alien.
                    self.stats.score += self.settings.alien_points # Increments the score when an alien is shot.
                    self.scoreboard.prep_score() # Prepares the score with the new value.
                    self.scoreboard.check_high_score() # Checks if the score is a new high score.
                    self._speed_up() # Speeds up the game if the a new level is reached.
                except ValueError:
                    #Displays an error if bullets list does not contain the bullet.
                    print('Bullets list does not contain bullet.')

    def _speed_up(self):
        '''Speeds up the game if a new level is reached.'''

        # Checks if the remainder is 0 when the score is divided by 1000.
        # A new level is reached after every 1000 points.
        if self.stats.score % 1000 == 0: 
            self.stats.level += 1 # Increments level number.
            self.settings.speed_up() # Speeds up the game by the speed factor.
            self.scoreboard.prep_level() # Prepares the new level number.

    def _ship_hit(self):
        '''Responds to the ship being hit by an alien, or if an alien reaches the bottom of the screen.'''
        if self.stats.ships_left > 1: # Checks if there are any ships left.

            self.stats.ships_left -= 1 # Decrements number of ships.
            self.scoreboard.prep_lives() # Prepares the new number of lives left.

            self.aliens.clear() # Empties the aliens list.
            self.bullets.clear() # Empties the bullets list.

            self._create_alien() # Creates new aliens.
            self.ship.center_ship() # Recenter the ship.

            sleep(0.5) # Pause the game for 0.5 seconds.
        else:
            self.stats.game_active = False # Sets the game to an inactive state.
            pygame.mouse.set_visible(True) # Make the mouse cursor visble when the game is not active.

    def _check_ship_alien_collision(self):
        '''Responds to an alien and the ship colliding.'''
        for alien in self.aliens: # Loops through each alien.
            if pygame.Rect.colliderect(alien.rect, self.ship.rect): # Checks if the alien collides with the ship.
                self._ship_hit() # Resets the game for a new round.
                break 

    def _check_aliens_bottom(self):
        '''Checks if an alien reaches the bottom of the screen.'''
        for alien in self.aliens: # Loops through each alien.
            if alien.rect.bottom >= self.window_rect.bottom: # Checks if the alien reaches the bottom of the screen.
                self._ship_hit() # Resets the game for a new round.
                break 

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets list.'''
        # Checks if the number of bullets fired is less than that allowed.
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self) # Creates a new bullet.
            self.bullets.append(new_bullet) # Adds it to the bullets list.

    def _update_bullets(self):
        '''Update the position of bullets and remove old bullets.'''
        for bullet in  self.bullets: # Loop through each bullet.
            bullet.update() # Updates the position of the bullet.
            if bullet.rect.bottom <= 0: # Checks if the bottom of the bullet reaches the top of the screen.
                self.bullets.remove(bullet) # Removes the bullet from the list.
            self._check_bullet_alien_collision(bullet) # Checks if the bullet hits the alien.

    def _update_aliens(self):
        '''Updates the position of the aliens.'''
        if random.randint(1, self.settings.alien_probability) == 1: # Checks if the random number is 1.
            self._create_alien() # Randomly creates an alien.

        for alien in self.aliens: # Loop through each alien.
            alien.update() # Updates the position of the alien.
        
        self._check_ship_alien_collision() # Check if an alien collides with the ship.
        self._check_aliens_bottom() # Checks if an alien reaches the bottom of the screen.

    def _create_alien(self):
        '''Create a new alien and adds it to the alien list.'''
        alien = Alien(self) # Creates alien.
        self.aliens.append(alien) # Adds alien to the aliens list.

    def _update_screen(self):
        '''Redraws each frame of the screen.''' 
        if self.stats.game_active: # Checks if the game is active.
            self.screens.draw_background() # Draws the game background.

            for bullet in self.bullets: # Loops through each bullet.
                bullet.draw() # Draw bullet.

            for alien in self.aliens: # Loops through each alien.
                alien.draw() # Draw alien

            self.ship.draw() # Draw ship.
            self.scoreboard.show_score() # Draw score, high score, level and lives.
        else:
            self.screens.draw_start_screen() # Draw start screen of game.

        pygame.display.flip() # Display the current frame on the screen.
        self.clock.tick(self.settings.FPS) # Limits the screen to 60 frames per second.


if __name__ == '__main__':
    space_shooter = SpaceShooter() # Creates an instance of the game.
    space_shooter.run_game() # Starts the game.