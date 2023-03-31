#


#require for configure pygame environment
#step :  
# 1.download pygame-1.9.6-cp39-cp39-win_amd64.whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
# 2.run command : py -m pip install --user pygame-1.9.6-cp39-cp39-win_amd64.whl
# 
#note : pygram version must be correspond with python version for successful configure 
# 
#

import pygame
import sys

from settings import Settings 
from ship import Ship
from alien import Alien
import game_func as gf

from pygame.sprite import Group


def run_game() :
	
	#init
	pygame.init()	
	ai_settings = Settings()
	screen = pygame.display.set_mode((
		ai_settings.screen_width , ai_settings.screen_height))
	pygame.display.set_caption("Rocket Free")
	ship = Ship(ai_settings, screen) 		
	alien = Alien(ai_settings, screen) 
	
	bullets = Group() #null editor
	aliens = Group() 
	gf.create_fleet(ai_settings , screen , ship , aliens)
	

	#main cycle
	while True :	
		gf.check_events(ai_settings, screen , ship , bullets )
		ship.update() 
		bullets.update()
		
		gf.update_bullets(aliens, bullets,screen , ship,ai_settings)
		gf.update_screen(ai_settings , screen , ship , bullets , aliens)				
		gf.update_aliens(ai_settings,  aliens,ship)
		pygame.display.flip()  #similar to flush recent draw

	
	
	
run_game()

