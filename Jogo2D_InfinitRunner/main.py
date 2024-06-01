import pygame
import player
from player import Player
from ground import Ground

WIDTH = 1200
HEIGHT = 600

pygame.init()
game_window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("INFINIT RUNNER JOGOS 2D")

# BackGround
BACKGROUND = pygame.image.load('data/background_03.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, [1200, 600])

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

#Grupo de Sprites
playerGroup = pygame.sprite.Group()
jogador = Player()
playerGroup.add(jogador)

groundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(WIDTH * i)
    groundGroup.add(ground)

gameLoop = True

#Funcoes de Desenho na tela e Update.
def draw():
    playerGroup.draw(game_window)
    groundGroup.draw(game_window)
def update():
    groundGroup.update()
    playerGroup.update()

clock = pygame.time.Clock()

while gameLoop:
    clock.tick(30)
    game_window.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False


    if is_off_screen(groundGroup.sprites()[0]):
        groundGroup.remove(groundGroup.sprites()[0])
        newGround = Ground(WIDTH - 20)
        groundGroup.add(newGround)

    #colisao com o Ground (Chao)
    if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
        player.SPEED = 0
    else:
        player.SPEED = 10

    update()
    draw()
    pygame.display.update()


