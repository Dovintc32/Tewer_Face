import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-0")

BACKGROUND_COLOR = (30, 30, 30)
RECT_COLOR = (255, 0, 0)
RECT_COLOR2 = (0, 255, 0)

# Позиция и размер
rect_x, rect_y = 100, 100
rect_width, rect_height = 50, 50
rect2_x, rect2_y = 650, 450

# Загружаем изображения
player1_img = pygame.image.load("T-0\\player1.png")
player2_img = pygame.image.load("T-0\\player2.png")

# Масштабируем
player1_img = pygame.transform.scale(player1_img, (rect_width, rect_height))
player2_img = pygame.transform.scale(player2_img, (rect_width, rect_height))

# Скорость
speed = 5
SHIFT_speed_pl1 = 0
SHIFT_speed_pl2 = 0

clock = pygame.time.Clock()
running = True
game_play = True

collision_sound = pygame.mixer.Sound("T-0\\collision.wav")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_play:
        # Управление
        SHIFT_speed_pl1 = 5 if keys[pygame.K_LSHIFT] else 0
        SHIFT_speed_pl2 = 5 if keys[pygame.K_RSHIFT] else 0

        if keys[pygame.K_a]: rect_x -= speed + SHIFT_speed_pl1
        if keys[pygame.K_d]: rect_x += speed + SHIFT_speed_pl1
        if keys[pygame.K_w]: rect_y -= speed + SHIFT_speed_pl1
        if keys[pygame.K_s]: rect_y += speed + SHIFT_speed_pl1

        if keys[pygame.K_LEFT]: rect2_x -= speed + SHIFT_speed_pl2
        if keys[pygame.K_RIGHT]: rect2_x += speed + SHIFT_speed_pl2
        if keys[pygame.K_UP]: rect2_y -= speed + SHIFT_speed_pl2
        if keys[pygame.K_DOWN]: rect2_y += speed + SHIFT_speed_pl2

        # Ограничение движения
        rect_x = max(0, min(rect_x, WIDTH - rect_width))
        rect_y = max(0, min(rect_y, HEIGHT - rect_height))
        rect2_x = max(0, min(rect2_x, WIDTH - rect_width))
        rect2_y = max(0, min(rect2_y, HEIGHT - rect_height))

        # Проверяем столкновение
        rect1 = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        rect2 = pygame.Rect(rect2_x, rect2_y, rect_width, rect_height)

        if rect1.colliderect(rect2):
            collision_sound.play()
            game_play = False

    # --- Отрисовка ---
    screen.fill(BACKGROUND_COLOR)

    if game_play:
        # Рисуем игроков
        screen.blit(player1_img, (rect_x, rect_y))
        screen.blit(player2_img, (rect2_x, rect2_y))
    else:
        # Рисуем экран Game Over
        game_over_font = pygame.font.SysFont(None, 72)
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        pygame.draw.rect(screen, (0, 255, 0), restart_button)
        font = pygame.font.SysFont(None, 36)
        screen.blit(font.render("Restart", True, (0, 0, 0)), (WIDTH // 2 - 50, HEIGHT // 2 + 60))

        # Клик мыши для рестарта
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if restart_button.collidepoint(mouse_pos):
                # Сброс переменных
                rect_x, rect_y = 100, 100
                rect2_x, rect2_y = 650, 450
                game_play = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()