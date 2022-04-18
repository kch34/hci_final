#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:20:05 2022

@author: kch34
"""
import pygame,time

panel_width  = 1600 
panel_height = 800

energy_text= ["Is nuclear energy is the leading source of clean energy in the US?",
                "Are nuclear energy related disasters the most common energy related disasters?",
                "How much does human error factor into nuclear reactor issues?",
                "Does nuclear power only impact the energy sector?",
                "Do price flucuations affect nuclear energy like it does for other nonrenewable energies such as coal and gas?",
                "Do nuclear plants require a high cost to maintain after construction?",
                "Is nuclear power the most reliable form of energy?",
                "Will nuclear power plants become obsolete once the world runs out of uranium?",
                "Does nuclear energy have the highest energy density of renewable and nonrenewable resources?",
                "Does nuclear energy affect people’s everyday lives?",
                "Is nuclear energy vital for the future of electric cars?",
                "How many jobs does the nuclear sector result in?",
                "Is nuclear energy a crucial energy source for the US military?",
                "How many countries use nuclear energy?"
                ]
weapons_text = ["Are nuclear weapons high or low yield devices compared the Hiroshima and Nagasaki Bombs of WW2?",
               "How many nations have nuclear weapons?",
               "How many nuclear weapons are there worldwide?",
               "Are nuclear weapons maintenance costs high or low?",
               "Are nuclear weapons accidents rare?",
               "Was the Cuban Missile Crisis was the closest we’ve come to nuclear war?",
               "Are limited Nuclear Exchanges are survivable?",
               "Does nuclear energy spread nuclear weapons?",
               "Can we defend against nuclear weapons?",
               "What is the risk of nuclear war?",
               "Are today’s nuclear weapons far more powerful than those in the Cold War?",
               "Can the US be certain if someone were to launch nuclear missiles at them?",
               "Are nuclear weapons tests done in a manner in which they have no adverse effects on humans?",
               "blank"
               ]

e_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#image 1
ind = 0
img = 'en_0'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 2
ind = 1
img = 'en_1'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 3
ind = 2
img = 'en_2'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 4
ind = 3
img = 'en_3'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 5
ind = 4
img = 'en_4'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 6
ind = 5
img = 'en_5'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 7
ind = 6
img = 'en_6'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 8
ind = 7
img = 'en_7'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 9
ind = 8
img = 'en_8'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 10
ind = 9
img = 'en_9'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 11
ind = 10
img = 'en_10'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 12
ind = 11
img = 'en_11'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 13
ind = 12
img = 'en_12'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))
#image 14
ind = 13
img = 'en_13'
e_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
e_list[ind]   = pygame.transform.scale(e_list[ind] , (panel_width, panel_height-40))




w_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#image 1
ind = 0
img = 'w_0'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 2
ind = 1
img = 'w_1'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 3
ind = 2
img = 'w_2'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 4
ind = 3
img = 'w_3'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 5
ind = 4
img = 'w_4'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 6
ind = 5
img = 'w_5'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 7
ind = 6
img = 'w_6'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 8
ind = 7
img = 'w_7'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 9
ind = 8
img = 'w_8'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 10
ind = 9
img = 'w_9'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 11
ind = 10
img = 'w_10'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 12
ind = 11
img = 'w_11'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 13
ind = 12
img = 'w_12'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))
#image 14
ind = 13
img = 'w_13'
w_list[ind]  = pygame.image.load(r'{}.jpg'.format(img))
w_list[ind]   = pygame.transform.scale(w_list[ind] , (panel_width, panel_height-40))







pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((panel_width, panel_height))


menu_image  = pygame.image.load(r'test.jpg')
menu_image  = pygame.transform.scale(menu_image, (panel_width, panel_height-40))
black_image = pygame.image.load(r'blck.jpg')
black_image  = pygame.transform.scale(black_image, (panel_width, panel_height-40))



main_menu  = True
draw_left  = True
draw_middle = True
draw_right = True
weapons_menu = False
energy_menu = False
weapon_list   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
energy_list   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# white color
color = (255,255,255)
#black color
color2 = (0,0,0)
# light shade of the button
color_light = (170,170,170)
# dark shade of the button
color_dark = (100,100,100)
# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
textmiddle = smallfont.render('Feedback' , True , color)

def draw_menu_buttons(window_surface,mouse,panel_height,panel_width,color,color_dark,color_light,textybois,clicked):
    smallfont = pygame.font.SysFont('Corbel',25)
    click_list   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #color shading for the button
    x = panel_width/2 -500
    y = 50
    w = 1000
    q = 0
    for i in textybois:
        #statement 1
        text = smallfont.render(i , True , color)
        if y<= mouse[0] <= x+w and y-40 <= mouse[1] <= y-40+40:
            pygame.draw.rect(window_surface,color_light,[x,y-40,w,40])  
            if clicked == True:
                click_list[q] = 1
            else:
                click_list[q] = 0
        else:
            pygame.draw.rect(window_surface,color_dark,[x,y-40,w,40])
            click_list[q] = 0
        # superimposing the text onto our button
        window_surface.blit(text,(x+10,y-30))
        y+=45
        q+=1
    return click_list
    
clicked      = False
while True:
    left_click   = False
    middle_click = False
    right_click  = False

    mouse = pygame.mouse.get_pos()
    

    if main_menu == True:
        #draw image itself
        window_surface.blit(menu_image, (0, 0))
        # rendering a text written in
        textleft = smallfont.render('Weapons' , True , color)
        textright = smallfont.render('Energy' , True , color)
    elif energy_menu == True:
        textleft = smallfont.render('Back' , True , color)
        textright = smallfont.render('' , True , color)
        if 1 in energy_list:
            slide = energy_list.index(1)
            window_surface.blit(e_list[slide], (0, 0))
        else:
            energy_list = draw_menu_buttons(window_surface,mouse,panel_height,panel_width,color,color_dark,color_light,energy_text,clicked)
    elif weapons_menu == True:
        textleft = smallfont.render('Back' , True , color)
        textright = smallfont.render('' , True , color)
        if 1 in weapon_list:
            slide = weapon_list.index(1)
            window_surface.blit(w_list[slide], (0, 0))
        else:
            weapon_list = draw_menu_buttons(window_surface,mouse,panel_height,panel_width,color,color_dark,color_light,weapons_text,clicked)
    clicked      = False
        
    
        
    #always draw and check for the Left button
    if draw_left == True:
        #color shading for the button
        if 0<= mouse[0] <= 0+140 and panel_height-40 <= mouse[1] <= panel_height-40+40:
            pygame.draw.rect(window_surface,color_light,[0,panel_height-40,140,40])   		
            left_click=True
        else:
            pygame.draw.rect(window_surface,color_dark,[0,panel_height-40,140,40])
        # superimposing the text onto our button
        window_surface.blit(textleft ,(0+10,panel_height-30))
    #Always draw and check for the feedback button
    if draw_middle == True:
        #color shading for the button
        if (panel_width/2 -140)<= mouse[0] <= (panel_width/2 -140)+140 and panel_height-40 <= mouse[1] <= panel_height-40+40:
            pygame.draw.rect(window_surface,color_light,[(panel_width/2 -140),panel_height-40,140,40])
            middle_click=True    
        else:
            pygame.draw.rect(window_surface,color_dark,[(panel_width/2 -140),panel_height-40,140,40])
        # superimposing the text onto our button
        window_surface.blit(textmiddle ,((panel_width/2 -140)+20,panel_height-30))        
    #Always draw and check for the right Button
    if draw_right == True:
        #color shading for the button
        if (panel_width-140)<= mouse[0] <= (panel_width-140)+140 and panel_height-40 <= mouse[1] <= panel_height-40+40:
            pygame.draw.rect(window_surface,color_light,[(panel_width-140),panel_height-40,140,40])   	
            right_click=True    
        else:
            pygame.draw.rect(window_surface,color_dark,[(panel_width-140),panel_height-40,140,40])
        # superimposing the text onto our button
        window_surface.blit(textright ,((panel_width-140)+20,panel_height-30))  
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    	#checks if a mouse is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            #middle button press
            #left button press
            if left_click == True and energy_menu == True:
                if 1 in energy_list:
                    window_surface.blit(black_image, (0, 0))                
                    energy_list   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    
                else:
                    main_menu    = True
                    energy_menu  = False
                    weapons_menu = False            
            elif left_click == True and weapons_menu == True:
                if 1 in weapon_list:
                    window_surface.blit(black_image, (0, 0))                
                    weapon_list   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                else:
                    main_menu    = True
                    energy_menu  = False
                    weapons_menu = False 
            elif left_click == True and main_menu == True:
                main_menu   = False
                energy_menu = False
                weapons_menu = True
                window_surface.blit(black_image, (0, 0))                
            #right button press
            if right_click == True and main_menu == True:
                main_menu   = False
                weapons_menu = False
                energy_menu = True
                window_surface.blit(black_image, (0, 0))
                
    pygame.display.update()
    #sleep to delay 
    time.sleep(0.00001)
