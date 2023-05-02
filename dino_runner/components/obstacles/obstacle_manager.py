import pygame
import random
from dino_runner.components.obstacles.cactus import Bird, LargeCactus, Cactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:  # si la longitud de la lista esta vacia añadimos obstaculos
            if random.randint(0, 2) == 0:
                # agregamos un cactus tipo small
                # llama a la clase cactus
                self.obstacles.append(Cactus(SMALL_CACTUS))

            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))

            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:  # recorremos la lista de obstaculos para ver si algun obstaculo choco con el dinosaurio
            obstacle.update(game.game_speed, self.obstacles)
            # preguntamos si el dinosaurio colisiono con algun obstaculo de la lista obstaculo
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
