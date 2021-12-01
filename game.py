import random
import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from screens import Screens
from player import Ship, Bullet
from enemy import Alien, AlienBullet, Asteroid
from explosion import Explosion

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
        self.aliens = [] # List to store aliens.
        self.alien_bullets = [] # List to store bullets shot by aliens.
        self.asteroids = [] # List to store asteroids.
        self.explosions = [] # List to store explosions.

        self.screens = Screens(self) # Creates an instance to display the start screen, game over screen and background.

    def run_game(self):
        '''Starts game loop.'''
        while True:
            self._check_events() # Check for any keyboard or mouse interactions.

             # Checks if the game is active and the game_over flag is set to False.
            if self.stats.game_active and not self.stats.game_over:
                self.ship.update() # Updates the position of the ship.
                self._update_bullets() # Updates the position of the bullets on the screen.
                self._update_aliens() # Updates the position of the aliens on the screen.
                self._update_alien_bullets() # Updates the position of the alien bullets on the screen.
                self._update_asteroids() # Update the position of the asteroids on the screen.

            self._update_screen() # Redraw each frame on the screen.

    def _start_game(self):
        '''Starts a new game when the game is launched, or if the player has no more ships.'''
        # Reset the game settings.
        self.settings.initialize_dynamic_settings() # Sets dynamic settings for game.
        self.stats.reset_stats() # Reset game statistics.
        self.stats.game_active = True # Starts the game in an active state.
        self.stats.game_over = False # Sets the game_over flag to False.
        self.scoreboard.prep_score() # Prepares score to be displayed.
        self.scoreboard.prep_level() # Prepares level number to be displayed.
        self.scoreboard.prep_lives() # Prepapre number of lives to be displayed.
        self.aliens.clear() # Empties the aliens list.
        self.bullets.clear() # Empties the bullets list.
        self.asteroids.clear() # Empties the asteroids list.
        self.explosions.clear() # Empties the list explosions list.
        self.alien_bullets.clear() # Empties the alien bullets list.
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
                    self._check_play_button(mouse_pos) # Checks if the Play button or Play Again button was clicked.

    def _check_play_button(self, mouse_pos):
        '''Starts the a new game when the player clicks the Play button or Play Again Button.'''
        if self.stats.game_over: # Checks if the game is over.
            button_clicked = self.screens.play_again_button_rect.collidepoint(mouse_pos) # Returns True if the Play Again button was clicked.
        else: # If the game is not over.
            button_clicked = self.screens.play_button_rect.collidepoint(mouse_pos) # Returns True if the Play button was clicked.

        # Checks if the Play button or Play Again button was clicked and the game is not active.
        if button_clicked and not self.stats.game_active: 
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
                    # Creates an explosion instance, with the current instance and the center of the alien.
                    explosion = Explosion(self, alien.rect.center) 
                    self.explosions.append(explosion) # Adds the explosion to the explosions list.

                    self.aliens.remove(alien) # Remove any alien that have collided with the bullet.
                    self.bullets.remove(bullet) # Remove any bullet that have collided with the alien.
                    self.stats.score += self.settings.alien_points # Increments the score when an alien is shot.
                    self.scoreboard.prep_score() # Prepares the score with the new value.
                    self.scoreboard.check_high_score() # Checks if the score is a new high score.
                    self._speed_up() # Speeds up the game if the a new level is reached.
                except ValueError:
                    # Displays an error if bullets list does not contain the bullet.
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
            self.alien_bullets.clear() # Empties the alien bullets list.
            self.asteroids.clear() # Empties the asteroids list.
            self.explosions.clear() # Empties the list containing the explosions.

            self.ship.center_ship() # Recenter the ship.

            sleep(0.5) # Pause the game for 0.5 seconds.
        else:
            self.stats.game_active = False # Sets the game to an inactive state.
            self.stats.game_over = True # Sets the game over flag to True.
            pygame.mouse.set_visible(True) # Make the mouse cursor visble when the game is not active.

    def _check_ship_alien_collision(self):
        '''Responds to an alien and the ship colliding.'''
        for alien in self.aliens: # Loops through each alien.
            if pygame.Rect.colliderect(alien.rect, self.ship.rect): # Checks if the alien collides with the ship.
                self._ship_hit() # Resets the game for a new round.
                break 

    def _check_ship_alien_bullets_collision(self):
        '''Responds to an alien bullet and the ship colliding'''
        for alien_bullet in self.alien_bullets: # Loops through each bullet shot by the alien.
            if pygame.Rect.colliderect(alien_bullet.rect, self.ship.rect): # Checks if the alien bullet collides with the ship.
                self._ship_hit() # Resets the game for a new round.
                break

    def _check_asteroid_ship_collision(self):
        '''Responds to an asteroid and the ship colliding.'''
        for asteroid in self.asteroids: # Loops through each asteroid.
            if pygame.Rect.colliderect(asteroid.rect, self.ship.rect): # Checks if the asteroid collides with the ship.
                self._ship_hit() # Resets the game for a new round.
                break

    def _check_bullet_asteroid_collision(self):
        '''Responds to a bullet-asteroid collision.'''
        for asteroid in self.asteroids: # Loops through each asteroid.
            for bullet in self.bullets: # Loops through each bullet.
                if pygame.Rect.colliderect(bullet.rect, asteroid.rect): # Checks if a bullet collides with the asteroid.

                    # Creates an explosion instance, with the current instance and the center of the asteroid.
                    explosion = Explosion(self, asteroid.rect.center)
                    self.explosions.append(explosion) # Adds the explosion to the explosions list.

                    self.bullets.remove(bullet) # Removes the bullet.
                    self.asteroids.remove(asteroid) # Removes the asteroid.
                    self.stats.score += self.settings.asteroid_points # Increments the score when an asteroid is shot.
                    self.scoreboard.prep_score() # Prepares the score with the new value.
                    self.scoreboard.check_high_score() # Checks if the score is a new high score.
                    self._speed_up() # Speeds up the game if the a new level is reached.
                    break 

    def _check_asteroid_bottom(self):
        '''Checks is an alien reaches the bottom of the screen.'''
        for asteroid in self.asteroids: # Loop through each asteroid.
            if asteroid.rect.bottom >= self.window_rect.bottom: # Checks if an alien reaches the bottom of the screen.
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
        '''Updates the position of the aliens and create new ones.'''
        if random.randint(1, self.settings.alien_probability) == 1: # Randomly create an alien.
            alien = Alien(self) # Create an alien.
            self.aliens.append(alien) # Adds alien to the aliens list.

        for alien in self.aliens: # Loop through each alien.
            alien.update() # Updates the position of the alien.
            if alien.shoot(): # If the alien shoot a bullet.
                x, y = alien.get_alien_bullet_coordinates() # Obtain the starting position of the bullet.
                alien_bullet = AlienBullet(self, x, y) # Creates an instance of the bullet.
                self.alien_bullets.append(alien_bullet) # Adds the bullet to the alien bullets list.

        self._check_ship_alien_collision() # Check if an alien collides with the ship.
        self._check_aliens_bottom() # Checks if an alien reaches the bottom of the screen.

    def _update_alien_bullets(self):
        '''Updates the position of the alien bullets.'''
        for alien_bullet in self.alien_bullets: # Loops through each bullet shot by the alien.
            alien_bullet.update() # Updates the position of the bullet.
            
            if alien_bullet.rect.top >= self.window_rect.height: # Checks if the bullet reaches the bottom of the screen.
                self.alien_bullets.remove(alien_bullet) # Removes the bullet from the alien bullet list.

        self._check_ship_alien_bullets_collision() # Checks if a bullet shot by the alien collides with the ship.

    def _update_asteroids(self):
        '''Updates the position of the asteroids and create new ones.'''
        if random.randint(1, self.settings.asteroid_probability) == 1: # Randomly creates an asteroid.
            asteroid = Asteroid(self) # Create an asteroid
            self.asteroids.append(asteroid) # Adds asteroid to the asteroid list.

        for asteroid in self.asteroids: # Loop through each asteroid.
            asteroid.update() # Updates the position of the asteroid.

        self._check_asteroid_ship_collision() # Checks if an asteroid collides with the ship.
        self._check_bullet_asteroid_collision() # Checks if an asteroid is shot.
        self._check_asteroid_bottom() # Checks if an asteroid reaches the bottom of the screen.

    def _draw_explosions(self):
        '''Display each explosion on the screen.'''
        for explosion in self.explosions: # Loops through each explosion.
            # Checks if the explosion index does not equal to the length of the explosion images list.
            if explosion.index != len(explosion.explosion_images):
                explosion.update() # Switches to a new explosion image.
                explosion.draw() # Draw the explosion image.
            else:
                # Removes the explosion if the index is equal to the length of the explosion images list.
                self.explosions.remove(explosion) 

    def _update_screen(self):
        '''Redraws each frame of the screen.''' 
        if self.stats.game_active and not self.stats.game_over: # Checks if the game is active and the game is not over.
            self.screens.draw_background() # Draws the game background.

            for bullet in self.bullets: # Loops through each bullet.
                bullet.draw() # Draw bullet.

            for asteroid in self.asteroids: # Loops through each asteroid.
                asteroid.draw() # Draws asteroid.

            for alien in self.aliens: # Loops through each alien.
                alien.draw() # Draw alien.

            for alien_bullet in self.alien_bullets: # Loops through each bullet shot by the alien.
                alien_bullet.draw() # Draws alien bullet.

            self._draw_explosions() # Draws explosions.

            self.ship.draw() # Draw ship.
            self.scoreboard.show_score() # Draw score, high score, level and lives.
        elif not self.stats.game_active and self.stats.game_over: # Checks if the game is inactive and the game is over.
            self.screens.draw_game_over_screen() # Draws the game over screen when there are no more ships left.
        else:
            self.screens.draw_start_screen() # Draw the start screen of the game when the game is first launched.

        pygame.display.flip() # Display the current frame on the screen.
        self.clock.tick(self.settings.FPS) # Limits the screen to 60 frames per second.


if __name__ == '__main__':
    space_shooter = SpaceShooter() # Creates an instance of the game.
    space_shooter.run_game() # Starts the game.