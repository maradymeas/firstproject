import pygame
size = (500, 400)
screen = pygame.display.set_mode(size)
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            col = (0,255, 255)
            pygame.draw.cirlce(
                screen, col, pos, 20, 5
            )
            pygame.display.update()