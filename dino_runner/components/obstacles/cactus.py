import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, image):
        # elige una imagen aleatoria de la lista
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)  # super(). invoca un metodo de la clase padre
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

# EL PAJARO ESTA ANIMADO NO ES COMO LOS CACTUS (ESTATICO)


class Bird(Obstacle):  # HEREDA DE LA CLASE OBSTACLE
    def __init__(self, image):
        # SOLO TIENE UN TIPO Y ESTA ANIMADO (EL LOS CACTUS HAY 2 TIPOS SMALL Y LARGE)
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):  # HACEMOS UN METODO DRAW PORQUE EL METODO DRAW EN OBSTACLE SOLO FUNCIONA PARA LOS CACTUS
        if self.index >= 12:
            self.index = 0  # VOLVEMOS A PONER EL INDEX EN 0
        # DIVIDIMOS EL INDICE ACTUAL ENTRE 6
        screen.blit(self.image[self.index//6], self.rect)
        self.index += 1  # INCREMENTAMOS EL INDEX
