import pygame
import pygame.gfxdraw

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
pygame.draw.line(screen,((0,0,255)), (100,100), (100,180),5)
pygame.draw.circle(screen,((0,0,255)), (100,85), 20,5)
pygame.draw.line(screen,((0,0,255)), (100,110), (60,150),5)
pygame.draw.line(screen,((0,0,255)), (100,110), (150,150),5)
pygame.draw.line(screen,((0,0,255)), (100,180), (60,220),5)
pygame.draw.line(screen,((0,0,255)), (100,180), (150,220),5)

while running:
    # to show our window constantly

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()