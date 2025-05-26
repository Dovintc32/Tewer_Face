import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Spawner")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MENU_COLOR = (100, 100, 100)

# Определение координат комнат
A_coords = [(0, 0), (100, 0), (100, 500), (0, 500)]
B_coords = [(100, 0), (200, 0), (200, 500), (100, 500)]
C_coords = [(200, 0), (300, 0), (300, 500), (200, 500)]
D_coords = [(300, 0), (400, 0), (400, 500), (300, 500)]
E_coords = [(400, 0), (500, 0), (500, 500), (400, 500)]

# Списки координат и цветов комнат
room_coords = [A_coords, B_coords, C_coords, D_coords, E_coords]
room_colors = [RED, YELLOW, CYAN, GREEN, BLUE]

# Данные о монстрах
MONSTER_NAMES = ["m1", "m2", "m3", "m4", "m5"]
MAX_MONSTERS = 3  # Максимум 3 монстра на экране
Active_Monster = []

# Переменные для таймера
start_time = time.time()
next_spawn_time = start_time + random.randint(2, 5)  # Уменьшено время спавна
running = True
game_over = False
restart_timer = None
MENU_RECT = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 50, 200, 100)

# Основной цикл
while running:
    current_time = time.time()
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Обработка кликов мыши
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            for monster in Active_Monster[:]:
                # Прямоугольник монстра
                rect_size = 60
                rect = pygame.Rect(
                    monster['center'][0] - rect_size//2,
                    monster['center'][1] - rect_size//2,
                    rect_size,
                    rect_size
                )
                if rect.collidepoint(mouse_pos):
                    Active_Monster.remove(monster)
        
        # Обработка клика по кнопке перезапуска
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if MENU_RECT.collidepoint(event.pos):
                # Сброс всех переменных
                Active_Monster = []
                next_spawn_time = time.time() + random.randint(2, 5)
                game_over = False
                restart_timer = None

    # Спавн новых монстров
    if current_time >= next_spawn_time and len(Active_Monster) < MAX_MONSTERS and not game_over:
        # Получаем занятые комнаты
        used_rooms = [m['room_index'] for m in Active_Monster]
        
        # Находим доступные комнаты
        available_rooms = [i for i in range(len(room_coords)) if i not in used_rooms]
        
        if available_rooms:
            room_index = random.choice(available_rooms)
            monster_name = random.choice(MONSTER_NAMES)
            
            # Вычисляем центр комнаты
            x_coords = [p[0] for p in room_coords[room_index]]
            y_coords = [p[1] for p in room_coords[room_index]]
            center_x = sum(x_coords) // len(x_coords)
            center_y = sum(y_coords) // len(y_coords)
            
            # Создаем монстра
            Active_Monster.append({
                'name': monster_name,
                'room_index': room_index,
                'center': (center_x, center_y),
                'color': (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            })
            
            # Следующий спавн через случайное время
            next_spawn_time = current_time + random.randint(2, 5)  # Уменьшено время спавна

    # Проверка условия завершения игры
    if len(Active_Monster) >= MAX_MONSTERS and not game_over:
        game_over = True
        restart_timer = current_time + 2  # Таймер на 2 секунды

    # Отрисовка
    screen.fill((0, 0, 0))
    
    # Рисуем комнаты
    for i in range(len(room_coords)):
        pygame.draw.polygon(screen, room_colors[i], room_coords[i])
    
    # Рисуем монстров
    for monster in Active_Monster:
        # Прямоугольник монстра
        rect_size = 60
        rect = pygame.Rect(
            monster['center'][0] - rect_size//2,
            monster['center'][1] - rect_size//2,
            rect_size,
            rect_size
        )
        pygame.draw.rect(screen, monster['color'], rect)
        
        # Текст с именем монстра
        font = pygame.font.Font(None, 24)
        text = font.render(monster['name'], True, WHITE)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # Отображение меню при завершении игры
    if game_over:
        if current_time >= restart_timer:
            # Рисуем меню
            pygame.draw.rect(screen, MENU_COLOR, MENU_RECT)
            font = pygame.font.Font(None, 36)
            text = font.render("Restart", True, WHITE)
            text_rect = text.get_rect(center=MENU_RECT.center)
            screen.blit(text, text_rect)
        else:
            # Отображение сообщения о завершении игры
            font = pygame.font.Font(None, 48)
            text = font.render("Game Over!", True, RED)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)

    # Обновляем экран
    pygame.display.flip()

# Выход из Pygame
pygame.quit()