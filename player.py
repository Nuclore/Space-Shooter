import pygame

class Ship:
	'''Class to manage the ship and its position.'''

	def __init__(self, game):
		'''Initialize the ship and it's starting position.'''
		self.window = game.window # Accesses the game window.
		self.window_rect = self.window.get_rect() # Obtains the rect for the game window.
		self.settings = game.settings # Accesses the game window.

		self.image = pygame.image.load('assets/images/player/ship.png') # Loads the ship image.
	
		# Gets the rectangle of the ship image, which is used for collision detection.
		# The rect object contains attributes such as: x, y, width, height, left, right, top, bottom.
		# x represents the x-coordinate of the top left corner of the image.
		# y represents the y-coordinate of the top left corner of the image.
		# By default, the returned rectangle would start start at the top left corner of the screen (0, 0).
		self.rect = self.image.get_rect() # Obtains the rect of the ship image.

		# Starts the player at the bottom of the screen.
		self.rect.x = int(self.window_rect.width / 2) - self.rect.width # Starting horizontal value of ship.
		self.rect.y = int(self.window_rect.height - 150) # Starting vertical value of ship.

		# Movement flags, each with an initial value of False.
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		'''Moves the ship based on the movement flags.'''
		# Checks if the ship is moving right,  and is not at the right edge of the screen.
		if self.moving_right and self.rect.right < self.window_rect.width:
			self.rect.x += self.settings.ship_speed # Moves the ship to the right.

		# Checks if the ship is moving left, and is not at the left edge of the screen.
		if self.moving_left and self.rect.left > 0:
			self.rect.x -= self.settings.ship_speed # Moves the ship to the left.

		# Checks if the ship is moving up, and is is not at the top edge of the screen.
		if self.moving_up and self.rect.top > 0:
			self.rect.y -= self.settings.ship_speed # Moves the ship upwards.

		# Checks if the ship is moving down, and is not at the bottom edge of the screen.
		if self.moving_down and self.rect.bottom < self.window_rect.height:
			self.rect.y += self.settings.ship_speed # Move the ship downwards.

	def center_ship(self):
		# Center the ship at the bottom of the screen.
		self.rect.x = int(self.settings.screen_width / 2) - self.rect.width # Staring horizontal position of ship.
		self.rect.y = int(self.settings.screen_height - 150) # Starting vertical position of ship.

	def draw(self):
		'''Displays the ship on the screen at th specified position.'''
		self.window.blit(self.image, self.rect)


class Bullet:
	'''Class to represent a bullet.'''

	def __init__(self, game):
		'''Create a bullet at the ship's current position.'''
		self.window = game.window # Accesses the game window.
		self.ship = game.ship # Access the ship from the game.
		self.settings = game.settings # Accesses the game settings.
 
		self.image = pygame.image.load('assets/images/player/bullet.png') # Loads the bullet image.
		self.rect = self.image.get_rect() # Obtains the rect for the bullet image.

		self.rect.x = (self.ship.rect.left + self.ship.rect.right) / 2 # Starting horizontal position of bullet (center of ship)
		self.rect.y = self.ship.rect.y # Starting vertical position of bullet (top of ship)

	def update(self):
		'''Updates the position of the bullet on the screen.'''
		# Moves the bullet up the screen by subtracting its current vertical position from its speed.
		self.rect.y -= self.settings.bullet_speed 

	def draw(self):
		'''Displays the bullet on the screen at the specified position.'''
		self.window.blit(self.image, self.rect)


