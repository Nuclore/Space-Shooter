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
		self.alien_bullet_probability = 400 # Chance of an alien shooting a bullet is 1/500 per frame.
		self.asteroid_probability = 500 # Chance of an asteroid spawning is 1/400 per frame.

		self.speedup_scale = 1.1 # Speed up factor for each level.

		self.alien_points = 100 # How many points aliens are worth.
		self.asteroid_points = 100 # How many points asteroids are worth. 

		self.frame_duration = 60 # Duration of explosion frame in milliseconds.

		self.initialize_dynamic_settings() # Initializes settings that will change during gameplay.

	def initialize_dynamic_settings(self):
		'''Initialize settings that would change throughout the game.'''
		self.ship_speed = 4.0 # Initial speed of ship.
		self.bullet_speed = 5.0 # Initital speed of bullet.
		self.alien_speed = 1.0 # Initial speed of alien.
		self.alien_bullet_speed = 2.0 # Initial speed of alien bullet.
		self.asteroid_speed = 1.0 # Initial speed of asteroid.

	def speed_up(self):
		'''Increases the value of the dynamic settings after each level by the speed up factor.'''
		self.ship_speed *= self.speedup_scale # Increases the ship speed by the speed up factor.
		self.bullet_speed *= self.speedup_scale # Increases the bullet speed by the speed up factor.
		self.alien_speed *= self.speedup_scale # Increases the alien speed by the speed up factor.
		self.alien_bullet_speed *= self.speedup_scale # Increases the speed of the alien bullet by the speedup factor.
		self.asteroid_speed *= self.speedup_scale # Increases the speed of the asteroid by the speedup factor.
