from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):

    # recibimos una imagen y un tipo para saber de que tipo sera el obstaculo
    def __init__(self, image, type):
        self.image = image
        self.type = type  # tipo de obstaculo
        # especificamos la imagen y de que tipo es
        # toda la informacion de la imagen
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH  # la imagen se pone al final

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed  # game_speed para recorrer las cosas
        if self.rect.x < -self.rect.width:  # preguntamos si el obstaculo salio de la pantalla
            obstacles.pop()  # sacamos el primer elemento de la lista con pop

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
