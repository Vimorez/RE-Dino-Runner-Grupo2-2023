import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)  # NOMBRE DEL JUEGO
        # ICONO DEL DINOSAURIO (DinoWallpaper.png)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))  # TAMAÑO DE LA PANTALLA
        self.clock = pygame.time.Clock()  # CONTROLA EL TIEMPO DENTRO DEL JUEGO
        self.playing = False  # INDICA EL ESTADO DEL JUEGO
        self.game_speed = 20  # VELOCIDAD DEL JUEGO
        self.x_pos_bg = 0  # POSICION PARA EL FONDO DE LA PANTALLA X
        self.y_pos_bg = 380  # POSICION PARA EL FONDO DE PANTALLA Y
        self.player = Dinosaur()

    def run(self):  # METODO QUE EJECUTA EL JUEGO
        # Game loop: events - update - draw
        self.playing = True  # YA ESTOY JUGANDO
        while self.playing:
            self.events()  # PROCESAR EVENTOS
            self.update()  # UPDATE DE LOS ESTADOS
            self.draw()  # DIBUJADO DE PANTALLA
        pygame.quit()  # SI SE SALE DEL WHILE

    def events(self):
        for event in pygame.event.get():  # CAPTURA TODOS LOS EVENTOS QUE LE PASARE EN EL JUEGO
            if event.type == pygame.QUIT:  # PARA QUE SE SALGA DEL BUCLE WHILE SI ES QUE SE SALE DEL WHILE EN DEF RUN
                self.playing = False  # NO ESTA JUGANDO

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

    def draw(self):  # DIBUJAR EN PANTALLA
        # 30 CUADROS POR SEGUNDO TICK ES LA UNIDAD DE UN SEGUNDO
        self.clock.tick(FPS)
        # LA PANTALLA(SCREEN) LA LLENO(FILL) CON EL COLOR 255 (BLANCO)
        self.screen.fill((255, 255, 255))
        self.draw_background()  # METODO QUE PERMITE DIBUJAR EL FONDO DE PANTALLA
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        # DEFINO EL ANCHO DE LA IMAGEN BG ➡︎(BG ES UNA CONSTANTE)
        image_width = BG.get_width()
        # NOS PERMITE DIBUJAR EN PYGAME (BLIT PERMITE DIBUJAR UNA IMAGEN DE LA PISTA) TENEMOS QUE DARLE LAS POSICIONES
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        # DIBUJAMOS LA MISMA IMAGEN FUERA DE LA PANTALLA
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
