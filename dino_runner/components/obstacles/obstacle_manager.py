import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus

from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:  # si la longitud de la lista esta vacia añadimos obstaculos
            aux = random.randint(0, 2)
            if aux == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))

            elif aux == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))

            elif aux == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:  # recorremos la lista de obstaculos para ver si algun obstaculo choco con el dinosaurio
            obstacle.update(game.game_speed, self.obstacles)
            # preguntamos si el dinosaurio colisiono con algun obstaculo de la lista obstaculo
            if game.player.dino_rect.colliderect(obstacle.rect):
                self.hit_sound = pygame.mixer.Sound(
                    '/Users/famozam/Documents/GitHub/RE-Dino-Runner-Grupo2-2023/dino_runner/assets/hit.wav')
                self.hit_sound.play()
                if not game.player.shield:

                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1
                    break
                else:

                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
