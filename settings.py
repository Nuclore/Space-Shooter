class Settings:
	'''Class containing game settings.'''

	def __init__(self):
		'''Initialze the game's static settingss.'''

		self.screen_width = 1280 # Screen width
		self.screen_height = 720 # Screen height
		self.caption = 'Space Shooter' # Game title
		self.FPS = 60 # Frames per second

		self.ship_limit = 3 # Number of ships.

		self.bullets_allowed = 3 # Bullets allowed.

		self.alien_probability = 100 # Chance of alien spawning is 1/100 per frame.

		self.speedup_scale = 1.1 # Speed up factor for each level.

		self.alien_points = 100 # How many points aliens are worth.

		self.initialize_dynamic_settings() # Initializes settings that will change during gameplay.

	def initialize_dynamic_settings(self):
		'''Initialize settings that would change throughout the game.'''
		self.ship_speed = 4.0 # Initial speed of ship.
		self.bullet_speed = 5.0 # Initital speed of bullet.
		self.alien_speed = 1.0 # Initial speed of alien.

	def speed_up(self):
		'''Increases the value of the dynamic settings after each level by the speed up factor.'''
		self.ship_speed *= self.speedup_scale # Increases the ship speed by the speed up factor.
		self.bullet_speed *= self.speedup_scale # Increases the bullet speed by the speed up factor.
		self.alien_speed *= self.speedup_scale # Increases the alien speed by the speed up factor.
