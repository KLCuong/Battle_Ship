import pygame
import sys
import config  # 🔹 Lấy thông số màn hình & màu nền từ file config.py
from components.draw_button import Button
from ui.settings.window_size import window_size_screen

def setting_screens(screen, font):
    clock = pygame.time.Clock()
    running = True

    # Lấy kích thước và màu nền từ config
    width, height = config.WIDTH, config.HEIGHT
    color_bg = config.BG_COLOR

    # Khởi tạo nút
    return_button = Button(width // 2 - 100, height // 2 + 50, 200, 60, "Return", font)
    window_size_button = Button(width // 2 - 100, height // 2 - 30, 200, 60, "Window Size", font)

    while running:
        # Nếu người dùng vừa thay đổi kích thước màn hình, cập nhật lại layout
        if (width != config.WIDTH) or (height != config.HEIGHT):
            width, height = config.WIDTH, config.HEIGHT
            screen = pygame.display.set_mode((width, height))
            return_button = Button(width // 2 - 100, height // 2 + 50, 200, 60, "Return", font)
            window_size_button = Button(width // 2 - 100, height // 2 - 30, 200, 60, "Window Size", font)

        screen.fill(color_bg)

        # Tiêu đề
        title_text = font.render("SETTINGS MENU", True, (0, 0, 100))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        # Vẽ nút
        return_button.draw(screen)
        window_size_button.draw(screen)

        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if window_size_button.is_clicked(event):
                window_size_screen(screen, font, width, height)
            if return_button.is_clicked(event):
                return  # Quay lại Main Menu

        pygame.display.flip()
        clock.tick(60)
