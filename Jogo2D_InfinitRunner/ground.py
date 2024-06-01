import pygame

#Tamanho da Tela
WIDTH = 1200
HEIGHT = 600
GROUND_WIDTH = 2400
GROUND_HEIGHT = 30
GAME_SPEED = 10


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[1] = HEIGHT - GROUND_HEIGHT
        self.rect[0] = xpos

    def update(self, *args, **kwargs):
        self.rect[0] -= GAME_SPEED

