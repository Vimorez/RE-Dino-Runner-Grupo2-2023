import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    def __init__(self, image):
        # elige una imagen aleatoria de la lista
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)  # super(). invoca un metodo de la clase padre
        if image == SMALL_CACTUS:
            self.rect.y = 325
        elif image == LARGE_CACTUS:
            self.rect.y = 300
