class GameStats:
	'''Class to track game statistics.'''

	def __init__(self, game):
		'''Initialize statistics.'''
		self.settings = game.settings # Accesses the game settings.
		self.reset_stats() # Reset the game statistics.

		self.game_active = False # Starts the game in an inactive state.

		self.high_score = 0 # High score should never be reset.
		
	def reset_stats(self):
		'''Initialize statistics that can change during the game.'''
		self.ships_left = self.settings.ship_limit # Resets the number of ships.
		self.score = 0 # Sets initial score to 0.
		self.level = 1 # Sets initial level number to 1.
		