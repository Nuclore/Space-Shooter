import random 

import pygame

class Alien:
	'''Class to represent an alien and its movement.'''

	def __init__(self, game):
		'''Initialize the alien and set its starting position.'''
		self.window = game.window # Accesses the game window.
		self.window_rect = self.window.get_rect() # Obtains the rect for the game window.
		self.settings = game.settings # Accesses the game settings.

		self.image = pygame.image.load('assets/images/alien.png') # Load the alien image.
		self.rect = self.image.get_rect() # Obtains the rect for the alien image.

		self.rect.x = random.randint(0, (self.window_rect.width - self.rect.width)) # Starting horizontal position for the alien.
		self.rect.y = -100 # Starting vertical position for the alien.

		# Random direction for alien (i.e. -1, 0 and 1)
		# -1 represents left, 0 represents straight, 1 represents right.
		self.direction = random.randint(-1, 1) 

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


