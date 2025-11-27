import pygame
import os
import sys

class EndingScreen:
    def __init__(self):
        assets = os.path.join(os.path.dirname(__file__), "..", "Assets", "images")

        # 배경 이미지
        self.background = pygame.image.load(
            os.path.join(assets, "ending.png")
        ).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # 종료 버튼 이미지 (end_b.png)
        self.finish_img = pygame.image.load(
            os.path.join(assets, "end_b.png")
        ).convert_alpha()
        self.finish_img = pygame.transform.scale(self.finish_img, (80, 80))

        # 버튼 위치 (start, restart와 동일)
        self.finish_rect = self.finish_img.get_rect()
        self.finish_rect.topleft = (700, 500)

    def update(self, screen):
        # 배경 / 버튼 그리기
        screen.blit(self.background, (0, 0))
        screen.blit(self.finish_img, self.finish_rect.topleft)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # 버튼 클릭 시 프로그램 종료
        if self.finish_rect.collidepoint(mouse_pos):
            if mouse_click[0]:  # 왼쪽 클릭
                pygame.quit()
                sys.exit()

        return None
