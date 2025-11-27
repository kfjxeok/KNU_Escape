import pygame
import os

class Stage6:
    def __init__(self):
        assets_root = os.path.join(os.path.dirname(__file__), "..", "Assets", "images")

        # ==========================
        # 배경 이미지
        # ==========================
        bg_path = os.path.join(assets_root, "stage6_gate.png")
        self.background = pygame.image.load(bg_path).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # ==========================
        # 캐릭터 이미지
        # ==========================
        self.frames = [
            pygame.image.load(os.path.join(assets_root, f"character{i}.png")).convert_alpha()
            for i in range(1, 4)
        ]
        self.frames = [pygame.transform.scale(frame, (80, 100)) for frame in self.frames]

        self.frame_index = 0
        self.anim_counter = 0

        # 캐릭터 시작 위치
        self.player_rect = self.frames[0].get_rect(center=(258, 553))

        # 시작 딜레이
        self.just_started = True
        self.start_timer = 0

        # 엔딩 히트박스 (419, 427 중심)
        self.ending_rect = pygame.Rect(419 - 5, 427 - 5, 10, 10)

    def update(self, screen):
        # 배경 그리기
        screen.blit(self.background, (0, 0))

        # 캐릭터 움직임
        if self.just_started:
            self.start_timer += 1
            if self.start_timer > 30:
                self.just_started = False
        else:
            mx, my = pygame.mouse.get_pos()
            self.player_rect.center = (mx, my)

        # 캐릭터 애니메이션
        self.anim_counter += 1
        if self.anim_counter >= 10:
            self.anim_counter = 0
            self.frame_index = (self.frame_index + 1) % 3

        screen.blit(self.frames[self.frame_index], self.player_rect)

        # 엔딩 좌표 → 다음 단계 신호 전달
        if self.player_rect.colliderect(self.ending_rect):
            return "next"   # ★ main.py의 흐름과 동일하게 next 반환

        return None
