import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 800
scene = 1

color1 = (255, 0, 0)
color2 = (0, 255, 0)

color = color1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-1")

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    
        keys = pygame.key.get_pressed()
        if scene == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            if color == color1:
                color = color2
            else:
                color = color1
    
        screen.fill(color)
    pygame.display.flip()
pygame.quit()