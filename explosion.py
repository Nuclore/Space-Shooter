import pygame

class Explosion:
	'''Class to represent an explosion when a collision occurs.'''

	def __init__(self, game, center):
		'''Initialize the explosion images and its position.'''
		self.window = game.window # Accesses the game window.
		self.settings = game.settings # Accesses the game setttings.
		self.explosion_images = [] # List to store explosion images.
		
		for number in range(1, 8): # Loops through each explosion image.
			explosion_image = pygame.image.load(f'assets/images/explosion/explosion_frame_{number}.png') # Loads the explosion image.
			self.explosion_images.append(explosion_image) # Adds the explosion image to the images list.

		self.index = 0 # Index for accessing each explosion image, initially set to 0.
		# Duration of an explosion frame in milliseconds i.e. how long it would take to display an explosion image.
		self.frame_duration = self.settings.frame_duration 

		self.center = center # Center of the explosion (x, y).
		self.explosion_image = None # Initial value of the explosion image set to None.
 
		self.last_update = pygame.time.get_ticks() # Returns number of milliseconds since the game was started.

	def update(self):
		'''Switches to a new explosion frame.'''
		now = pygame.time.get_ticks() # Returns the number of milliseconds since the game was started.
		time_difference = now - self.last_update # Calculates the difference in time in milliseconds.

		if time_difference > self.frame_duration: # Checks if the time diffrerence is greater than the frame duration.
			self.last_update = now # Updates the last timestamp to the current timestamp.

			if self.index < len(self.explosion_images): # Checks if the index is less than the length of the explosion images list.
				self.explosion_image = self.explosion_images[self.index] # # Gets the explosion image at the specified index.
				self.rect = self.explosion_image.get_rect() # Obtains the rect for the explosion image.
				self.rect.center = self.center # Assigns the center of the explosion image to the center of the explosion.
				self.index += 1 # Increments the index for a new image.

	def draw(self):
		'''Displays each explosion frame on the screen at the specified position.'''
		if self.explosion_image: # Checks if the image has content.
			self.window.blit(self.explosion_image, self.rect) # Draws explosion image.

