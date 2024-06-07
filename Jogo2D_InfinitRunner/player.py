import pygame

GAME_SPEED = 10
SPEED = 10


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('data/Run__000.png').convert_alpha(),
                          pygame.image.load('data/Run__001.png').convert_alpha(),
                          pygame.image.load('data/Run__002.png').convert_alpha(),
                          pygame.image.load('data/Run__003.png').convert_alpha(),
                          pygame.image.load('data/Run__004.png').convert_alpha(),
                          pygame.image.load('data/Run__005.png').convert_alpha(),
                          pygame.image.load('data/Run__006.png').convert_alpha(),
                          pygame.image.load('data/Run__007.png').convert_alpha(),
                          pygame.image.load('data/Run__008.png').convert_alpha(),
                          pygame.image.load('data/Run__009.png').convert_alpha()
                          ]
        self.image = pygame.image.load('data/Run__000.png')
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.current_image = 0

    def update(self, *args, **kwargs):
        def move_player(self):

            # Movimentos eixo X
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.rect[0] += GAME_SPEED
            if key[pygame.K_a]:
                self.rect[0] -= GAME_SPEED

            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image, [100, 100])

        move_player(self)
        self.rect[1] += SPEED

        def fly(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.rect[1] -= 30
                self.image = pygame.image.load('data/Fly.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, [100, 100])
        fly(self)

        def fall(self):
            key = pygame.key.get_pressed()
            if not key[pygame.K_SPACE] and SPEED != 0:
                self.image = pygame.image.load('data/Fall.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, [100, 100])
        fall(self)

