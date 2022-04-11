#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:20:05 2022

@author: kch34
"""

import pygame

panel_width  = 3000
panel_height = 1500

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((panel_width, panel_height))


image = pygame.image.load(r'test3.jpg')
image = pygame.transform.scale(image, (panel_width, panel_height))



background = pygame.Surface((panel_width, panel_height))
background.fill(pygame.Color('#000000'))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    window_surface.blit(background, (0, 0))
    window_surface.blit(image, (0, 0))
    pygame.display.update()