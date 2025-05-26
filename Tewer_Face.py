from shapely.geometry import Polygon, point
import pygame, time, random
from SETTINGS import *
    
Color_scene = (0, 0, 0)
Monster_choice = ("None", -1)

def ChoiceM(Color_scene, scene):
    global Monster_choice
    if Choice == True: 
        pygame.draw.rect(screen, WHITE, (1200, 50, 150, 100))

    if Choice != True:
        square_surfaceM = pygame.Surface((150, 50), pygame.SRCALPHA)
        square_surfaceM2 = pygame.Surface((150, 100), pygame.SRCALPHA)
        square_surfaceM.fill((255, 255, 255, 150))
        square_surfaceM2.fill((255, 255, 255, 150))
        screen.blit(square_surfaceM, (1200, 0))
        screen.blit(Monster_Text, (monster_text_x + 1200, monster_text_y ))   

    else: 
        pygame.draw.rect(screen, WHITE, (1200, 0, 150, 50))
        screen.blit(Monster_Text, (monster_text_x + 1200, monster_text_y )) 
        screen.blit(Monster_name_Text, (monster_name_text_x + 1200, monster_text_y + 50))
        screen.blit(Monster_name_Text2, (monster_name2_text_x + 1200, monster_text_y + 100))

    if MousePol2.intersects(Polygon([(1200, 0), (1350, 0), (1350, 50), (1200, 50)])) and not Choice: 
        screen.blit(square_surfaceM2, (1200, 50))
        screen.blit(Monster_name_Text, (monster_name_text_x + 1200, monster_text_y + 50))
        screen.blit(Monster_name_Text2, (monster_name2_text_x + 1200, monster_text_y + 100))
        pass

    if show_mouse: pygame.draw.polygon(screen, COLOR, MousePol)
    return Color_scene, scene

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load("addet\song\SongMenu.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tewer Face by Dovintc")
pygame.display.set_icon(pygame.image.load("addet\image\Tewer_Face_icon.png"))
pygame.mouse.set_visible(not show_mouse)

square_size_x = 550
square_size_y = 120
square_surface = pygame.Surface((square_size_x, square_size_y), pygame.SRCALPHA)

scene = 0
text_index = 0
current_text = texts[text_index]

fade_alpha = 0
fade_speed = 5
is_fading = False

Choice = False
Running = True
while Running:


    mp = pygame.mouse.get_pos()
    MousePol = [(mp[0], mp[1]), (mp[0] + 10, mp[1]), (mp[0] + 10, mp[1] + 15), (mp[0], mp[1] + 15)]
    text_Room_surface = Text.render(room, True, BLACK)
    MousePol2 = Polygon(MousePol)
    Treugol_Right = Polygon(Right)
    Treugol_left = Polygon(Left)
    BW = WIDTH / 5
    BH = HEIGHT / 3
    Button_Play = [BW, BH, BW * 3, BH]
    Button_Play_For_Poly = [(BW + 100, BH + 200), ((BW * 4) - 100, BH + 200), ((BW * 4) - 100, (BH * 2) + 50), (BW + 100, (BH * 2) + 50)]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        
        if MousePol2.intersects(Polygon([(1200, 0), (1350, 0), (1350, 50), (1200, 50)])) and event.type == pygame.MOUSEBUTTONDOWN:
            Choice = not Choice
            

        if scene == 0.5 and event.type == pygame.MOUSEBUTTONDOWN:
            text_index += 1
            if text_index < len(texts):
                current_text = texts[text_index]
                fade_alpha = 0 
                is_fading = True
            else:
                scene = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if scene == 1 and MousePol2.intersects(Treugol_Right):
                scene = 2
                if Language == "RU":
                    room = "Комната 2"
                elif Language == "EN":
                    room = "Home camera 2"
                sound.play()

            elif scene == 2 and MousePol2.intersects(Treugol_Right):
                scene = 3
                if Language == "RU":
                    room = "Комната 3"
                elif Language == "EN":
                    room = "Home camera 3"
                sound.play()

            elif scene == 3 and MousePol2.intersects(Treugol_left):
                scene = 2
                if Language == "RU":
                    room = "Комната 2"
                elif Language == "EN":
                    room = "Home camera 2"
                sound.play()

            elif scene == 3 and MousePol2.intersects(Treugol_Right):
                scene = 4
                if Language == "RU":
                    room = "Комната 4"
                elif Language == "EN":
                    room = "Home camera 4"
                sound.play()

            elif scene == 2 and MousePol2.intersects(Treugol_left):
                scene = 1
                if Language == "RU":
                    room = "Комната 1"
                elif Language == "EN":
                    room = "Home camera 1"
                sound.play()

            elif scene == 4 and MousePol2.intersects(Treugol_left):
                scene = 3
                if Language == "RU":
                    room = "Комната 3"
                elif Language == "EN":
                    room = "Home camera 3"
                sound.play()

            elif scene == 4 and MousePol2.intersects(Treugol_Right):
                scene = 5
                if Language == "RU":
                    room = "Комната 5"
                elif Language == "EN":
                    room = "Home camera 5"
                sound.play()

            elif scene == 5 and MousePol2.intersects(Treugol_left):
                scene = 4
                if Language == "RU":
                    room = "Комната 4"
                elif Language == "EN":
                    room = "Home camera 4"
                sound.play()

    print(scene)
    if background_loaded and song_loaded:
        screen.fill(BLACK)
        screen.blit(error_text_background, (text_x - x_not_found, text_y + 25))    
        screen.blit(error_text_song, (text_x - x_not_found, text_y - 25))
        if show_mouse: pygame.draw.polygon(screen, COLOR, MousePol)

    elif background_loaded:
        screen.fill(BLACK)
        screen.blit(error_text_background, (text_x - x_not_found, text_y))    
        if show_mouse: pygame.draw.polygon(screen, COLOR, MousePol)

    elif song_loaded:
        screen.fill(BLACK)
        screen.blit(error_text_song, (text_x - x_not_found, text_y))  
        if show_mouse: pygame.draw.polygon(screen, COLOR, MousePol)


    if scene == 0 and not background_loaded and not song_loaded:
        screen.blit(Background, (0, 0))
        pygame.draw.polygon(screen, DARCKBLUE, Button_Play_For_Poly)
        square_surface.fill((255, 255, 255, 70))  # Красный, 50% прозрачности
        screen.blit(square_surface, (440, 110))  # Рисуем наш прозрачный квадрат # Обновляем экран
        screen.blit(Start_Text, (620 - x_Start_Text, 490))
        screen.blit(Name_Text, (440, 100))
        screen.blit(Author_Text, (450, 190))
        if show_mouse: pygame.draw.polygon(screen, COLOR, MousePol)
        
        if MousePol2.intersects(Polygon(Button_Play_For_Poly)) and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.stop()
            scene = 0.5
            soundHorror.play()

    if scene == 0.5:
        screen.fill(BLACK)
        if show_mouse: pygame.draw.polygon(screen, COLOR, MousePol)
        
        if is_fading:
            fade_alpha += fade_speed / 10
            if fade_alpha >= 255:
                is_fading = False
                fade_alpha = 255
        else: fade_alpha = 255

        ME_Text = Text2.render(current_text, True, text_colors[text_index])
        ME_Text.set_alpha(fade_alpha)

        text_width, text_height = Text2.size(current_text)
        text_x = (WIDTH // 2) - (text_width // 2)
        text_y = (HEIGHT // 2) - (text_height // 2)

        screen.blit(ME_Text, (text_x, text_y))

    if scene == 1:
        screen.fill(PURPPLE)
        pygame.draw.polygon(screen, BLACK, Right)
        screen.blit(text_Room_surface, (10, 10))
        Color_scene, scene = ChoiceM(Color_scene, scene)
    elif scene == 2:
        screen.fill(DARCKGREEN)
        pygame.draw.polygon(screen, BLACK, Left)
        pygame.draw.polygon(screen, BLACK, Right)
        screen.blit(text_Room_surface, (10, 10))
        Color_scene, scene = ChoiceM(Color_scene, scene)
    elif scene == 3:
        screen.fill(DARK_YELLOW)
        pygame.draw.polygon(screen, BLACK, Left)
        pygame.draw.polygon(screen, BLACK, Right)
        screen.blit(text_Room_surface, (10, 10))
        Color_scene, scene = ChoiceM(Color_scene, scene)
    elif scene == 4:
        screen.fill(BLUE)
        pygame.draw.polygon(screen, BLACK, Left)
        pygame.draw.polygon(screen, BLACK, Right)
        screen.blit(text_Room_surface, (10, 10))
        Color_scene, scene = ChoiceM(Color_scene, scene)
    elif scene == 5:
        screen.fill(DARK_RED)
        pygame.draw.polygon(screen, BLACK, Left)
        screen.blit(text_Room_surface, (10, 10))
        Color_scene, scene = ChoiceM(Color_scene, scene)
    

    elif scene == -1:
       screen.fill(Color_scene)
       if show_mouse: pygame.draw.polygon(screen, COLOR, MousePol)



    pygame.display.flip()
pygame.quit()