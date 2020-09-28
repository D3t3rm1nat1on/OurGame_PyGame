import pygame, sys
from pygame import font

''' окно '''

window = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Welcom to the club, buddy')
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()
bg = pygame.image.load("background.jpg")

while True:
    clock.tick(60)
    window.blit(bg, (0, 0))
    start_button = pygame.draw.rect(window, (255, 20, 147), (150, 90, 500, 50));
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    text = myfont.render('Start game', False, (0, 0, 0))
    window.blit(text, (300, 90))
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 <= x <= 650 and 90 <= y <= 140:
                import src.main as g
                game = g.GameWindow()
                game.run()
                sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
