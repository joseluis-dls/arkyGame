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
main_menu = False
font = pygame.font.SysFont("serif", 30)  #SELECCIONAR UNA FUENTE
go = pygame.image.load("imagenes/imagenes/fondo 1.png").convert()
fondo = pygame.image.load("imagenes/imagenes/nuevo fondo.jpeg").convert()
niveles = pygame.image.load("imagenes/imagenes/levels2.png").convert()
volumen = pygame.image.load("imagenes/imagenes/pantalla volumen.png").convert()
pantalla_botones = pygame.image.load("imagenes/imagenes/botones pantalla.png").convert()
pantalla_idioma = pygame.image.load("imagenes/imagenes/language.png").convert()

sonido_boton = pygame.mixer.Sound("sonidoboton2.mp3")
sonido_has_perdido = pygame.mixer.Sound("sonidohasperdido.mp3") 

    #MUSICA JUEGO
pygame.mixer.music.load("menu music.mp3")
pygame.mixer.music.set_volume(0.5)     #MODIFICADOR DE VOLUMEN DE MUSICA DEL JUEGO

#MUSICA JUEGO
pygame.mixer.music.play(loops=-1)  #HACER QUE SE ESCUCHE LA MUSICA DEL JUEGO Y QUE ENTRE EN UN LOOP

#BOTONES
boton_nivel_1 = pygame.Rect(160,150,140,50)
boton_nivel_2 = pygame.Rect(160,220,140,50)
boton_nivel_3 = pygame.Rect(160,290,140,50)
boton_opciones = pygame.Rect(10,20,80,50)
boton_volumen = pygame.Rect(250,120,250,50)
boton_quitar_vol = pygame.Rect(120,100,250,50)
boton_poner_vol = pygame.Rect(300,100,250,50)
boton_idioma = pygame.Rect(250,280,250,50)
boton_español = pygame.Rect(160,150,140,50)
boton_ingles = pygame.Rect(160,200,50,50)
boton_menu = pygame.Rect(160,290,140,50)

class Tuerca(pygame.sprite.Sprite):     #CREACION DE CLASE PARA EL PERSONAJE
    def __init__(self):             #INICIALIZAR LA CLASE
        super().__init__()          #INICIALIZAR LA SUPER CLASE
        self.image = pygame.image.load("imagenes/imagenes/tuerca.png").convert()  #AGREGANDO PERSONAJE, #COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
        self.image.set_colorkey(NEGRO) #CON ESTA FUNCION SE REMUEVE EL FONDO NEGRO DE LA IMAGEN
        self.rect = self.image.get_rect()  #OBTENER LA RECTA O CUADRO DEL SPRITE
        self.rect.centerx = W // 11     #PONERLO EN PANTALLA
        self.rect.bottom = H -330       #PONERLO EN PANTALLA
        self.speed_x = 0                #MODIFICAR LA VELOCIDAD DEL PERSONAJE
        self.shield = 100               #MODIFICAR LA VIDA DEL PERSONAJE

class Boton1(pygame.sprite.Sprite):     #CREACION DE CLASE PARA EL PERSONAJE
    def __init__(self):             #INICIALIZAR LA CLASE
        super().__init__()          #INICIALIZAR LA SUPER CLASE
        self.image = pygame.image.load("imagenes/imagenes/boton nv1.png").convert()  #AGREGANDO PERSONAJE, #COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
        self.image.set_colorkey(NEGRO) #CON ESTA FUNCION SE REMUEVE EL FONDO NEGRO DE LA IMAGEN
        self.rect = self.image.get_rect()  #OBTENER LA RECTA O CUADRO DEL SPRITE
        self.rect.centerx = W // 3     #PONERLO EN PANTALLA
        self.rect.bottom = H -200       #PONERLO EN PANTALLA
        self.speed_x = 0                #MODIFICAR LA VELOCIDAD DEL PERSONAJE
        self.shield = 100               #MODIFICAR LA VIDA DEL PERSONAJE

class Boton2(pygame.sprite.Sprite):     #CREACION DE CLASE PARA EL PERSONAJE
    def __init__(self):             #INICIALIZAR LA CLASE
        super().__init__()          #INICIALIZAR LA SUPER CLASE
        self.image = pygame.image.load("imagenes/imagenes/boton nv2.png").convert()  #AGREGANDO PERSONAJE, #COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
        self.image.set_colorkey(NEGRO) #CON ESTA FUNCION SE REMUEVE EL FONDO NEGRO DE LA IMAGEN
        self.rect = self.image.get_rect()  #OBTENER LA RECTA O CUADRO DEL SPRITE
        self.rect.centerx = W // 3     #PONERLO EN PANTALLA
        self.rect.bottom = H -130       #PONERLO EN PANTALLA
        self.speed_x = 0                #MODIFICAR LA VELOCIDAD DEL PERSONAJE
        self.shield = 100               #MODIFICAR LA VIDA DEL PERSONAJE

class Boton3(pygame.sprite.Sprite):     #CREACION DE CLASE PARA EL PERSONAJE
    def __init__(self):             #INICIALIZAR LA CLASE
        super().__init__()          #INICIALIZAR LA SUPER CLASE
        self.image = pygame.image.load("imagenes/imagenes/boton nv3.png").convert()  #AGREGANDO PERSONAJE, #COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
        self.image.set_colorkey(NEGRO) #CON ESTA FUNCION SE REMUEVE EL FONDO NEGRO DE LA IMAGEN
        self.rect = self.image.get_rect()  #OBTENER LA RECTA O CUADRO DEL SPRITE
        self.rect.centerx = W // 3.1     #PONERLO EN PANTALLA
        self.rect.bottom = H -50       #PONERLO EN PANTALLA
        self.speed_x = 0                #MODIFICAR LA VELOCIDAD DEL PERSONAJE
        self.shield = 100               #MODIFICAR LA VIDA DEL PERSONAJE



all_sprites = pygame.sprite.Group()


tuerca = Tuerca()     
all_sprites.add(tuerca)

boton1 = Boton1()
all_sprites.add(boton1)

boton2 = Boton2()
all_sprites.add(boton2)

boton3 = Boton3()
all_sprites.add(boton3)


#----------------------------------TEXTO-------------------------------------------------------------

def pintar_boton(PANTALLA ,boton, palabra):
    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(PANTALLA,(83,212,254,255), boton, 0) 
    else:
        
        pygame.draw.rect(PANTALLA, (83,212,254,255), boton, 0)

    texto = font.render(palabra, True, (NEGRO)) 
    PANTALLA.blit(texto, (boton.x +(boton.width-texto.get_width())/2,
                        boton.y +(boton.height-texto.get_height())/2))


def Pvolumen():     #FUNCION NIVEL 2
    PANTALLA.blit(volumen, [0,0])        #SE INGRESA IMAGEN
    pygame.display.flip()
    waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
    while waiting:          #MIENTRAS SE ESPERA
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                if boton_quitar_vol.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    pygame.mixer.music.set_volume(0.0)     #MODIFICADOR DE VOLUMEN DE MUSICA DEL JUEGO
                if boton_poner_vol.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    pygame.mixer.music.set_volume(0.5)     #MODIFICADOR DE VOLUMEN DE MUSICA DEL JUEGO              
            if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                if event.key == pygame.K_SPACE:
                    sonido_boton.play()
                    waiting = False  # SE DEJA DE ESPERAR

        pintar_boton(PANTALLA, boton_quitar_vol, "Volumen")
        pintar_boton(PANTALLA, boton_poner_vol, "Volumen")

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


def idioma():     #FUNCION NIVEL 2
    PANTALLA.blit(pantalla_idioma, [0,0])        #SE INGRESA IMAGEN
    pygame.display.flip()
    waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
    while waiting:          #MIENTRAS SE ESPERA
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                if boton_español.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    menuesp()
            if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                if event.key == pygame.K_SPACE:
                    sonido_boton.play()
                    waiting = False  # SE DEJA DE ESPERAR

        pintar_boton(PANTALLA, boton_español, "Volumen")
            


def show_game_over_screen():     #FUNCION PANTALLA GAME OVER
    PANTALLA.blit(pantalla_botones, [0,0])          #SE INGRESA IMAGEN
    pygame.display.flip()
    waiting = True         #SE COMIENZA A ESPERAR
    while waiting:         #MIENTRAS SE ESPERA
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                if boton_volumen.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    Pvolumen()
                if boton_idioma.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    idioma()
            if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                if event.key == pygame.K_SPACE:
                    sonido_boton.play()
                    waiting =  False  # SE DEJA DE ESPERAR

        pintar_boton(PANTALLA, boton_volumen, "Volumen")
        pintar_boton(PANTALLA, boton_idioma, "Volumen")


def menu1():     #FUNCION NIVEL 2
    inicio()
    PANTALLA.blit(niveles, [0,0])        #SE INGRESA IMAGEN
    pygame.display.flip()
    waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
    while waiting:          #MIENTRAS SE ESPERA
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                if boton_nivel_1.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    nivel1()
                if boton_nivel_2.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    nivel2()
                if boton_nivel_3.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    nivel3()
                if boton_opciones.collidepoint(pygame.mouse.get_pos()):
                    sonido_boton.play()
                    show_game_over_screen()

        pintar_boton(PANTALLA, boton_nivel_1, "Nivel 1")
        pintar_boton(PANTALLA,boton_nivel_2,"Nivel 2")
        pintar_boton(PANTALLA,boton_nivel_3,"Nivel 3")
        pintar_boton(PANTALLA,boton_opciones,"")

        if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
            if event.key == pygame.K_SPACE:
                waiting = False  # SE DEJA DE ESPERAR

def menu():
    PANTALLA.blit(niveles, [0,0])
    for event in pygame.event.get():  #EVENTO PARA SALIR DE LA VENTANA
        if event.type == pygame.QUIT: sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button==1:
            if boton_nivel_1.collidepoint(pygame.mouse.get_pos()):
                sonido_boton.play()
                nivel1()
            if boton_nivel_2.collidepoint(pygame.mouse.get_pos()):
                sonido_boton.play()
                nivel2()
            if boton_nivel_3.collidepoint(pygame.mouse.get_pos()):
                sonido_boton.play()
                nivel3()
            if boton_opciones.collidepoint(pygame.mouse.get_pos()):
                sonido_boton.play()
                show_game_over_screen()

    pintar_boton(PANTALLA, boton_nivel_1, "Nivel 1")
    pintar_boton(PANTALLA,boton_nivel_2,"Nivel 2")
    pintar_boton(PANTALLA,boton_nivel_3,"Nivel 3")
    pintar_boton(PANTALLA,boton_opciones,"")

#GAME OVER
game_over = True
score = 0
#BUCLE PRINCIPAL
running = True  
nivel_dos = True
while running:
    menu()

    clock.tick(60) #60 FPS
    all_sprites.draw(PANTALLA)

    pygame.display.flip()
pygame.QUIT


