import pygame
import os

class StartScreen:
    def __init__(self):
        # Assets/images 폴더 경로
        assets = os.path.join(os.path.dirname(__file__), "..", "Assets", "images")

        # 배경 이미지 (start.png)
        self.background = pygame.image.load(
            os.path.join(assets, "start.png")
        ).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # start 버튼 이미지 (start_b.png)
        self.start_img = pygame.image.load(
            os.path.join(assets, "start_b.png")
        ).convert_alpha()
        # 필요하면 크기 조정 (gameover 버튼처럼 80x80)
        self.start_img = pygame.transform.scale(self.start_img, (80, 80))

        # 버튼 위치: 오른쪽 아래 (gameover랑 동일)
        self.start_rect = self.start_img.get_rect()
        self.start_rect.topleft = (700, 500)

    def update(self, screen):
        # 배경, 버튼 그리기
        screen.blit(self.background, (0, 0))
        screen.blit(self.start_img, self.start_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # 버튼 클릭 체크
        if self.start_rect.collidepoint(mouse_pos):
            if mouse_click[0]:  # 왼쪽 클릭
                return "start_game"

        return None
