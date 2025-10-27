import pygame
import sys
import os
from components.draw_button import Button
from ui.settings.setting import setting_screens
import config  

pygame.init()

# Đặt cửa sổ giữa màn hình
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Main Menu")

font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

def update_buttons():
    w, h = config.WIDTH, config.HEIGHT
    start_btn = Button(w // 2 - 100, h // 2 - 30, 200, 60, "Start Game", font)
    setting_btn = Button(w // 2 - 100, h // 2 + 50, 200, 60, "Settings", font)
    quit_btn = Button(w // 2 - 100, h // 2 + 130, 200, 60, "Quit", font)
    return start_btn, setting_btn, quit_btn

start_button, setting_button, quit_button = update_buttons()
running = True

while running:
    screen.fill(config.BG_COLOR)

    # Vẽ các nút
    start_button.draw(screen)
    setting_button.draw(screen)
    quit_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if start_button.is_clicked(event):
            print("Start Game clicked!")

        if setting_button.is_clicked(event):
            new_screen = setting_screens(screen, font)
            # Sau khi trở lại, cập nhật lại màn hình và nút
            screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
            start_button, setting_button, quit_button = update_buttons()

        if quit_button.is_clicked(event):
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
sys.exit()
