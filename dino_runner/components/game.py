import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components import text_utils
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


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

        self.cloud = Cloud()

        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.running = True
        self.death_count = 0

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)
        self.game_speed = 20
        self.points = 0  # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True
        # Print a white background
        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        # Print menu elements
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()
        # create a menu event handler

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message(
                'Press any key to Start')
            self.screen.blit(text, text_rect)

        elif self.death_count > 0:
            text, text_rect = text_utils.get_centered_message(
                'Press any Key to Restart')
            score, score_rect = text_utils.get_centered_message('Your Score: ' + str(self.points),
                                                                height=half_screen_height + 50)
            death, death_rect = text_utils.get_centered_message('Death count: ' + str(self.death_count),
                                                                height=half_screen_height + 100)
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(death, death_rect)
        self.screen.blit(
            RUNNING[0], (half_screen_width - 20, half_screen_height - 140))

        # Tarea menu para despues de la muerte

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()
# se hizo un cambio en events

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        rect_left = pygame.Rect(0, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT)
        self.screen.fill((255, 192, 203), rect_left)  # ROSA

        rect_right = pygame.Rect(SCREEN_WIDTH // 2, 0,
                                 SCREEN_WIDTH // 2, SCREEN_HEIGHT)
        self.screen.fill((176, 224, 230), rect_right)  # CELESTE

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.update(game_speed=30)  # CAMBIO
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.score()
        self.clock.tick(FPS)

        self.draw_background()
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()

        pygame.display.flip()

    def draw_background(self):

        image_width = BG.get_width()
        BG.fill((55, 55, 55))  # AÑADI EL COLOR CAFE

        BG.fill((55, 55, 55))
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))

        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:

            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(str(self.points))
        self.player.check_invincibility(self.screen)
        self.screen.blit(text, text_rect)
