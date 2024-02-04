from pygame import *
from random import *
font.init()
import sys
import json

win_width = 700
win_hight = 500 

window = display.set_mode((win_width,win_hight))
display.set_caption("Shooter")
background1 = transform.scale(image.load("Ball_Game_map.png").convert(),(win_width,win_hight))
run = True


'''Замітки в json'''
saveDict = {
    "Level" : 1,
    "live" : 100,
    "power" : 100,
    "sword": "меч.png"

}
#with open("save.json", "w",encoding="utf-8") as file:
#    json.dump(saveDict, file)


# клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale( image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))     

class Player(GameSprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.animation_set = [transform.scale(image.load(f"playerAnim/player{i}.png"),(50,50)) for i in range(1, 17)]
        self.i = 0


    def update(self):
        
        move = False
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            move = True
            self.i+=1
            self.rect.x -=self.speed
            self.image = self.animation_set[self.i%4 + 4]

        if keys[K_RIGHT] and self.rect.x < win_width-80:
            move = True
            self.i+=1
            self.rect.x +=self.speed
            self.image = self.animation_set[self.i%4 + 8]

        if keys [K_UP] and self.rect.y > 5:
            move = True
            self.i+=1
            self.rect.y -=5
            self.image = self.animation_set[self.i %4 + 12]

        if keys[K_DOWN] and self.rect.y < win_hight-80:
            move = True
            self.i+=1
            self.rect.y +=5
            self.image = self.animation_set[self.i%4]
        
        #if move == False:
        #    self.i+=4
        #    self.image = self.animation_set[self.i%16]
            
        
class _Event(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((wall_width, wall_height))
        self.image.fill(color)
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

class TextArea():
    def __init__(self, x,y, width = 10, height=10, color = None):
        self.rect = Rect(x,y,width,height)
        self.fill_color = color
         
    def set_text(self,text, fsize = 12, text_color = (0,0,0)):
        self.image = font.Font(None,fsize).render(text,True,text_color)

    def draw(self, shift_x = 0,shift_y = 0):
        draw.rect(window,self.fill_color,self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)   


player = Player("player.png",250,320,20,40,5)

LIGHT_BLUE = (200,200,255)
card = TextArea(120,100,290,70, LIGHT_BLUE)
card.set_text("Hello, im Sans",50)

 
 

background1 = transform.scale(image.load("Ball_Game_map.png").convert(),(win_width,win_hight))
enemySans = _Event((154, 205, 50), 550, 70, 30, 10)
nextLocal = _Event((54, 205, 50), 600, 350, 50, 100)



level = 1

def save():
    with open("save.json", "w",encoding="utf-8") as file:
        saveDict["Level"] = level
        
        json.dump(saveDict, file)

def load():
    with open("save.json","r",encoding="utf-8") as file:
        saveDict = json.load(file)
        global level
        level = saveDict["Level"]

def level1():
    global level
    window.blit(background1,(0,0))
     
    if sprite.collide_rect(player,enemySans):
        if mouse.get_pressed()[0]:
            if card.collidepoint( mouse.get_pos()[0], mouse.get_pos()[1]):
                card.fill_color = (randint(0,255),randint(0,255),randint(0,255))

        card.draw()
    
    if sprite.collide_rect(player,nextLocal):
        print(1)
        player.rect.x = 50
        player.rect.y = 230
        level = 2
        
    enemySans.draw_wall()
    nextLocal.draw_wall()


background2 = transform.scale(image.load("PapyrusSentryStation.png").convert(),(win_width,win_hight))
prevLocal = _Event((54, 205, 50), 0, 230, 50, 150)


def level2():
    global level
    window.blit(background2,(0,0))
    
    if sprite.collide_rect(player,prevLocal):
       
        print(2)
        player.rect.x = 550
        player.rect.y = 350
        level = 1

    prevLocal.draw_wall()
 


font = font.SysFont(None, 30)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
# Main container function that holds the buttons and game functions

def main_menu():
    backgroundMenu = transform.scale(image.load("mainMenu.jpg").convert(),(win_width,win_hight))
    click = False
    while True:
 
        window.blit(backgroundMenu,(0,0))
        draw_text('Main Menu', font, (255,255,255), window, 250, 40)
         #creating buttons
        button_1 = Rect(200, 100, 200, 50)
        button_2 = Rect(200, 180, 200, 50)
        
        
        mx, my = mouse.get_pos()
 
        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            draw.rect(window, (155,255, 0), button_1)
            if click:
                load()
                run()
        else:
            draw.rect(window, (255, 0, 0), button_1)
        if button_2.collidepoint((mx, my)):
            draw.rect(window, (155, 155, 0), button_2)
            if click:
                options()
        else:
            draw.rect(window, (255, 0, 0), button_2)
 
        #writing text on top of button
        draw_text('PLAY', font, (255,255,255), window, 270, 115)
        draw_text('Level', font, (255,255,255), window, 250, 195)


        click = False
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    quit()
                    sys.exit()
            if e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    click = True
 
        display.update()
        time.delay(60)
 
backgroundOptions = transform.scale(image.load("options.jpg").convert(),(win_width,win_hight))
def options():
    running = True
    global level
    #window = display.set_mode((1000,700))
    lv1 = GameSprite("Ball_Game_map.png",100,100 , 200,200,0)
    lv2 = GameSprite("PapyrusSentryStation.png",400,100 , 200,200,0)

    click = False
    while running:
        window.blit(backgroundOptions,(0,0))
 
        draw_text('OPTIONS SCREEN', font, (255, 255, 255), window, 20, 20)
        
        lv1.reset()
        lv2.reset()
          #writing text on top of button
        draw_text('Level 1', font, (255,255,255), window, 100, 300)
        draw_text('Level 2', font, (255,255,255), window, 400, 300)
        
        mx, my = mouse.get_pos()
 
        #defining functions when a certain button is pressed
        if lv1.rect.collidepoint((mx, my)):
             
            if click:
                print("click")
                level = 1
                run()
         
        if lv2.rect.collidepoint((mx, my)):
            if click:
                level = 2
                run()
 
 
      


        click = False
  
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    running = False
            if e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    click = True

       
        display.update()
        time.delay(60)

 


def run():
    while run:

        for e in event.get():
            if e.type == QUIT:
                save()
                quit()
                sys.exit()

            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    main_menu()

        if level == 1:
            level1()
        elif level == 2:
            level2()
    
        player.update()
        player.reset()

        display.update()
        time.delay(50)

main_menu()
