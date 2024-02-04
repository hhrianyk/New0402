from pygame import *

background1 = transform.scale(image.load("Ball_Game_map.png").convert(),(win_width,win_hight))

def level1():
    window.blit(background1,(0,0))
     
    if sprite.collide_rect(player,enemySans):
       
        for event in event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
           
                if card.collidepoint(x,y):
                    card.fill_color = (0,250,250)

        card.draw()
