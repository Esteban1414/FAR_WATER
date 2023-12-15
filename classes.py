import pygame, random, time, threading
from Botones import *
pygame.init()

BLACK = (0,0,0)
coords = [0,0]
flag_2 = 0
flag_1 = 0
score = 0
i_timer = 0
win_lose = 2
flag_3 = 0
count = 4
puntuacion = 0
def timer():
    global i_timer,flag_3,coords
    i_timer = 1
    while(True):
        time.sleep(1)
        #print(i_timer)
        i_timer += 1
        if i_timer >= 4:
            i_timer = 1
            break
    i_timer = 0

letra = pygame.font.SysFont('times', 40, True)
def muestra_texto():
    show_score = letra.render('Score: '+ str(puntuacion), 1, BLACK)
    ventana.blit(show_score,(650,15))
class Personaje(pygame.sprite.Sprite):
    def __init__(self, animation_list,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.update_time_1 = pygame.time.get_ticks()
        self.ANIMATION_COOLDOWN = 70 #the time when the frame change
        self.update_time_2 = pygame.time.get_ticks()
        self.FISH_COOLDOWN = 3050 #the time when the fishing mechanic is available

        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,40,40)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface, items_group, animals_group):
        #draw image screen
        #pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x-90,self.rect.y-310))

        global coords,flag_2,flag_1,score,puntuacion, menu_state
        move_ticker = 0
        keyboard = pygame.key.get_pressed()
        click = pygame.mouse.get_pressed()
        fish_1 = False
        fish_2 = False    
        right_limit = 1200
        left_limit = 400
        up_limit = 620
        down_limit = 675
        timer_function = threading.Thread(target=timer)
        coords = [self.rect.x,self.rect.y]

        #move the character RIGHT and LEFT
        if keyboard[pygame.K_d] or keyboard[pygame.K_RIGHT]:
            self.update_action(0)
            #move item
            if move_ticker == 0:
                move_ticker = 10
                #update rectangle position
                self.rect.x += self.speed
                self.update_animation()
                if self.rect.x > right_limit:
                    self.rect.x = right_limit - 1
        if keyboard[pygame.K_a] or keyboard[pygame.K_LEFT]:
            self.update_action(1)
            #move item
            if move_ticker == 0:
                move_ticker = 10
                #update rectangle position
                self.rect.x -= self.speed
                self.update_animation()
                if self.rect.x < left_limit:
                    self.rect.x = left_limit - 1

        #move the character UP and DOWN
        if keyboard[pygame.K_s] or keyboard[pygame.K_DOWN]:
            self.update_action(3)
            #move item
            if move_ticker == 0:
                move_ticker = 10
                #update rectangle position
                self.rect.y += self.speed
                self.update_animation()
                if self.rect.y > down_limit:
                    self.rect.y = down_limit - 1
        if keyboard[pygame.K_w] or keyboard[pygame.K_UP]:
            self.update_action(2)
            #move item
            if move_ticker == 0:
                move_ticker = 10
                #update rectangle position
                self.rect.y -= self.speed
                self.update_animation()
                if self.rect.y < up_limit:
                    self.rect.y = up_limit - 1

        #the character will fish
        if keyboard[pygame.K_RETURN] or keyboard[pygame.K_e] or click[0]:
            fish_1 = True #especial action part 1/2
        else:
            fish_1 = False #remove the frist especial animation in order to do the sencond 
            fish_2 = True    

        if fish_1 == True and move_ticker == 0:
            self.update_action(4) #update especial action part 1/2
            self.update_animation()
         
        if fish_2 == True and fish_1 == False and self.action == 4 and pygame.time.get_ticks() - self.update_time_2 > self.FISH_COOLDOWN:
            self.update_action(5) #update especial action part 2/2
            self.update_animation()
            self.update_time_2 = pygame.time.get_ticks()
            timer_function.start()
            #check for collitions
            if pygame.sprite.spritecollide(self,items_group,True):
                score += 30
                flag_1 = 1
                puntuacion +=30
                
            if pygame.sprite.spritecollide(self,animals_group,True):
                flag_2 = 1  

        #help for the movement and tha actions changes
        if move_ticker > 0:
            move_ticker -= 1   
        
    def update_animation(self):
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time_1 > self.ANIMATION_COOLDOWN:
            self.update_time_1 = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        #check if the new action is differnet to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_date = pygame.time.get_ticks()


#+=================================================================================================================

class Items(pygame.sprite.Sprite):
    def __init__(self, health, animation_list,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed #the pixels jump between the other pixels
        self.animation_list = animation_list
        self.health = health
        self.frame_index = 0
        self.action = 0
        self.update_time_1 = pygame.time.get_ticks()
        self.update_time_2 = pygame.time.get_ticks()
        self.ANIMATION_COOLDOWN_1 = 800 #the time when the frame change
        self.ANIMATION_COOLDOWN_2 = 20 #the speed of the items

        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,50,50)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface):
        #draw image screen
        #pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x-25,self.rect.y-50))

        right_limit = 1400

        #move item
        self.update_animation()
        if pygame.time.get_ticks() - self.update_time_2 > self.ANIMATION_COOLDOWN_2:
            self.update_time_2 = pygame.time.get_ticks()
            self.rect.x += self.speed #move the items from width until the limit width
        #when reach the width screen limit, move at the start and repeat
        if self.rect.x > right_limit: #or temp_health == 0:
            self.rect.x = -100
            ramdom_y = random.randint(600,680) #update the ramdom place
            self.rect.y = ramdom_y #move in a ramdom place

    def update_animation(self):
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time_1 > self.ANIMATION_COOLDOWN_1:
            self.update_time_1 = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

#+=================================================================================================================

class Background(pygame.sprite.Sprite):
    def __init__(self, animation_list,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.update_time_1 = pygame.time.get_ticks()
        self.ANIMATION_COOLDOWN = 800 #the time when the frame change

        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,1,1)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface):
        #draw image screen
        pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x,self.rect.y))

        self.update_animation()

    def update_animation(self):
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time_1 > self.ANIMATION_COOLDOWN:
            self.update_time_1 = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

#+=================================================================================================================

class Animal(pygame.sprite.Sprite):
    def __init__(self, health, animation_list,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed #the pixels jump between the other pixels
        self.animation_list = animation_list
        self.health = health
        self.frame_index = 0
        self.action = 0
        self.update_time_1 = pygame.time.get_ticks()
        self.update_time_2 = pygame.time.get_ticks()
        self.ANIMATION_COOLDOWN_1 = 800 #the time when the frame change
        self.ANIMATION_COOLDOWN_2 = 10 #the speed of the items

        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,50,25)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface):
        #draw image screen
        #pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x,self.rect.y))

        left_limit = -100

        #move item
        self.update_animation()
        if pygame.time.get_ticks() - self.update_time_2 > self.ANIMATION_COOLDOWN_2:
            self.update_time_2 = pygame.time.get_ticks()
            self.rect.x -= self.speed #move the items from width until the limit width
        #when reach the width screen limit, move at the start and repeat
        if self.rect.x < left_limit: #or temp_health == 0:
            self.rect.x = 1500
            ramdom_y = random.randint(600,680) #update the ramdom place
            self.rect.y = ramdom_y #move in a ramdom place

    def update_animation(self):
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time_1 > self.ANIMATION_COOLDOWN_1:
            self.update_time_1 = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

#+=================================================================================================================

class Extra(pygame.sprite.Sprite):
    def __init__(self, animation_list,x,y,num_frames):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.num_frames = num_frames - 1

        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,40,40)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface):
        #draw image screen
        pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x,self.rect.y))

        self.update_animation()

    def update_animation(self):
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]

        global flag_2, score, puntuacion

        if flag_2 == 1:
            self.frame_index += 1
            flag_2 = 0
        #if the animatios has ended, which means all the life is out
        if  self.frame_index >= self.num_frames:
            score = -1000
            puntuacion = 0
            self.frame_index = self.num_frames

class Extra2(pygame.sprite.Sprite):
    def __init__(self, animation_list,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.x_main = 0
        self.y_main = 0

        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,1,1)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface):
        #draw image screen
        pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x,self.rect.y))

        self.update_animation()

    def update_animation(self):
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]

        global coords, i_timer

        temp_x = coords[0]
        temp_y = coords[1] - 350

        self.frame_index = i_timer
        self.rect.x = temp_x
        self.rect.y = temp_y

class Boat(pygame.sprite.Sprite):
    def __init__(self, animation_list,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.update_time_1 = pygame.time.get_ticks()
        self.ANIMATION_COOLDOWN = 800 #the time when the frame change


        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,1,1)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface):
        #draw image screen
        pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x,self.rect.y))

        self.update_animation()
    
    def update_animation(self):
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time_1 > self.ANIMATION_COOLDOWN:
            self.update_time_1 = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

#+=================================================================================================================

class Extra3(pygame.sprite.Sprite):
    def __init__(self, animation_list,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.update_time_1 = pygame.time.get_ticks()
        self.ANIMATION_COOLDOWN = 500 #the time when the frame change

        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,1,1)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface):
        #draw image screen
        pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x,self.rect.y))

        global flag_1,count

        if flag_1 == 1:
            self.update_animation()

    def update_animation(self):
        global count,flag_1
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time_1 > self.ANIMATION_COOLDOWN and count <= 4:
            self.update_time_1 = pygame.time.get_ticks()
            self.frame_index += 1
            count -= 1
            if count == 0:
                count = 3
                flag_1 = 0
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            count = 4

#+=================================================================================================================
def WIN_LOSE():
    global score, win_lose, flag_3 
    if score > 60 and flag_3 == 0:
        flag_3 = 1
        if (flag_3 == 1):
            print('you win')
            flag_3 = 2
            ventana.blit(game_over,(0,0))
        win_lose = 1
    elif score < 0 and flag_3 == 0:
        flag_3 = 1 
        if (flag_3 == 1):
            print('score = ',score)
            print('you lose')
            flag_3 = 2
        win_lose = 0
    if win_lose == 0:
        ventana.blit(game_over,(0,0))
    return win_lose


class Net(pygame.sprite.Sprite):
    def __init__(self, animation_list,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.x_main = 0
        self.y_main = 0

        #selec starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,1,1)#to modify the rectangle size
        self.rect.center = (x,y)

    def update(self,surface):
        #draw image screen
        #pygame.draw.rect(surface,(0,0,0),self.rect,1) #to see the rectangle in the animation
        surface.blit(self.image,(self.rect.x,self.rect.y))

        global coords

        temp_x = coords[0] - 15
        temp_y = coords[1] - 15

        self.rect.x = temp_x
        self.rect.y = temp_y
