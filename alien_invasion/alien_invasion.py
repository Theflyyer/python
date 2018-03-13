#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu



import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
	'''初始化游戏并定义一个屏幕对象'''
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	# 创建一个存储子弹的编组
	bullets = Group()

	'''开始游戏的主循环'''
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)# 响应事件
		ship.update()# 更新飞船
		gf.update_bullets(bullets)# 更新子弹
		gf.update_screen(ai_settings, screen, ship, bullets)# 更新屏幕

run_game()