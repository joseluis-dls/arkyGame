import pygame, random, sys  
from pygame import *
from niveluno import nivel1
from nivel2 import nivel2
from nivel3 import nivel3
from mainesp import menuesp
from nvll1rep import nivel1rep

#Pantalla - ventana
W, H = 700, 400           #VALORES PARA EL TAMAÑO DE LA VENTANA 
#COLORES
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
GRIS = (176, 168, 167)

pygame.init()   #INICIALIZAR PYGAME
pygame.mixer.init()     # INICIALIZAR EL SONIDO
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption("Arky(Medes)")           # NOMBRE DE LA PANTALLA EN DONDE SE MUESTRA EL JUEGO
icono=pygame.image.load("imagenes/imagenes/arky.png")    # ICONO DE LA PANTALLA DONDE SE MUESTRA EL JUEGO
pygame.display.set_icon(icono)
clock = pygame.time.Clock()  #CONTROLAR LA CANTIDAD DE FPS DEL JUEGO
go = pygame.image.load("imagenes/imagenes/fondo 1.png").convert()

sonido_boton = pygame.mixer.Sound("sonidoboton2.mp3")
sonido_has_perdido = pygame.mixer.Sound("sonidohasperdido.mp3") 

    #MUSICA JUEGO
pygame.mixer.music.load("musica start.mp3")
pygame.mixer.music.set_volume(0.5)     #MODIFICADOR DE VOLUMEN DE MUSICA DEL JUEGO

#MUSICA JUEGO
pygame.mixer.music.play(loops=-1)  #HACER QUE SE ESCUCHE LA MUSICA DEL JUEGO Y QUE ENTRE EN UN LOOP


def inicio():     #FUNCION NIVEL 2
    PANTALLA.blit(go, [0,0])        #SE INGRESA IMAGEN
    pygame.display.flip()
    waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
    while waiting:          #MIENTRAS SE ESPERA
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                if event.key == pygame.K_SPACE:
                    sonido_boton.play()
                    waiting = False  # SE DEJA DE ESPERAR

#BUCLE PRINCIPAL
running = True  
nivel_dos = True
while running:
    inicio()
    from main import menu

    


    clock.tick(60) #60 FPS

    pygame.display.flip()
pygame.QUIT
