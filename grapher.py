import sys
import pygame
import datetime
import math

width = 500
height = 500

def f(x):
    return math.sin(x)


def main():
    screen = pygame.display.set_mode((width,height))
    running = True
    hS = 0
    vS = 0
    deltaX = 0
    deltaY = 0
    zoomX = 1
    zoomY = 1
    while running:
        hS = hS + deltaX
        vS = vS + deltaY
        screen.fill((0, 0, 0))
        for i in range(-100, 100):
            pygame.draw.line(screen, (255, 0, 0), (zoomX * i + hS, zoomY * f(i) + vS), ((zoomX * (i + 1) + hS, zoomY * f(i + 1) + vS)))
        pygame.display.flip()

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    deltaX = -1
                elif events.key == pygame.K_RIGHT:
                    deltaX = 1
                elif events.key == pygame.K_UP:
                    deltaY = -1
                elif events.key == pygame.K_DOWN:
                    deltaY = 1
                elif events.key == pygame.K_d:
                    if (zoomX != 8):
                        zoomX = zoomX * 2
                elif events.key == pygame.K_a:
                    if(zoomX != 1/8):
                        zoomX = zoomX / 2
                elif events.key == pygame.K_w:
                    if (zoomY != 8):
                        zoomY = zoomY * 2
                elif events.key == pygame.K_s:
                    if(zoomY != 1/8):
                        zoomY = zoomY / 2
            elif events.type == pygame.KEYUP:
                if events.key == pygame.K_LEFT:
                    deltaX = 0
                elif events.key == pygame.K_RIGHT:
                    deltaX = 0
                elif events.key == pygame.K_UP:
                    deltaY = 0
                elif events.key == pygame.K_DOWN:
                    deltaY = 0

main()