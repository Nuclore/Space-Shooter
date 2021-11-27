import random 

import pygame

class Alien:
	'''Class to represent an alien and its movement.'''

	def __init__(self, game):
		'''Initialize the alien and set its starting position.'''
		self.window = game.window # Accesses the game window.
		self.window_rect = self.window.get_rect() # Obtains the rect for the game window.
		self.settings = game.settings # Accesses the game settings.

		self.image = pygame.image.load('assets/images/enemy/alien.png') # Load the alien image.
		self.rect = self.image.get_rect() # Obtains the rect for the alien image.

		self.rect.x = random.randint(0, (self.window_rect.width - self.rect.width)) # Starting horizontal position for the alien.
		self.rect.y = -100 # Starting vertical position for the alien.

		# Random direction for alien (i.e. -1, 0 and 1)
		# -1 represents left, 0 represents straight, 1 represents right.
		self.direction = random.randint(-1, 1)

	def shoot(self):
		'''Checks if the alien should shoot a bullet.'''
		if random.randint(1, self.settings.alien_bullet_probability) == 1: # If the value is 1, return True.
			return True

	def get_alien_bullet_coordinates(self):
		'''Returns the starting horizontal and vertical position of the bullet.'''
		x = (self.rect.left + self.rect.right) / 2 # Obtains the starting horizontal position of the bullet (center of alien).
		y = self.rect.bottom # Obtains the starting vertical position of the bullet (bottom of alien).
		return x, y 

	def update(self):
		'''Updates the position of the alien.'''
		self.rect.y += self.settings.alien_speed # Move the alien down the screen by the speed of the alien.
		self.rect.x += self.direction  # Move the alien left, straight or right.

		# Checks if the alien reaches either edge of the screen.
		if self.rect.left <= 0 or self.rect.right >= self.window_rect.right:
			self.direction *= -1 # Reverses the direction of the alien.

	def draw(self):
		'''Display the alien on the screen at the specified position.'''
		self.window.blit(self.image, self.rect)


class AlienBullet:
	'''Class to represent a bullet shot by an alien, and its movement.'''

	def __init__(self, game, x, y):
		'''Initializes the bullet shot from the alien and  set its starting position.'''
		self.window = game.window # Accesses the game window.
		self.settings = game.settings # Accesses the game settings.

		self.image = pygame.image.load('assets/images/enemy/alien_bullet.png') # Loads the alien bullet image.
		self.rect = self.image.get_rect() # Obtains the rect for the alien bullet image.

		self.rect.x = x # Starting horizontal position of bullet.
		self.rect.y = y # Starting vertical position of bullet.

	def update(self):
		'''Updates the position of the bullet shot by the alien.'''
		self.rect.y += self.settings.alien_bullet_speed # Move the bullet downwards by the speed of the bullet.

	def draw(self):
		'''Display the bullet on the screen at the specified position.'''
		self.window.blit(self.image, self.rect) # Draws the bullet.


class Asteroid:
	'''Class to represent an asteroid an its movement.'''

	def __init__(self, game):
		'''Initializes the asteroid and set its starting position.'''
		self.window = game.window # Accesses the game window.
		self.window_rect = self.window.get_rect() # Obtains the rect for the game window.
		self.settings = game.settings # Accesses the game settings.

		self.image = pygame.image.load('assets/images/enemy/asteroid.png') # Loads the asteroid image.
		self.rect = self.image.get_rect() # Obtains the rect for the asteroid image.

		self.rect.x = random.randint(0, (self.window_rect.width - self.rect.width)) # Starting horizontal position for the asteroid.
		self.rect.y = -100 # Starting vertical position for the asteroid.

	def update(self):
		'''Updates the position for the asteroid.'''
		self.rect.y += self.settings.asteroid_speed # Moves the asteroid downwards by the by the speed of the asteroid.

	def draw(self):
		'''Display the asteroid on the screen at the specified position.'''
		self.window.blit(self.image, self.rect) # Draws the asteroid.



