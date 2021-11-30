import pygame

class Explosion:
	'''Class to represent an explosion when a collision occurs.'''

	def __init__(self, game, center):
		'''Initialize the explosion frames and its position.'''
		self.window = game.window # Accesses the game window.
		self.settings = game.settings # Accesses the game setttings.
		self.images = [] # List to store explosion images.
		
		for number in range(1, 8): # Loops through each explosion image.
			image = pygame.image.load(f'assets/images/explosion/explosion_frame_{number}.png') # Loads the explosion image.
			self.images.append(image) # Adds the explosion image to the images list.

		self.index = 0 # Index for accessing each explosion frame, which is intially set to 0.
		self.frame_duration = self.settings.FPS # Duration of an explosion frame i.e. how many frames after will the explosion frame be displayed.

		self.center = center # Center of the explosion (x, y).
		self.image = None # Initial value of the image set to None.
 
		self.last_update = pygame.time.get_ticks() # Get the current timestamp of the game.

	def update(self):
		'''Switches to a new explosion frame.'''
		now = pygame.time.get_ticks() # Get the current timestamp of the game.
		frames_elapsed = now - self.last_update # Calculates how many frames elapsed from the current timestamp to the previous timestamp.

		if frames_elapsed > self.frame_duration: # Checks if the frames elapsed is greater than the duration of a frame.
			self.last_update = now # Updates the last timestamp to the current timestamp.

			if self.index < len(self.images): # Checks if the index is less than the length of the explosion images list.
				self.image = self.images[self.index] # # Gets the image at the specified index.
				self.rect = self.image.get_rect() # Obtains the rect for the image.
				self.rect.center = self.center # Assigns the center of the image to the center of the explosion.
				self.index += 1 # Increments the index for a new image.

	def draw(self):
		'''Displays each explosion frame on the screen at the specified position.'''
		if self.image: # Checks if the image has content.
			self.window.blit(self.image, self.rect) # Draws explosion.

