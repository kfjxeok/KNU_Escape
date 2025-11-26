import pygame
import os

class Stage5:
    def __init__(self):
        base = os.path.dirname(os.path.dirname(__file__))   # knu_escape/
        assets = os.path.join(base, "Assets", "images")

        # 배경 이미지 로드
        self.background = pygame.image.load(
            os.path.join(assets, "stage5_select.png")
        ).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # 캐릭터 애니메이션 프레임
        self.walk_frames = [
            pygame.transform.scale(
                pygame.image.load(os.path.join(assets, "character1.png")).convert_alpha(),
                (80, 100)
            ),
            pygame.transform.scale(
                pygame.image.load(os.path.join(assets, "character2.png")).convert_alpha(),
                (80, 100)
            ),
            pygame.transform.scale(
                pygame.image.load(os.path.join(assets, "character3.png")).convert_alpha(),
                (80, 100)
            ),
        ]

        self.frame_index = 0
        self.animation_speed = 0.2
        self.player_rect = self.walk_frames[0].get_rect(center=(100, 500))

    def update(self, screen):
        # 배경 그리기
        screen.blit(self.background, (0, 0))

        # 캐릭터 위치 마우스 따라가기
        mx, my = pygame.mouse.get_pos()
        self.player_rect.center = (mx, my)

        # 캐릭터 걷기 애니메이션
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.walk_frames):
            self.frame_index = 0
        frame = self.walk_frames[int(self.frame_index)]

        # 캐릭터 그리기
        screen.blit(frame, self.player_rect)

        return "stay"
