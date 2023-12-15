import pygame,sys
import button
pygame.init()
ventana_width = 1400
ventana_height = 800
ventana = pygame.display.set_mode((ventana_width, ventana_height))

#-----------------------CARGAR IMAGENES-------------------------------
#PANTALLA DE INICIO
main_img = pygame.image.load("menu/Pantallas/inicio.png").convert_alpha()

#BOTON START
start_image = pygame.image.load("menu/Botones/play.png").convert_alpha()

#BOTON EXIT
exit_image = pygame.image.load("menu/Botones/exit.png").convert_alpha()

#BOTON CONFIGURACION
settings_image = pygame.image.load("menu/Botones/settings.png").convert_alpha()

#BOTON AUDIO
audio_image = pygame.image.load("menu/Botones/sonido.png").convert_alpha()

#BOTON NO AUDIO
no_audio_image = pygame.image.load("menu/Botones/sin_sonido.png").convert_alpha()

#BOTON DE REGRESO
back_image = pygame.image.load("menu/Botones/back.png").convert_alpha()

#BOTON DE INSTRUCCIONES
instruccions_B = pygame.image.load("menu/Botones/instructions.png").convert_alpha()
instruccions_image = pygame.image.load("menu/Pantallas/intructions.png").convert_alpha()


niveles = pygame.image.load("menu/Pantallas/levels.png").convert_alpha()
dificult = pygame.image.load("menu/Pantallas/difficulty.png").convert_alpha()

#BOTON DE NIVELES
nivel1_img = pygame.image.load("menu/Botones/level 1.png").convert_alpha()
#NIVEL 1 DIFICULTAD:
easy1_img = pygame.image.load("menu/Botones/easy1.png").convert_alpha()
hard1_img = pygame.image.load("menu/Botones/hard1.png").convert_alpha()

nivel2_img = pygame.image.load("menu/Botones/level 2.png").convert_alpha()
#NIVEL 2 DIFICULTAD:
easy2_img = pygame.image.load("menu/Botones/Easy 2.png").convert_alpha()
hard2_img = pygame.image.load("menu/Botones/Hard 2.png").convert_alpha()

nivel3_img = pygame.image.load("menu/Botones/level 3.png").convert_alpha()
#NIVEL 3 DIFICULTAD:
easy3_img = pygame.image.load("menu/Botones/Easy 3.png").convert_alpha()
hard3_img = pygame.image.load("menu/Botones/Hard 3.png").convert_alpha()

#GAME OVER
game_over = pygame.image.load("menu/Pantallas/game_over.png").convert_alpha()

#----------------------MENU PRINCIPAL--------------------
start_button = button.Button(390, 350, start_image, 0.95)
exit_button = button.Button(750, 368, exit_image, 0.80)

settings_button = button.Button(1, 620, settings_image, 0.8)
#----------------------MENU OPCIONES---------------------
instructions_button = button.Button(700, 380, instruccions_B, 0.9)
back_button = button.Button(1280, 685, back_image, 1.25)
audio_button = button.Button(388, 368, audio_image, 0.9)
no_audio_button = button.Button(388, 368, no_audio_image, 0.9)

#-----------------------MENU NIVELES--------------------------
nivel1_button = button.Button(288, 168, nivel1_img, 1)
#-----------------------DIFICULTAD NIVEL 1--------------------
easy1_button = button.Button(390, 350, easy1_img, 1)
hard1_button = button.Button(750, 350, hard1_img, 1)


nivel2_button = button.Button(588, 168, nivel2_img, 1)
#-----------------------DIFICULTAD NIVEL 2--------------------
easy2_button = button.Button(390, 350, easy2_img, 1)
hard2_button = button.Button(750, 350, hard2_img, 1)

nivel3_button = button.Button(888, 168, nivel3_img, 1)
#-----------------------DIFICULTAD NIVEL 3--------------------
easy3_button = button.Button(390, 350, easy3_img, 1)
hard3_button = button.Button(750, 350, hard3_img, 1)
