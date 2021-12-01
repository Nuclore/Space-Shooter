import pygame.font

class Scoreboard:
	'''Class to reprsent scoring information.'''

	def __init__(self, game):
		'''Initialize scorekeeping attributes.'''
		self.window = game.window # Acccesses the game window.
		self.window_rect = self.window.get_rect() # Obtains the rect for the game window.
		self.settings = game.settings # Accesses the game settings.
		self.stats = game.stats  # Access the game statistics.

		self.text_color = (255, 255, 255) # Set text color to white.
		self.font = pygame.font.SysFont(None, 62) # Creates a font with size 62.

		self.ship_image = pygame.image.load('assets/images/player/ship.png') # Loads the ship image.
		self.ship_rect = self.ship_image.get_rect() # Obtains the rect for the ship image.
		self.ship_width = self.ship_rect.width # Returns the width of the ship image.
		self.ship_height = self.ship_rect.height # Returns the height of the ship image.
		self.spacing = 10 # Spacing between each ship image.

		self.prep_score() # Prepares score.
		self.prep_high_score() # Prepares high score.
		self.prep_level() # Prepares level number.

	def prep_score(self):
		'''Convert the score into a image to be displayed.'''
		score_str = f'Score: {self.stats.score}' # String containing score.
		self.score_image = self.font.render(score_str, True, self.text_color) # Creates a score image.

		# Sets the position for the score to be displayed.
		self.score_rect = self.score_image.get_rect() # Obtains the rect for the score image.
		self.score_rect.right = self.window_rect.right -20 # x value for score image.
		self.score_rect.top = 20 # y value for score image. 

	def prep_high_score(self):
		'''Converts he high socre into an image to be displayed.'''
		high_score_str = f'High Score: {self.stats.high_score}' # String containing high score.
		self.high_score_image = self.font.render(high_score_str, True, self.text_color) # Creates a high score image.

		# Sets the position for the high score to be displayed.
		self.high_score_rect = self.high_score_image.get_rect() # Obtains the rect for the high score image.
		self.high_score_rect.centerx = self.window_rect.centerx # Centers the high score at the top of the screen.
		self.high_score_rect.top = self.score_rect.top # High score will be set at the same height as the score image.

	def prep_level(self):
		'''Converts the level into an image to be displayed.'''
		level_str = f'Level: {self.stats.level}' # String containing level number.
		self.level_image = self.font.render(level_str, True, self.text_color) # Creates a level image.

		# Sets the position of the level number to be displayed.
		self.level_rect = self.level_image.get_rect() # Obtains the rect for the level image.
		self.level_rect.right = self.score_rect.right # Level will be assigned the same x value as score.
		self.level_rect.top = self.score_rect.bottom + 10 # Level will be 10 pixels below score.

	def prep_lives(self):
		'''Converts the number of ships left, as ship images to be displayed at the top left corner of the screen.'''
		self.ship_images = [] # List to store ship images.
		self.ship_rects = [] # List to store ship rects.

		for number in range(self.stats.ships_left): # Loops through the number of lives.
			image = pygame.image.load('assets/images/player/ship.png') # Load the ship image.
			# Scales the ship image to half of its width, and half of its height.
			scaled_image = pygame.transform.scale(image, (self.ship_width / 2, self.ship_height / 2)) 
			self.ship_images.append(scaled_image) # Adds the scaled image to the list of ship images.

			rect = image.get_rect() # Obtains the rect for the image.
			rect.x = self.spacing + (number * ((rect.width / 2) + self.spacing)) # Horizontal position of the ship image.
			rect.y = 20 # Vertical position of the ship image.
			self.ship_rects.append(rect) # Add the rect to the list of ship rects.

	def show_score(self):
		'''Display the scores, level and lives on the screen.'''
		self.window.blit(self.score_image, self.score_rect) # Draws the score.
		self.window.blit(self.high_score_image, self.high_score_rect) # Draws the high score.
		self.window.blit(self.level_image, self.level_rect) # Draws the level number.

		for image, rect in zip(self.ship_images, self.ship_rects): # Loops through each ship image and ship rect simulataneously.
			self.window.blit(image, rect) # Draws the ship.

	def check_high_score(self):
		'''Sets a high score if current score is higher than previous high score.'''
		if self.stats.score > self.stats.high_score: # Checks if current score is higher than high score.
			self.stats.high_score = self.stats.score # Sets the high score to the current score.
			self.prep_high_score() # Prepares high score.
			self.stats.save_high_score() # Saves high score to a file.