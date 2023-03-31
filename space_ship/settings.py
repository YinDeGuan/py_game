#

class Settings() : 
	""" alion settings """
	
	def __init__(self) :
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (255,255,255)

		self.ship_speed_factor = 1.5 
		
		self.bullet_speed_factor=1
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=60,60,60  #notice usage
		
		
		self.fleet_drop_speed = 10
		self.fleet_direction = 1  
		
		self.alien_speed_factor = 0.5 
		
