import pygame

class Screens:
	'''Class for creating the screens for the game.'''
	def __init__(self, game):
		'''Loads the images and get their rects.'''
		self.window = game.window # Accesses the game window.
		self.window_rect = self.window.get_rect()
		self.settings = game.settings # Accesses game settings.

		self.bg_image = pygame.image.load('assets/images/screens/background.png') # Loads the background image.
		self.bg_image_rect = self.bg_image.get_rect() # Obtains the rect for the background image.

		self.title = pygame.image.load('assets/images/screens/title.png') # Loads the title image.
		self.title_rect = self.title.get_rect() # Obtains the rect for the title image.
		self.title_rect.x = (self.window_rect.width / 2) - (self.title_rect.width / 2) # x value for the title image.
		self.title_rect.y = 100 # y value for the title.

		self.alien = pygame.image.load('assets/images/enemy/alien.png') # Loads the alien image.
		self.alien_rect = self.alien.get_rect() # Obtains the rect for the alien image.
		self.alien_rect.x = (self.window_rect.width / 2) - (self.alien_rect.width / 2) # x value for the alien image.
		self.alien_rect.y = 300 # y value for the alien image.

		self.ship = pygame.image.load('assets/images/player/ship.png') # Loads the ship image.
		self.ship_rect = self.ship.get_rect() # Obtains the rect for the ship image.
		self.ship_rect.right = self.alien_rect.left - 20 # Right side of the ship will be 20 pixels less than the left side of the alien.
		self.ship_rect.y = 280 # y value for ship image.

		self.asteroid = pygame.image.load('assets/images/enemy/asteroid.png') # Loads the asteroid image.
		self.asteroid_rect = self.asteroid.get_rect() # Obtains the rect for the ship image.
		self.asteroid_rect.left = self.alien_rect.right + 20 # Left side of the asteroid will be 20 pixels more than the right side of the alien.
		self.asteroid_rect.y = 280 # y value for asteroid image.

		self.controls = pygame.image.load('assets/images/screens/controls.png') # Loads the control image.
		self.controls_rect = self.controls.get_rect() # Obtains the rect for the controls image.
		self.controls_rect.right = self.window_rect.width - 20  # Right side of rect will be 20 pixels less than the width of the screen.
		self.controls_rect.bottom = self.window_rect.height - 20 # Bottom side of rect will be 20 pixels less than the height of the screen.
		
		self.instructions = pygame.image.load('assets/images/screens/instructions.png') # Loads the instructions image.
		self.instructions_rect = self.instructions.get_rect() # Obtains the rect for the instructions image.
		self.instructions_rect.x = 20 # x value for instructions image.
		self.instructions_rect.bottom = self.window_rect.height - 20 # Bottom side of rect will be 20 pixels less than the height of the screen.

		self.play_button = pygame.image.load('assets/images/screens/play_button.png') # Loads the play button image.
		self.play_button_rect = self.play_button.get_rect() # Obtains the rect for the play button image.
		self.play_button_rect.x = (self.settings.screen_width / 2) - (self.play_button_rect.width / 2) # x value for the play button image.
		self.play_button_rect.y = 500 # y value for the play button image.

		self.game_over = pygame.image.load('assets/images/screens/game_over.png') # Loads the game over image.
		self.game_over_rect = self.game_over.get_rect() # Obtains the rect for the game over image.
		self.game_over_rect.x = (self.window_rect.width / 2) - (self.game_over_rect.width / 2) # x value for the game over image.
		self.game_over_rect.y = (self.window_rect.height / 2) - self.game_over_rect.height # y value for the game over image.

		self.play_again_button = pygame.image.load('assets/images/screens/play_again_button.png') # Loads the play again button image.
		self.play_again_button_rect = self.play_again_button.get_rect() # Obtains the rect for the play again image.
		self.play_again_button_rect.x = (self.window_rect.width / 2) - (self.play_again_button_rect.width / 2) # x value for the play again button image.
		self.play_again_button_rect.top = self.game_over_rect.bottom + 200 # y value for the play again button image.
 
	def draw_start_screen(self):
		'''Displays the start screen for the game.'''
		self.window.blit(self.bg_image, self.bg_image_rect) # Draws the background image.
		self.window.blit(self.title, self.title_rect) # Draws the title.
		self.window.blit(self.alien, self.alien_rect) # Draws the alien.
		self.window.blit(self.ship, self.ship_rect) # Draws the ship.
		self.window.blit(self.asteroid, self.asteroid_rect) # Draws the asteroid.
		self.window.blit(self.controls, self.controls_rect) # Draw the controls.
		self.window.blit(self.instructions, self.instructions_rect) # Draw the instructions.
		self.window.blit(self.play_button, self.play_button_rect) # Draws the play button.

	def draw_game_over_screen(self):
		'''Display the game over screen when the player has no more ships left.'''
		self.window.blit(self.bg_image, self.bg_image_rect) # Draws the background image.
		self.window.blit(self.game_over, self.game_over_rect) # Draws the Game Over text.
		self.window.blit(self.play_again_button, self.play_again_button_rect) # Draws the Play Again button.

	def draw_background(self):
		'''Displays the background during gameplay.'''
		self.window.blit(self.bg_image, self.bg_image_rect)
