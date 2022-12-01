import pygame, random, sys
from pygame import *
from mainesp import menuesp

def nivel2():

    #Pantalla - ventana
    W, H = 700, 400           #VALORES PARA EL TAMAÑO DE LA VENTANA 
    #COLORES
    BLANCO = (255,255,255)
    NEGRO = (0,0,0)
    ROJO = (255,0,0)
    AZUL = (0,0,255)
    VERDE = (0,255,0)

    pygame.init()   #INICIALIZAR PYGAME
    pygame.mixer.init()     # INICIALIZAR EL SONIDO
    PANTALLA = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Arky(Medes)")           # NOMBRE DE LA PANTALLA EN DONDE SE MUESTRA EL JUEGO
    icono=pygame.image.load("imagenes/imagenes/arky.png")    # ICONO DE LA PANTALLA DONDE SE MUESTRA EL JUEGO
    pygame.display.set_icon(icono)
    clock= pygame.time.Clock()  #CONTROLAR LA CANTIDAD DE FPS DEL JUEGO

    #-----------------------------------FUNCIONES-------------------------------------------------------

    #----------------------------------TEXTO-------------------------------------------------------------
    def draw_text(surface, text, size, x, y): #FUNCION PARA DIBUJAR TEXTO EN LA PANTALLA
        font = pygame.font.SysFont("serif", size)  #SELECCIONAR UNA FUENTE
        text_surface = font.render(text, True, NEGRO) # RENDERIZAR Y SELECCIONAR EL COLOR DEL TEXTO
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)     #MODIFICAR LA POSICION DEL TEXTO
        surface.blit(text_surface, text_rect)     #PINTAR EL TEXTO

    #--------------------------BARRA DE VIDA-------------------------------------------------------------
    def draw_health_bar(surface, x, y, porcentaje):  #FUNCION BARRA DE VIDA
        BAR_LENGHT = 150     #LARGO DE LA BARRA DE VIDA
        BAR_HEIGHT = 10     #ALTURA DE LA BARRA DE VIDA
        fill = (porcentaje / 100) * BAR_LENGHT        #
        border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
        fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surface, AZUL, fill)  #COLOR DE LA BARRA DE VIDA
        pygame.draw.rect(surface, BLANCO, border, 2)       #BORDE DE LA BARRA DE VIDA Y COLOR


    #-------------------------PERSONAJE---------------------------------------------------------------
    class Personaje(pygame.sprite.Sprite):     #CREACION DE CLASE PARA EL PERSONAJE
        def __init__(self):             #INICIALIZAR LA CLASE
            super().__init__()          #INICIALIZAR LA SUPER CLASE
            self.moving_animationRight = False
            self.moving_animationLeft = False

            self.spritesRight = []
            self.spritesLeft = []

            self.spritesRight.append(pygame.image.load("animaciones3/arky_baston1.png").convert())  # MOVIMIENTO DERECHA; COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
            self.spritesRight.append(pygame.image.load("animaciones3/arky_baston2.png").convert())
            self.spritesRight.append(pygame.image.load("animaciones3/arky_baston3.png").convert())
            self.spritesRight.append(pygame.image.load("animaciones3/arky_baston4.png").convert())
            self.spritesRight.append(pygame.image.load("animaciones3/arky_baston5.png").convert())

            self.spritesLeft.append(pygame.image.load("animaciones3/arky_bastonL1.png").convert())  # MOVIMIENTO IZQUIERDA; COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
            self.spritesLeft.append(pygame.image.load("animaciones3/arky_bastonL2.png").convert())
            self.spritesLeft.append(pygame.image.load("animaciones3/arky_bastonL3.png").convert())
            self.spritesLeft.append(pygame.image.load("animaciones3/arky_bastonL4.png").convert())
            self.spritesLeft.append(pygame.image.load("animaciones3/arky_bastonL5.png").convert())

            self.current_spriteRight = 0 #UBICAR EN QUÉ SPRITE SE ENCUENTRA ACTUALMENTE
            self.image = self.spritesRight[self.current_spriteRight]
            self.current_spriteLeft = 0
            self.imageLeft = self.spritesLeft[self.current_spriteLeft]
            
            
            self.rect = self.image.get_rect()  #OBTENER LA RECTA O CUADRO DEL SPRITE
            self.rectLeft = self.imageLeft.get_rect()

            self.rect.centerx = 700 // 2     #PONERLO EN PANTALLA
            self.rect.bottom = 400 - 10        #PONERLO EN PANTALLA
            self.speed_x = 0                #MODIFICAR LA VELOCIDAD DEL PERSONAJE
            self.shield = 100               #MODIFICAR LA VIDA DEL PERSONAJE

            
        def movingRight(self):
            self.moving_animationRight = True

        def movingLeft(self):
            self.moving_animationLeft = True

        def update(self):
            
            self.speed_x = 0
            
            if self.moving_animationRight == True:
                self.current_spriteRight += 0.25
                if int(self.current_spriteRight) >= len(self.spritesRight):
                    self.current_spriteRight = 0
                    self.moving_animationRight = False
            if self.moving_animationLeft == True:
                self.current_spriteLeft += 0.25
                if int(self.current_spriteLeft) >= len(self.spritesLeft):
                    self.current_spriteLeft = 0
                    self.moving_animationLeft = False
            
            if self.moving_animationRight == True:
                self.image = self.spritesRight[int(self.current_spriteRight)]
                
            if self.moving_animationLeft == True:
                self.image = self.spritesLeft[int(self.current_spriteLeft)]

            self.image.set_colorkey((NEGRO))
            self.imageLeft.set_colorkey((NEGRO))
            keystate = pygame.key.get_pressed()  #COMADO GET_PRESSED SIRVE PARA PODER DEJAR PRESIONADA UNA LETRA

            if keystate[pygame.K_LEFT]:          #SELECCION DE TECLA PARA MOVER A LA IZQUIERDA
                self.speed_x = -5         #VELOCIDAD PERSONAJE
                self.movingLeft()
            if keystate[pygame.K_RIGHT]:         #SELECCION DE TECLA PARA MOVER A LA DERECHA
                self.speed_x = 5          #VELOCIDAD PERSONAJE
                self.movingRight()
            
            self.rect.x += self.speed_x    
            if self.rect.right > 700:        # FUNCION PARA QUE EL PERSONAJE NO SE SALGA D ELA PANTALLA
                self.rect.right = 700        # SI EL LADO DERECHO DE MI PERSONAJE ES MAYOR A W SE IGUALA A W PARA QUE YA NO PUEDA SEGUIR MAS
            if self.rect.left < 0:         # SI EL LADO IZQUIERDO DE MI PERSONAJE ES MEMNOR A CERO SE IGUALA A CERO PARA QUE NO PUEDA SEGUIR MAS
                self.rect.left = 0

    #----------------------------ITEMS--------------------------------------------------------------------------------
    class Libros(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = random.choice(libros_imagenes)  #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
            self.image.set_colorkey(VERDE)               #QUITA EL FONDO NEGRO DE LA IMAGEN
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
            self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
            self.speedy = random.randrange(1,4)  # VELOCIDAD ALEATORIA DE LOS ITEMS

        def update(self):
            self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
            if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
                    self.rect.x = random.randrange(W - self.rect.width) 
                    self.rect.y = random.randrange(-100, -40)    
                    self.speedy = random.randrange(1,4)

    class Control(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = random.choice(control_imagenes)     #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
            self.image.set_colorkey(NEGRO)          #QUITA EL FONDO NEGRO DE LA IMAGEN
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
            self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
            self.speedy = random.randrange(2,5)  # VELOCIDAD ALEATORIA DE LOS ITEMS

        def update(self):
            self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
            if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
                    self.rect.x = random.randrange(W - self.rect.width) 
                    self.rect.y = random.randrange(-100, -40)    
                    self.speedy = random.randrange(2,5)

    class Items_especiales(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = random.choice(items_especiales)  #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
            self.image.set_colorkey(BLANCO)               #QUITA EL FONDO NEGRO DE LA IMAGEN
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
            self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
            self.speedy = random.randrange(1,2)  # VELOCIDAD ALEATORIA DE LOS ITEMS

        def update(self):
            self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
              #  if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
               #         self.rect.x = random.randrange(W - self.rect.width) 
                #        self.rect.y = random.randrange(-100, -40)    
                 #       self.speedy = random.randrange(1,3)


    def rules():  #FUNCION PARA INGRESAR IMAGEN
        PANTALLA.blit(instrucciones, [0,0])        #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True       #SE COMIENZA A ESPERAR
        while waiting:       #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MEMNU
                        waiting = False  # SE DEJA DE ESPERAR


    def show_game_over_screen():     #FUNCION PANTALLA GAME OVER
        PANTALLA.blit(go, [0,0])          #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True         #SE COMIENZA A ESPERAR
        while waiting:         #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                    if event.key == pygame.K_SPACE:
                        waiting = False  # SE DEJA DE ESPERAR

    font = pygame.font.SysFont("serif", 30)  #SELECCIONAR UNA FUENTE
    def pintar_boton(PANTALLA ,boton, palabra):
        if boton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(PANTALLA,(83,212,254,255), boton, 0) 
        else:
            
            pygame.draw.rect(PANTALLA, (83,212,254,255), boton, 0)

        texto = font.render(palabra, True, (NEGRO)) 
        PANTALLA.blit(texto, (boton.x +(boton.width-texto.get_width())/2,
                            boton.y +(boton.height-texto.get_height())/2))


    boton_menu = pygame.Rect(550,290,140,50)
    boton_exit = pygame.Rect(50,320,80,50)

    def gover():     #FUNCION NIVEL 2
        PANTALLA.blit(gonv2, [0,0])        #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
        while waiting:          #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button==1:
                    if boton_menu.collidepoint(pygame.mouse.get_pos()):
                        from main import menu
                    if boton_exit.collidepoint(pygame.mouse.get_pos()):
                        exit()
        
            pintar_boton(PANTALLA, boton_menu, "Volumen")
            pintar_boton(PANTALLA, boton_exit, "Volumen")


    def nivel_2():     #FUNCION NIVEL 2
        PANTALLA.blit(intro_nivel_2, [0,0])        #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
        while waiting:          #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                    if event.key == pygame.K_SPACE:
                        waiting = False  # SE DEJA DE ESPERAR

    def factos1():     #FUNCION NIVEL 2
        PANTALLA.blit(fact1, [0,0])        #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
        while waiting:          #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                    if event.key == pygame.K_SPACE:
                        waiting = False  # SE DEJA DE ESPERAR

    def factos2():     #FUNCION NIVEL 2
        PANTALLA.blit(fact2, [0,0])        #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
        while waiting:          #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                    if event.key == pygame.K_SPACE:
                        waiting = False  # SE DEJA DE ESPERAR
    
    def factos3():     #FUNCION NIVEL 2
        PANTALLA.blit(fact3, [0,0])        #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True          #MIENTRAS SE COMIENZA A ESPERAR
        while waiting:          #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                    if event.key == pygame.K_SPACE:
                        waiting = False  # SE DEJA DE ESPERAR
        

    def gana():         #FUNCION GANA
        PANTALLA.blit(pantalla_gana, [0,0])      #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True            #SE COMIENZA A ESPERAR
        while waiting:            #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                    if event.key == pygame.K_SPACE:
                        waiting = False  # SE DEJA DE ESPERAR


    def final():       #FUNCION IMAEN FINAL
        PANTALLA.blit(pantalla_final, [0,0])       #SE INGRESA IMAGEN
        pygame.display.flip()
        waiting = True      #SE ESPERA
        while waiting:      #MIENTRAS SE ESPERA
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                    if event.key == pygame.K_SPACE:
                        waiting = False  # SE DEJA DE ESPERAR
                        while running:
                            running = False     #SE DEJA DE CORRER EL JUEGO





    libros_imagenes = []       #CREAMOS UNA LISTA CON TODOS LOS ITEMS PARA DESPUES ASIGANRLO A LA VARIABLE DE LIBROS_IMAGENES
    libros_list = ["imagenes/imagenes/lapiz.png", "imagenes/imagenes/regla.png"]

    for img in libros_list:
        libros_imagenes.append(pygame.image.load(img).convert())  #PROCESO PARA ASIGNAR LA VARIABLE CON LAS IMAGENES A LA NUEVA VARIABLE

    control_imagenes = []     #CREAMOS UNA LISTA CON TODOS LOS ITEMS PARA DESPUES ASIGANRLO A LA VARIABLE DE CONTROL_IMAGENES
    control_list = ["imagenes/imagenes/fb.png", "imagenes/imagenes/cel.png", "imagenes/imagenes/instagram.png"]

    for img in control_list:
        control_imagenes.append(pygame.image.load(img).convert())

    items_especiales = []     #CREAMOS UNA LISTA CON TODOS LOS ITEMS PARA DESPUES ASIGANRLO A LA VARIABLE DE CONTROL_IMAGENES
    items_especiales_list = ["imagenes/imagenes/calculadora_esp.png"]

    for img in items_especiales_list:
        items_especiales.append(pygame.image.load(img).convert())
    
    items_especiales2 = []     #CREAMOS UNA LISTA CON TODOS LOS ITEMS PARA DESPUES ASIGANRLO A LA VARIABLE DE CONTROL_IMAGENES
    items_especiales_list2 = ["imagenes/imagenes/calculadora_esp.png"]

    for img in items_especiales_list2:
        items_especiales2.append(pygame.image.load(img).convert())

    items_especiales3 = []     #CREAMOS UNA LISTA CON TODOS LOS ITEMS PARA DESPUES ASIGANRLO A LA VARIABLE DE CONTROL_IMAGENES
    items_especiales_list3 = ["imagenes/imagenes/calculadora_esp.png"]

    for img in items_especiales_list3:
        items_especiales3.append(pygame.image.load(img).convert())


    # IMAGENES DE FONDO
    fondo = pygame.image.load("imagenes/imagenes/nuevo fondo.jpeg").convert()
    go = pygame.image.load("imagenes/imagenes/fondo 1.png").convert()
    instrucciones = pygame.image.load("imagenes/imagenes/instrucciones2.png").convert()
    pantalla_final = pygame.image.load("imagenes/imagenes/pantalla final.png").convert()
    intro_nivel_2 = pygame.image.load("imagenes/imagenes/intro ronda 2 lv2.png").convert()
    pantalla_gana = pygame.image.load("imagenes/imagenes/ganador2.png").convert()
    fondo2 = pygame.image.load("imagenes/imagenes/nivel2.jpeg").convert()
    fact1 = pygame.image.load("imagenes/imagenes/fact1lv2.png").convert()
    fact2 = pygame.image.load("imagenes/imagenes/fact2lv2.png").convert()
    fact3 = pygame.image.load("imagenes/imagenes/fact3lv2.png").convert()
    gonv2 = pygame.image.load("imagenes/imagenes/go nv2.png").convert()

    #SONIDOS
    sonido_libro = pygame.mixer.Sound("sonidolibro.mp3")
    sonido_has_perdido = pygame.mixer.Sound("sonidohasperdido.mp3") 

    #MUSICA JUEGO
    pygame.mixer.music.load("sonidojuego.mp3")
    pygame.mixer.music.set_volume(0.2)     #MODIFICADOR DE VOLUMEN DE MUSICA DEL JUEGO

    #Grupo de sprites
    all_sprites = pygame.sprite.Group()
    libro_list = pygame.sprite.Group()
    control_list = pygame.sprite.Group()
    items_especiales_list = pygame.sprite.Group()

    #MUSICA JUEGO
    pygame.mixer.music.play(loops=-1)  #HACER QUE SE ESCUCHE LA MUSICA DEL JUEGO Y QUE ENTRE EN UN LOOP

    #GAME OVER
    game_over = True
    #BUCLE PRINCIPAL
    running = True
    while running:
        if game_over:

            rules()

            game_over = False 
            all_sprites = pygame.sprite.Group()
            libro_list = pygame.sprite.Group()
            control_list = pygame.sprite.Group()
            items_especiales_list = pygame.sprite.Group()
            items_especiales_list2 = pygame.sprite.Group()
            items_especiales_list3 = pygame.sprite.Group()

            personaje = Personaje()     
            all_sprites.add(personaje)

            for i in range(5):
                libro = Libros()
                all_sprites.add(libro)
                libro_list.add(libro)

            for i in range(7):
                control = Control()
                all_sprites.add(control)
                control_list.add(control)

            score = 0

        clock.tick(60) #60 FPS
        for event in pygame.event.get():  #EVENTO PARA SALIR DE LA VENTANA
            if event.type == pygame.QUIT:
                running = False
        
        all_sprites.update()

        #COLISIONES
        daño = pygame.sprite.spritecollide(personaje, control_list, True)  #AL TENER UN TRUE SIGNIFICA QUE CUANDO EL PERSONAJE HAGA UNA COLISION CON UN OBJETO ESTE DESAPARECERA
        for daño in daño:
            control = Control()
            all_sprites.add(control)
            control_list.add(control)
            personaje.shield -=25   # MODIFICADOR DE VIDA, #CADA VEZ QUE CHOQUE CON EL ITEMM SE LE RESTAAR 25 
            sonido_has_perdido.play()
            if personaje.shield <= 0:  #SI LA VIDA ES MENOR O IGUAL A CERO TE LLEVA AL GAME OVER
                sonido_has_perdido.play()
                gover()
            
        #punto_especial = pygame.sprite.spritecollide(personaje, items_especiales_list, True)
        punto = pygame.sprite.spritecollide(personaje, libro_list, True)
        punto_especial = pygame.sprite.spritecollide(personaje, items_especiales_list, True)
        punto_especial2 = pygame.sprite.spritecollide(personaje, items_especiales_list2, True)
        punto_especial3 = pygame.sprite.spritecollide(personaje, items_especiales_list3, True)
        if punto_especial:
                factos1()
                score +=4
                sonido_libro.play()
                libro_especial = Items_especiales()
                items_especiales_list.add(libro_especial)

        if punto_especial2:
                factos2()
                score +=4
                sonido_libro.play()
                libro_especial2 = Items_especiales()
                items_especiales_list2.add(libro_especial2)

        if punto_especial3:
                factos3()
                score +=4
                sonido_libro.play()
                libro_especial3 = Items_especiales()
                items_especiales_list3.add(libro_especial3)

        if punto:
            score += 1     #CADA VEZ QUE HAGA COLISIONCON EL OBJETO ESTE  SUMMARA 1  AL PUNTAJE
            sonido_libro.play()
            libro = Libros()
            all_sprites.add(libro)
            libro_list.add(libro)
            if score == 12:
                for i in range(1): #NUMERO DE LIBROS QUE VAN A CAER
                    libro_especial = Items_especiales()
                    all_sprites.add(libro_especial)
                    items_especiales_list.add(libro_especial)
            if score == 25:
                for i in range(1): #NUMERO DE LIBROS QUE VAN A CAER
                     libro_especial2 = Items_especiales()
                     all_sprites.add(libro_especial2)
                     items_especiales_list2.add(libro_especial2)
                nivel_2()
                PANTALLA.blit(go, [0,0])
                class Personaje(pygame.sprite.Sprite):     #CREACION DE CLASE PARA EL PERSONAJE
                    def __init__(self):             #INICIALIZAR LA CLASE
                        super().__init__()          #INICIALIZAR LA SUPER CLASE
                        self.image = pygame.image.load("imagenes/imagenes/grad.png").convert()  #AGREGANDO PERSONAJE, #COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
                        self.image.set_colorkey(BLANCO) #CON ESTA FUNCION SE REMUEVE EL FONDO NEGRO DE LA IMAGEN
                        self.rect = self.image.get_rect()  #OBTENER LA RECTA O CUADRO DEL SPRITE
                        self.rect.centerx = W // 2     #PONERLO EN PANTALLA
                        self.rect.bottom = H -10        #PONERLO EN PANTALLA
                        self.speed_x = 0                #MODIFICAR LA VELOCIDAD DEL PERSONAJE
                        self.shield = 100               #MODIFICAR LA VIDA DEL PERSONAJE

                def update(self):
                        self.speed_x = 0
                        keystate = pygame.key.get_pressed()  #COMADO GET_PRESSED SIRVE PARA PODER DEJAT PRESIONADA UNA LETRA
                        if keystate[pygame.K_LEFT]:          #SELECCION DE TECLA PARA MOVER A LA IZQUIERDA
                            self.speed_x = -10         #VELOCIDAD PERSONAJE
                        if keystate[pygame.K_RIGHT]:         #SELECCION DE TECLA PARA MOVER A LA DERECHA
                            self.speed_x = 10          #VELOCIDAD PERSONAJE
                        self.rect.x += self.speed_x    
                        if self.rect.right > W:        # FUNCION PARA QUE EL PERSONAJE NO SE SALGA D ELA PANTALLA
                            self.rect.right = W        # SI EL LADO DERECHO DE MI PERSONAJE ES MAYOR A W SE IGUALA A W PARA QUE YA NO PUEDA SEGUIR MAS
                        if self.rect.left < 0:         # SI EL LADO IZQUIERDO DE MI PERSONAJE ES MEMNOR A CERO SE IGUALA A CERO PARA QUE NO PUEDA SEGUIR MAS
                            self.rect.left = 0 

                class Libros(pygame.sprite.Sprite):
                    def __init__(self):
                        super().__init__()
                        self.image = random.choice(libros_imagenes)  #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
                        self.image.set_colorkey(BLANCO)               #QUITA EL FONDO NEGRO DE LA IMAGEN
                        self.rect = self.image.get_rect()
                        self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
                        self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
                        self.speedy = random.randrange(1,6)  # VELOCIDAD ALEATORIA DE LOS ITEMS

                    def update(self):
                        self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
                        if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
                            self.rect.x = random.randrange(W - self.rect.width) 
                            self.rect.y = random.randrange(-100, -40)    
                            self.speedy = random.randrange(1,6)

                class Control(pygame.sprite.Sprite):
                    def __init__(self):
                        super().__init__()
                        self.image = random.choice(control_imagenes)     #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
                        self.image.set_colorkey(NEGRO)          #QUITA EL FONDO NEGRO DE LA IMAGEN
                        self.rect = self.image.get_rect()
                        self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
                        self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
                        self.speedy = random.randrange(1,6)  # VELOCIDAD ALEATORIA DE LOS ITEMS

                    def update(self):
                     self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
                     if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
                        self.rect.x = random.randrange(W - self.rect.width) 
                        self.rect.y = random.randrange(-100, -40)    
                        self.speedy = random.randrange(1,6)
            if score ==40:
                for i in range(1): #NUMERO DE LIBROS QUE VAN A CAER
                    libro_especial3 = Items_especiales()
                    all_sprites.add(libro_especial3)
                    items_especiales_list3.add(libro_especial3)
            if score >= 50:
                gana()
                running = False
                from main import menu
        
        PANTALLA.blit(fondo2 , [0,0])  #SE INGRESA LA IMAGEN DE FONDO

        all_sprites.draw(PANTALLA)

        #CONTADOR| 
        draw_text(PANTALLA, str(score), 25, W / 1.8, 1)
        draw_text(PANTALLA, str("Tools"), 25, W / 2.1, 1)

        #BARRA DE SALUD
        draw_health_bar(PANTALLA, 5, 5, personaje.shield)

        pygame.display.flip()
    pygame.QUIT
