import pygame

class Bullet:
	'''Class to represent a bullet.'''

	def __init__(self, game):
		'''Create a bullet at the ship's current position.'''
		self.window = game.window # Accesses the game window.
		self.ship = game.ship # Access the ship from the game.
		self.settings = game.settings # Accesses the game settings.
 
		self.image = pygame.image.load('assets/images/bullet.png') # Loads the bullet image.
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



