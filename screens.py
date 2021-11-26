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

		self.title = pygame.image.load('assets/images/screens/title.png') # Loads the title.
		self.title_rect = self.title.get_rect() # Obtains the rect for the title.
		self.title_rect.x = (self.window_rect.width / 2) - (self.title_rect.width / 2) # x value for the title image.
		self.title_rect.y = 100 # y value for the title.

		self.ship = pygame.image.load('assets/images/ship.png') # Loads the ship image.
		self.ship_rect = self.ship.get_rect() # Obtains the rect for the ship image.
		self.ship_rect.x = (self.window_rect.width / 2) - (self.ship_rect.width / 2) # x value for the ship image.
		self.ship_rect.y = 300 # y value for ship image.
		
		self.play_button = pygame.image.load('assets/images/screens/play_button.png') # Loads the play button image.
		self.play_button_rect = self.play_button.get_rect() # Obtains the rect for the play button.
		self.play_button_rect.x = (self.settings.screen_width / 2) - (self.play_button_rect.width / 2) # x value for the play button.
		self.play_button_rect.y = 500 # y value for the play button.

	def draw_start_screen(self):
		'''Displays the start screen for the game.'''
		self.window.blit(self.bg_image, self.bg_image_rect) # Draws the background image.
		self.window.blit(self.title, self.title_rect) # Draws the title.
		self.window.blit(self.ship, self.ship_rect) # Draws the ship.
		self.window.blit(self.play_button, self.play_button_rect) # Draws the play button.

	def draw_background(self):
		'''Displays the background during gameplay.'''
		self.window.blit(self.bg_image, self.bg_image_rect)
