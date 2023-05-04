import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):  # HEREDA DE LA CLASE OBSTACLE
    def __init__(self, image):

        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index >= 12:
            self.index = 0  # SE REINICIA LA ANIMACION
        # DIVIDIMOS EL INDICE ACTUAL ENTRE 6
        # DETERMINA LA VELOCIDAD DEL OBJETO
        screen.blit(self.image[self.index//6], self.rect)
        self.index += 1  # SE INCREMENTA EN 1 PARA QUE LA PROXIMA VEZ QUE SE LLAME AL  método draw(), se seleccione la siguiente imagen
