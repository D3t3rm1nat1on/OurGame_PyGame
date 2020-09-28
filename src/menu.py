import pygame, sys

''' окно '''

window = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Welcom to the club, buddy')
clock = pygame.time.Clock()
''' холст '''
screen = pygame.Surface((400, 400))

pygame.init()
bg = pygame.image.load("background.jpg")

while True:
    clock.tick(60)
    window.blit(bg, (0, 0))
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
