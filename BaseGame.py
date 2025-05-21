from shapely.geometry import Polygon, point
import pygame, time, random

pygame.init()


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLOR = (255, 255, 255)
DARCKGREEN = (0, 47, 31)
PURPPLE = (96, 11, 135)
WHITE = (0, 0, 0)

room = "Комната 1"

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tewer Face by Dovintc")
pygame.mouse.set_visible(False)

TextRoom = pygame.font.SysFont(None , 36)

scene = 1

Running = True
while Running:

    mp = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    
    #переключение 
    MousePol = [(mp[0], mp[1]), (mp[0] + 10, mp[1]), (mp[0] + 10, mp[1] + 15), (mp[0], mp[1] + 15)]
    tp_room1 = [(1120, 300), (1120, 500), (1170, 400)]
    tp_room2 = [(80, 300), (80, 500), (30, 400)]
 
    MousePol2 = Polygon(MousePol)
    Treugol_room1 = Polygon(tp_room1)
    Treugol_room2 = Polygon(tp_room2)

    text_Room_surface = TextRoom.render(room, True, BLACK)

    if scene == 1:
        screen.fill(PURPPLE)
        pygame.draw.polygon(screen, RED, tp_room1)
        pygame.draw.polygon(screen, COLOR, MousePol)
        if MousePol2.intersects(Treugol_room1) and event.type == pygame.MOUSEBUTTONDOWN:
            scene, room = 2, "Комната 2"

    if scene == 2:
        screen.fill(DARCKGREEN)
        pygame.draw.polygon(screen, BLUE, tp_room2)
        pygame.draw.polygon(screen, COLOR, MousePol)
        if MousePol2.intersects(Treugol_room2) and event.type == pygame.MOUSEBUTTONDOWN:
            scene, room = 1, "Комната 1"



    screen.blit(text_Room_surface, (10, 10))
    pygame.display.flip()