import pygame

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLOR = (255, 255, 255)
DARCKGREEN = (0, 47, 31)
SMALLDARCKGREEN = (14, 102, 73)
PURPPLE = (96, 11, 135)
WHITE = (255, 255, 255)
DARCKBLUE = (17, 6, 87)

Text = pygame.font.SysFont("addet\image\Bold.ttf" , 36)
Text2 = pygame.font.Font("addet\image\Bold.ttf", 56)
Text3 = pygame.font.Font("addet\image\Bold.ttf", 86)

Start_Text = Text2.render("Start", True, SMALLDARCKGREEN)
Name_Text = Text3.render("Tewer Face", True, SMALLDARCKGREEN)
Author_Text = Text.render("by : Dovintc and Tooc1k R-1.0", True, PURPPLE)