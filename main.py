import pygame
from math import pi
pygame.init()
size = [700, 400]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), [60, 250], 40)
    pygame.draw.circle(screen, (255, 0, 0), [180, 250], 40)
    pygame.draw.circle(screen, (0, 255, 0), [300, 250], 40)

    pygame.display.flip()
pygame.quit()
