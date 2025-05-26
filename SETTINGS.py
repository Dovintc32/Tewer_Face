import pygame
import random
from shapely.geometry import Polygon

pygame.init()

Language = "RU"
if Language == "RU":
    room = "Комната 1"
    texts = ["Почему ты здесь?", "Уходи, тут опасно!", "Будь осторожен...", "Я предупреждал!"]
    Start_Button = "Начать"
    x_Start_Text = 40
    File_Fone_notdetected = "Файл фона не найден"
    File_Song_notdetected = "Файл музыки не найден"
    x_not_found = 0
    Monster = "Монстры"
    Monster_name = "Монстр 1"
    Monster_name2 = "Монстр 2"
elif Language == "EN":
    room = "Home camera 1"
    texts = ["Why are you here?", "Go away, it's dangerous here!", "Be careful...", "I warned you!"]
    Start_Button = "Start"
    x_Start_Text = 0
    File_Fone_notdetected = "The background file was not found"
    File_Song_notdetected = "Music file not found"
    x_not_found = 150
    Monster = "no transfer"
    Monster_name = "no transfer"
    Monster_name2 = "no transfer"
WIDTH, HEIGHT = 1400, 800
WIDTH_monster, HEIGHT_monster = 150, 50

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLOR = (0, 0, 255)
DARCKGREEN = (0, 47, 31)
SMALLDARCKGREEN = (14, 102, 73)
PURPPLE = (96, 11, 135)
WHITE = (255, 255, 255)
DARCKBLUE = (17, 6, 87)
DARK_RED = (139, 0, 0)
GREY = (94, 94, 94)
DARK_YELLOW = (110, 99, 0)

Right = [(1320, 300), (1320, 500), (1370, 400)]
Left = [(80, 300), (80, 500), (30, 400)]

text_colors = [WHITE, DARK_RED, RED, RED]

Text = pygame.font.SysFont(r"addet\image\Bold.ttf" , 36)
Text2 = pygame.font.Font(r"addet\image\Bold.ttf", 56)
Text3 = pygame.font.Font(r"addet\image\Bold.ttf", 86)
Text4 = pygame.font.Font(r"addet\image\Bold.ttf", 27)
Text5 = pygame.font.Font(r"addet\image\Bold.ttf", 25)


Start_Text = Text2.render(Start_Button, True, SMALLDARCKGREEN)
Name_Text = Text3.render("Tewer Face", True, BLACK)
Author_Text = Text.render("by : Dovintc and Tooc1k R-2.1", True, BLACK)

error_text_background = Text2.render(File_Fone_notdetected, True, WHITE)
text_width_error_background, text_height_error_background = Text2.size(File_Fone_notdetected)
text_x = (WIDTH // 2) - (text_width_error_background // 2)
text_y = (HEIGHT // 2) - (text_height_error_background // 2)

error_text_song = Text2.render(File_Song_notdetected, True, WHITE)
text_width_error_song, text_height_error_song = Text2.size(File_Song_notdetected)
text_x = (WIDTH // 2) - (text_width_error_song // 2)
text_y = (HEIGHT // 2) - (text_height_error_song // 2)

Monster_Text = Text4.render(Monster, True, BLACK)
text_width_monster, text_height_monster = Text4.size(Monster)
monster_text_x = (WIDTH_monster // 2) - (text_width_monster // 2)
monster_text_y = (HEIGHT_monster // 2) - (text_height_monster // 2)

Monster_name_Text = Text5.render(Monster_name, True, BLACK)
text_width_monster, text_height_monster = Text4.size(Monster)
monster_name_text_x = (WIDTH_monster // 2) - (text_width_monster // 2)
monster_name_text_y = (HEIGHT_monster // 2) - (text_height_monster // 2)

Monster_name_Text2 = Text5.render(Monster_name2, True, BLACK)
text_width_monster, text_height_monster = Text4.size(Monster)
monster_name2_text_x = (WIDTH_monster // 2) - (text_width_monster // 2)
monster_name2_text_y = (HEIGHT_monster // 2) - (text_height_monster // 2)

try:
    Background = pygame.image.load("addet\image\BackGround.png")
    Background = pygame.transform.scale(Background, (1400, 800))
    background_loaded = False
except:
    background_loaded = True
try:
    sound = pygame.mixer.Sound("addet\song\ChangeCamera.mp3")
    soundHorror = pygame.mixer.Sound("addet\song\StartHorror.mp3")
    song_loaded = False
except:
    song_loaded = True

show_mouse = True

polygon_monster_text = [(1200, 50), (1350, 50), (1350, 100), (1200, 100)]
polygon2_monster_text = [(1200, 100), (1350, 100), (1350, 150), (1200, 150)]