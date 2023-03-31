# coding=gbk
import sys
import pygame
from bullet import Bullet
from alien import Alien 
from time import sleep 

VAR=3

def check_events(ai_settings , screen , ship , bullets) : 
	""" response to keyboard and mouse event """
	for event in pygame.event.get() :
		if event.type == pygame.QUIT : 
			check_quit()
		elif event.type == pygame.KEYDOWN :
			check_keydown_events(event , ai_settings , screen ,  ship , bullets )
		elif event.type == pygame.KEYUP : 
			check_keyup_events(event,ship) 
		


			
def check_keydown_events(event , ai_settings , screen ,  ship , bullets ) :
	if event.key == pygame.K_RIGHT :
		ship.moving_right = True  
	elif event.key == pygame.K_LEFT : 
		ship.moving_left = True  
	elif event.key == pygame.K_UP : 
		ship.moving_up = True 
	elif event.key ==  pygame.K_DOWN : 
		ship.moving_down = True 
	elif event.key == pygame.K_SPACE : 
		fire_bullets(ai_settings, screen , ship , bullets) 
	elif event.key == pygame.K_ESCAPE :
		check_quit() 
	
		
def check_keyup_events(event ,ship) :
	if event.key == pygame.K_RIGHT : 
		ship.moving_right = False 
	elif event.key == pygame.K_LEFT :	
		ship.moving_left = False 
	elif event.key == pygame.K_UP : 
		ship.moving_up = False 
	elif event.key ==  pygame.K_DOWN : 
		ship.moving_down = False 
	

def check_quit() :
	sys.exit()


def fire_bullets(ai_settings , screen , ship , bullets ) :
	new_bullet = Bullet(ai_settings,screen , ship)
	bullets.add(new_bullet)
	


def update_screen(ai_settings , screen , ship , bullets , aliens) :
	screen.fill(ai_settings.bg_color)  
	#充填背景色应该放在 绘制其他图形前，否则会因背景充填而被覆盖
	for bullet in bullets.sprites() :
		bullet.draw_bullet() 
	ship.blitme()
	
	aliens.draw(screen)
	#对编组调用draw()时，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect决定。
	#在这里，aliens.draw(screen)在屏幕上绘制编组中的每个外星人
		
	
	
def update_bullets(aliens, bullets,screen , ship,ai_settings) :
	for bullet in bullets.copy() :
		if bullet.rect.bottom <= 0 :
			bullets.remove(bullet)

	collisions=pygame.sprite.groupcollide(bullets,aliens,False,True)
	#groupcollide可以完成精灵对象组之间的重叠处理。
	#arguments usage see some book 

	if len(aliens)==0 :
		create_fleet(ai_settings,screen,ship,aliens)
		#note scope 




def create_fleet(ai_settings , screen , ship , aliens) : 
	alien = Alien(ai_settings , screen) 
	number_alien_x = get_number_aliens_x(ai_settings , alien.rect.width) 
	number_rows = get_number_rows(ai_settings , ship.rect.height, alien.rect.height)
	
	for row_number in range(number_rows) : 
		for alien_number in range(number_alien_x) : 
			create_alien(ai_settings, screen , aliens, alien_number , row_number ) 
	


def get_number_aliens_x(ai_settings , alien_width) : 
	available_space_x = ai_settings.screen_width - 2 * alien_width 
	number_alien_x = int(available_space_x / (2 * alien_width))
	return number_alien_x 





def get_number_rows(ai_settings , ship_height, alien_height) : 
	available_space_y = (ai_settings.screen_height - 
		(VAR*alien_height) - ship_height)	
	number_rows= int(available_space_y/ (2* alien_height))
	return number_rows 



	
def create_alien(ai_settings , screen , aliens,  alien_number  ,  row_number ) : 
	alien = Alien(ai_settings , screen) 
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height* row_number 
	aliens.add(alien)




def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings , aliens)
			break 


			
def change_fleet_direction(ai_settings , aliens) : 
	for alien in aliens.sprites() :
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *=-1


def over_deal() :
	print("game over")
	check_quit()


def update_aliens(ai_settings, aliens,ship):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens): 
		#非精灵类对象与精灵对象组重叠检测
		over_deal() 

	
