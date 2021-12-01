import os

class GameStats:
	'''Class to track game statistics.'''

	def __init__(self, game):
		'''Initialize statistics.'''
		self.settings = game.settings # Accesses the game settings.
		self.reset_stats() # Reset the game statistics.

		self.game_active = False # Starts the game in an inactive state.
		self.game_over = False # Set to True when the player has no more ships left.

		self.high_score = 0 # High score of the game.
		self.load_high_score() # Loads the high score from high_score.txt, if high_score.txt exists.
		
	def reset_stats(self):
		'''Initialize statistics that can change during the game.'''
		self.ships_left = self.settings.ship_limit # Resets the number of ships.
		self.score = 0 # Sets initial score to 0.
		self.level = 1 # Sets initial level number to 1.

	def load_high_score(self):
		'''Loads the high score from a text file.'''
		if os.path.exists('high_score.txt'): # Checks if high_score.txt exist in the same directory.
			try:
				with open('high_score.txt') as f: # Opens  high_score.txt in read mode.
					high_score = f.readline().strip() # Reads the first line of the file, and strips any whitespace.
					self.high_score = int(high_score) # Converts the returned string into an integer and store it in the high_score attribute.
			except FileNotFoundError:
				# Displays an error if high_score.txt does not exist.
				print('high_score.txt does not exist.')
		else:
			print('high_score.txt does not exist.') # Displays an error if high_score.txt does not exist.

	def save_high_score(self):
		'''Save the high score to a text file.'''
		with open('high_score.txt', 'w') as f: # Creates high_score.txt in write mode.
			high_score = str(self.high_score) # Converts the high_score attribute into a string.
			f.write(high_score) # Writes the high score to the high_score.txt
	