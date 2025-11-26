import pygame
import os

class GameOverScreen:
    def __init__(self):
        assets = "Assets/images"

        # 게임오버 배경
        self.background = pygame.image.load(os.path.join(assets, "gameover.png"))
        self.background = pygame.transform.scale(self.background, (800, 600))

        # restart 버튼
        self.restart_img = pygame.image.load(os.path.join(assets, "restart.png"))
        self.restart_img = pygame.transform.scale(self.restart_img, (80, 80))

        # restart 버튼 위치
        self.restart_rect = self.restart_img.get_rect()
        self.restart_rect.topleft = (700, 500)

    def update(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.restart_img, self.restart_rect.topleft)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.restart_rect.collidepoint(mouse_pos):
            if mouse_click[0]:  # 왼쪽 클릭
                return "restart"

        return None
