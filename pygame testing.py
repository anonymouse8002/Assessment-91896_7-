import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("prototype 1")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
