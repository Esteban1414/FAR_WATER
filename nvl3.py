import pygame,sys, random
from classes_nvl3 import Personaje,Items,Background,Animal,Extra,Extra2,Extra3,Boat,WIN_LOSE,Net,Bridge, muestra_texto
from pygame.locals import *

pygame.init()
def nivel_3():
    #constantes
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    flags = FULLSCREEN | DOUBLEBUF
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    pygame.display.set_caption("FARWATER")

    #define game variables
    MAX_ITEMS = 15
    ITEMS_TIMER = 5000
    last_item = pygame.time.get_ticks()
    item_spawn = random.randint(180,200)

    MAX_ANIMALS = 6
    ANIMALS_TIMER = 10000
    last_animal = pygame.time.get_ticks()
    animal_spawn = random.randint(180,200)

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),flags,8)

    #cargado de la carpeta items
    personaje_animations = []
    personaje_types = ['guard']

    items_animations = []
    items_types = ['botella','chips2','petroleo','llanta']

    background_animations = []
    background_types = ['farm']

    animals_animations = []
    animals_types = ['pez']

    extra_animatios = []
    extra_types = ['lifebar']

    extra_2_animatios = []
    extra_2_types = ['number']

    ship_animations = []
    ship_types = ['ship']

    extra_3_animatios = []
    extra_3_types = ['container']

    net_animatios = []
    net_types = ['net']

    ship2_animatios = []
    ship2_types = ['ship2']


    animation_types_1 = ['walk','walk_invert','up','down','fish_1','fish_3']
    for personaje in personaje_types:
        #cargando la animacion
        animations_list_1 =  []
        for animations_1 in animation_types_1:
            #reseteo temporal de lista de imagenes
            temp_list_1 = []
            #definiendo cuantos frames son
            num_of_frames_1 = 3
            for i in range(num_of_frames_1):
                img_1 = pygame.image.load(f'pruebas_pi/personaje/{personaje}/{animations_1}/{i}.png').convert_alpha()
                ll_w_1 = img_1.get_width()
                ll_h_1 = img_1.get_height()
                img_2 = pygame.transform.scale(img_1,(int(ll_w_1*1.4), int(ll_h_1*1.4)))
                temp_list_1.append(img_2)
            animations_list_1.append(temp_list_1)
        personaje_animations.append(animations_list_1)

    animation_types_2 = ['walk']
    for item in items_types:
        #cargando la animacion
        animations_list_2 =  []
        for animations_2 in animation_types_2:
            #reseteo temporal de lista de imagenes
            temp_list_2 = []
            #definiendo cuantos frames son
            num_of_frames_2 = 4
            for i in range(num_of_frames_2):
                img_2 = pygame.image.load(f'pruebas_pi/items/{item}/{animations_2}/{i}.png').convert_alpha()
                ll_w_2 = img_2.get_width()
                ll_h_2 = img_2.get_height()
                img_2 = pygame.transform.scale(img_2,(int(ll_w_2*.5), int(ll_h_2*.5)))
                temp_list_2.append(img_2)
            animations_list_2.append(temp_list_2)
        items_animations.append(animations_list_2)

    animation_types_3 = ['walk']
    for rio in background_types:
        #cargando la animacion
        animations_list_3 =  []
        for animations_3 in animation_types_3:
            #reseteo temporal de lista de imagenes
            temp_list_3 = []
            #definiendo cuantos frames son
            num_of_frames_3 = 6
            for i in range(num_of_frames_3):
                img_3 = pygame.image.load(f'pruebas_pi/fondo/{rio}/{animations_3}/{i}.png').convert_alpha()
                ll_w_3 = img_3.get_width()
                ll_h_3 = img_3.get_height()
                img_2 = pygame.transform.scale(img_3,(int(ll_w_3), int(ll_h_3)))
                temp_list_3.append(img_2)
            animations_list_3.append(temp_list_3)
        background_animations.append(animations_list_3)

    animation_types_4 = ['walk']
    for animals in animals_types:
        #cargando la animacion
        animations_list_4 =  []
        for animations_4 in animation_types_4:
            #reseteo temporal de lista de imagenes
            temp_list_4 = []
            #definiendo cuantos frames son
            num_of_frames_4 = 4
            for i in range(num_of_frames_4):
                img_4 = pygame.image.load(f'pruebas_pi/animals/{animals}/{animations_4}/{i}.png').convert_alpha()
                ll_w_4 = img_4.get_width()
                ll_h_4 = img_4.get_height()
                img_2 = pygame.transform.scale(img_4,(int(ll_w_4*.5), int(ll_h_4*.5)))
                temp_list_4.append(img_2)
            animations_list_4.append(temp_list_4)
        animals_animations.append(animations_list_4)

    animation_types_5 = ['walk']
    for extras in extra_types:
        #cargando la animacion
        animations_list_5 =  []
        for animations_5 in animation_types_5:
            #reseteo temporal de lista de imagenes
            temp_list_5 = []
            #definiendo cuantos frames son
            num_of_frames_5 = 5
            for i in range(num_of_frames_5):
                img_5 = pygame.image.load(f'pruebas_pi/extra/{extras}/{animations_5}/{i}.png').convert_alpha()
                ll_w_5 = img_5.get_width()
                ll_h_5 = img_5.get_height()
                img_2 = pygame.transform.scale(img_5,(int(ll_w_5*.5), int(ll_h_5*.5)))
                temp_list_5.append(img_2)
            animations_list_5.append(temp_list_5)
        extra_animatios.append(animations_list_5)

    animation_types_6 = ['walk']
    for extras_2 in extra_2_types:
        #cargando la animacion
        animations_list_6 =  []
        for animations_6 in animation_types_6:
            #reseteo temporal de lista de imagenes
            temp_list_6 = []
            #definiendo cuantos frames son
            num_of_frames_6 = 4
            for i in range(num_of_frames_6):
                img_6 = pygame.image.load(f'pruebas_pi/extra_2/{extras_2}/{animations_6}/{i}.png').convert_alpha()
                ll_w_6 = img_6.get_width()
                ll_h_6 = img_6.get_height()
                img_2 = pygame.transform.scale(img_6,(int(ll_w_6*.5), int(ll_h_6*.5)))
                temp_list_6.append(img_2)
            animations_list_6.append(temp_list_6)
        extra_2_animatios.append(animations_list_6)


    animation_types_7 = ['walk']
    for ship in ship_types:
        #cargando la animacion
        animations_list_7 =  []
        for animations_7 in animation_types_7:
            #reseteo temporal de lista de imagenes
            temp_list_7 = []
            #definiendo cuantos frames son
            num_of_frames_7 = 2
            for i in range(num_of_frames_7):
                img_7 = pygame.image.load(f'pruebas_pi/fondo/{ship}/{animations_7}/{i}.png').convert_alpha()
                ll_w_7 = img_7.get_width()
                ll_h_7 = img_7.get_height()
                img_2 = pygame.transform.scale(img_7,(int(ll_w_7), int(ll_h_7)))
                temp_list_7.append(img_2)
            animations_list_7.append(temp_list_7)
        ship_animations.append(animations_list_7)

    animation_types_8 = ['walk']
    for extras_3 in extra_3_types:
        #cargando la animacion
        animations_list_8 =  []
        for animations_8 in animation_types_8:
            #reseteo temporal de lista de imagenes
            temp_list_8 = []
            #definiendo cuantos frames son
            num_of_frames_8 = 16
            for i in range(num_of_frames_8):
                img_8 = pygame.image.load(f'pruebas_pi/extra_3/{extras_3}/{animations_8}/{i}.png').convert_alpha()
                ll_w_8 = img_8.get_width()
                ll_h_8 = img_8.get_height()
                img_2 = pygame.transform.scale(img_8,(int(ll_w_8*1), int(ll_h_8*1)))
                temp_list_8.append(img_2)
            animations_list_8.append(temp_list_8)
        extra_3_animatios.append(animations_list_8)

    animation_types_9 = ['walk']
    for net in net_types:
        #cargando la animacion
        animations_list_9 =  []
        for animations_9 in animation_types_9:
            #reseteo temporal de lista de imagenes
            temp_list_9 = []
            #definiendo cuantos frames son
            num_of_frames_9 = 1
            for i in range(num_of_frames_9):
                img_9 = pygame.image.load(f'pruebas_pi/extra/{net}/{animations_9}/{i}.png').convert_alpha()
                ll_w_9 = img_9.get_width()
                ll_h_9 = img_9.get_height()
                img_2 = pygame.transform.scale(img_9,(int(ll_w_9*.8), int(ll_h_9*.8)))
                temp_list_9.append(img_2)
            animations_list_9.append(temp_list_9)
        net_animatios.append(animations_list_9)

    animation_types_10 = ['walk']
    for ship2 in ship2_types:
        #cargando la animacion
        animations_list_10 =  []
        for animations_10 in animation_types_10:
            #reseteo temporal de lista de imagenes
            temp_list_10 = []
            #definiendo cuantos frames son
            num_of_frames_10 = 2
            for i in range(num_of_frames_10):
                img_10 = pygame.image.load(f'pruebas_pi/fondo/{ship2}/{animations_10}/{i}.png').convert_alpha()
                ll_w_10 = img_10.get_width()
                ll_h_10 = img_10.get_height()
                img_2 = pygame.transform.scale(img_10,(int(ll_w_10), int(ll_h_10)))
                temp_list_10.append(img_2)
            animations_list_10.append(temp_list_10)
        ship2_animatios.append(animations_list_10)



    #create group
    personaje_group = pygame.sprite.Group()
    items_group = pygame.sprite.Group()
    background_group = pygame.sprite.Group()
    animals_group = pygame.sprite.Group()
    extras_group = pygame.sprite.Group()
    extras_2_group = pygame.sprite.Group()
    ship_group = pygame.sprite.Group()
    extra_3_group = pygame.sprite.Group()
    net_group = pygame.sprite.Group()
    ship2_group = pygame.sprite.Group()

    personaje_1 = Personaje(personaje_animations[0],500,700,1)#list,x,y,the speed if you move it
    personaje_group.add(personaje_1)

    background_1 = Background(background_animations[0],0,0)#list,xy,
    background_group.add(background_1)

    extra_1 = Extra(extra_animatios[0],1,1,num_of_frames_5)#list,x,y,
    extras_group.add(extra_1)

    extra_2 = Extra2(extra_2_animatios[0],0,0)#list,x,y,
    extras_2_group.add(extra_2)

    ship_1 = Boat(ship_animations[0],0,0)#list,x,y,
    ship_group.add(ship_1)

    extra_3 = Extra3(extra_3_animatios[0],SCREEN_WIDTH-90,0)#list,x,y,
    extra_3_group.add(extra_3)

    net_1 = Net(net_animatios[0],0,0)#list,x,y,
    net_group.add(net_1)

    ship_2 = Bridge(ship2_animatios[0],0,0)#list,x,y,
    ship2_group.add(ship_2)

    while_1 = False
    while not while_1:

        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

        screen.fill(WHITE)

        win_lose=WIN_LOSE()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] or win_lose == 0:
                while_1 = True
                pygame.quit()
                sys.exit()

        #create items
        #check if max of enemy has been reached
        if len(items_group) < MAX_ITEMS:
            #creat items
            if pygame.time.get_ticks() - last_item > ITEMS_TIMER:
                i = random.randint(0,len(items_types)-1)
                speed = random.randint(1,4)
                items = Items(items_animations[i],0,SCREEN_HEIGHT-item_spawn,speed) #list,y,x,the speed if you move it
                items_group.add(items)
                #reset enemy timer 
                last_item = pygame.time.get_ticks()
                ITEMS_TIMER = random.randint(1000,3000)
        
        if len(animals_group) < MAX_ANIMALS:
            #creat items
            if pygame.time.get_ticks() - last_animal > ANIMALS_TIMER:
                j = random.randint(0,len(animals_types)-1)
                animals = Animal(animals_animations[j],SCREEN_WIDTH,SCREEN_HEIGHT-animal_spawn,1) #list,y,x,the speed if you move it
                animals_group.add(animals)
                #reset enemy timer 
                last_animal = pygame.time.get_ticks()
                ANIMALS_TIMER = random.randint(5000,10000)
        
        background_group.update(screen)#draw the background
        items_group.update(screen)#draw the bottle,chips,cans,wheel
        animals_group.update(screen)#draw the fishes
        extras_group.update(screen)#draw the life bar
        extras_2_group.update(screen)#draw the cooldown fishing
        extra_3_group.update(screen)#draw the trash container
        ship_group.update(screen)
        personaje_group.update(screen, items_group,animals_group) #draw the main character
        ship2_group.update(screen)#draw the bridge
        net_group.update(screen)
        muestra_texto()
        pygame.display.flip()