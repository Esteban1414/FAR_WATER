from Botones import *
from Botones import ventana
from nvl1 import nivel_1
from nvl2 import nivel_2
from nvl3 import nivel_3
from hard1 import nivel_1_hard
from hard2 import nivel_2_hard
from hard3 import nivel_3_hard
from classes import puntuacion
# from classes1 import puntuacion
# from classes_nvl2 import puntaje
# from classes_nvl2_hard import puntaje
# from classes_nvl3 import marcador
# from classes_nvl3_hard import marcador



pygame.display.set_caption("FARWATER")
pygame.mixer.music.load('menu/musica1.mp3')
pygame.mixer.music.play(-1)
def menu():
    global menu_state,while_1
    BLACK=(0,0,0)
    menu_state ="main"
    while_1 = True
    while while_1:            
        ventana.blit(main_img,(0,0))
        if menu_state == "main":
            if start_button.draw(ventana):
                menu_state = "niveles"
            if exit_button.draw(ventana):
                pygame.quit()
            if settings_button.draw(ventana):
                menu_state = "settings"

    #-----------------------MENU NIVELES---------------------
        if menu_state == "niveles":
                ventana.blit(niveles,(0,0))
                if nivel1_button.draw(ventana):
                    menu_state = "nivel 1"
                if nivel2_button.draw(ventana):
                    menu_state = "nivel 2"
                if nivel3_button.draw(ventana):
                    menu_state = "nivel 3"
                if back_button.draw(ventana):
                    menu_state = "main"

    #-----------------------NIVEL 1--------------------------
        if menu_state == "nivel 1":
                ventana.blit(dificult,(0,0))
                if easy1_button.draw(ventana):
                    menu_state = "easy 1"
                if hard1_button.draw(ventana):
                    menu_state = "hard 1"
                if back_button.draw(ventana):
                    menu_state = "niveles"

    #-----------------------EASY 1--------------------------
        if menu_state == "easy 1":
                pygame.mixer.music.load('menu/musica2.mp3')
                pygame.mixer.music.play(-1)
                nivel_1()

    #-----------------------HARD 1--------------------------
        if menu_state == "hard 1":
                pygame.mixer.music.load('menu/musica2.mp3')
                pygame.mixer.music.play(-1)
                nivel_1_hard()
               
    #-----------------------NIVEL 2--------------------------
        if menu_state == "nivel 2":
                ventana.blit(dificult,(0,0))
                if easy2_button.draw(ventana):
                    menu_state = "easy 2"
                if hard2_button.draw(ventana):
                    menu_state = "hard 2"
                if back_button.draw(ventana):
                    menu_state = "niveles"

    #-----------------------EASY 2--------------------------
        if menu_state == "easy 2":
                pygame.mixer.music.load('menu/musica2.mp3')
                pygame.mixer.music.play(-1)
                nivel_2()
                
    #-----------------------HARD 2--------------------------
        if menu_state == "hard 2":
                pygame.mixer.music.load('menu/musica2.mp3')
                pygame.mixer.music.play(-1)
                nivel_2_hard()
    
    #-----------------------NIVEL 3--------------------------
        if menu_state == "nivel 3":
                ventana.blit(dificult,(0,0))
                if easy3_button.draw(ventana):
                    menu_state = "easy 3"
                if hard3_button.draw(ventana):
                    menu_state = "hard 3"
                if back_button.draw(ventana):
                    menu_state = "niveles"

    #-----------------------EASY 3--------------------------
        if menu_state == "easy 3":
                pygame.mixer.music.load('menu/musica2.mp3')
                pygame.mixer.music.play(-1)
                nivel_3()
            
    #-----------------------HARD 3--------------------------
        if menu_state == "hard 3":
                pygame.mixer.music.load('menu/musica2.mp3')
                pygame.mixer.music.play(-1)
                nivel_3_hard()

    #-----------------------OPCIONES-------------------------
        if menu_state == "settings":
                if audio_button.draw(ventana):
                    menu_state = "audio"
                    pygame.mixer.music.set_volume(0)
                if back_button.draw(ventana):
                    menu_state = "main"
                if instructions_button.draw(ventana):
                    menu_state = "instructions"
                    
    #-----------------------AUDIO----------------------------
        if menu_state == "audio":
                if no_audio_button.draw(ventana):
                    menu_state = "settings"
                    pygame.mixer.music.set_volume(1)
                if back_button.draw(ventana):
                    menu_state = "main" 
                if instructions_button.draw(ventana):
                    menu_state = "instructions"

    #-----------------------INSTRUCCIONES--------------------
        if menu_state == "instructions":
                ventana.blit(instruccions_image,(0,0))
                if back_button.draw(ventana):
                    menu_state = "settings"
        for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    while_1 = False
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()