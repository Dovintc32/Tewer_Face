from shapely.geometry import Polygon, point
import pygame, time, random
from SETTINGS import *

pygame.init()
pygame.font.init()

room = "Комната 1"

pygame.mixer.init()

pygame.mixer.music.load("addet\song\SongMenu.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

Background = pygame.image.load("addet\image\BackGround.png")
Background = pygame.transform.scale(Background, (1400, 800))
sound = pygame.mixer.Sound("addet\song\ChangeCamera.mp3")
soundHorror = pygame.mixer.Sound("addet\song\StartHorror.mp3")

WIDTH, HEIGHT = 1400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tewer Face by Dovintc")
pygame.display.set_icon(pygame.image.load("addet\image\Tewer_Face_icon.png"))
pygame.mouse.set_visible(False)

square_size_x = 550
square_size_y = 120
square_surface = pygame.Surface((square_size_x, square_size_y), pygame.SRCALPHA)

scene = 0
# Переменные для сцены 0.5
texts = ["Почему ты здесь?", "Уходи, тут опасно!", "Будь осторожен..."]
text_index = 0
current_text = texts[text_index]

fade_alpha = 0
fade_speed = 5  # Скорость появления текста
is_fading = False

Running = True
while Running:

    mp = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

        # Обработка клика мыши в сцене 0.5
        if scene == 0.5 and event.type == pygame.MOUSEBUTTONDOWN:
            text_index += 1
            if text_index < len(texts):
                current_text = texts[text_index]
                fade_alpha = 0  # Сброс анимации
                is_fading = True
            else:
                scene = 1
            

    #переключение 
    MousePol = [(mp[0], mp[1]), (mp[0] + 10, mp[1]), (mp[0] + 10, mp[1] + 15), (mp[0], mp[1] + 15)]
    
    Right = [(1320, 300), (1320, 500), (1370, 400)]
    Left = [(80, 300), (80, 500), (30, 400)]
    text_Room_surface = Text.render(room, True, BLACK)
    MousePol2 = Polygon(MousePol)
    Treugol_Right = Polygon(Right)
    Treugol_left = Polygon(Left)
    BW = WIDTH / 5 # 240
    BH = HEIGHT / 3 # 266,6
    Button_Play = [BW, BH, BW * 3, BH]
    Button_Play_For_Poly = [(BW + 100, BH + 200), ((BW * 4) - 100, BH + 200), ((BW * 4) - 100, (BH * 2) + 50), (BW + 100, (BH * 2) + 50)]
    #Button_Play_Poly = Polygon(Button_Play)



    if scene == 0:
        
        screen.blit(Background, (0, 0))
        pygame.draw.polygon(screen, DARCKBLUE, Button_Play_For_Poly)
        square_surface.fill((255, 255, 255, 70))  # Красный, 50% прозрачности
        screen.blit(square_surface, (440, 110))  # Рисуем наш прозрачный квадрат # Обновляем экран
        screen.blit(Start_Text, (620, 490))
        screen.blit(Name_Text, (440, 100))
        screen.blit(Author_Text, (450, 190))
        pygame.draw.polygon(screen, COLOR, MousePol)
        
        if MousePol2.intersects(Polygon(Button_Play_For_Poly)) and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.stop()
            scene = 0.5
            soundHorror.play()

    if scene == 0.5:
        screen.fill(BLACK)
        pygame.draw.polygon(screen, COLOR, MousePol)

        # Если начался новый текст — запускаем анимацию
        if is_fading:
            fade_alpha += fade_speed / 10
            if fade_alpha >= 255:
                is_fading = False
                fade_alpha = 255
        else:
            fade_alpha = 255

        # Рендерим текст с прозрачностью
        ME_Text = Text2.render(current_text, True, text_colors[text_index])
        ME_Text.set_alpha(fade_alpha)

        # Центрируем текст
        text_width, text_height = Text2.size(current_text)
        text_x = (WIDTH // 2) - (text_width // 2)
        text_y = (HEIGHT // 2) - (text_height // 2)

        # Рисуем текст
        screen.blit(ME_Text, (text_x, text_y))

    if scene == 1:
        screen.fill(PURPPLE)
        pygame.draw.polygon(screen, RED, Right)
        pygame.draw.polygon(screen, COLOR, MousePol)
        screen.blit(text_Room_surface, (10, 10))
        if MousePol2.intersects(Treugol_Right) and event.type == pygame.MOUSEBUTTONDOWN:
            scene, room = 2, "Комната 2"
            sound.play()

    if scene == 2:
        screen.fill(DARCKGREEN)
        pygame.draw.polygon(screen, BLUE, Left)
        pygame.draw.polygon(screen, COLOR, MousePol)
        screen.blit(text_Room_surface, (10, 10))
        if MousePol2.intersects(Treugol_left) and event.type == pygame.MOUSEBUTTONDOWN:
            scene, room = 1, "Комната 1"
            sound.play()

    
    pygame.display.flip()