import pygame
import os
import time

class Stage4:
    def __init__(self):
        assets_root = os.path.join(os.path.dirname(__file__), "..", "Assets", "images")

        # ==========================
        # 배경 이미지
        # ==========================
        bg_path = os.path.join(assets_root, "stage4_shalom.png")
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
        self.player_rect = self.frames[0].get_rect(center=(539, 549))

        # ==========================
        # face 이미지 (전체 화면)
        # ==========================
        self.prof_img = pygame.image.load(os.path.join(assets_root, "face.png")).convert_alpha()
        self.prof_img = pygame.transform.scale(self.prof_img, (800, 600))

        self.prof_showing = False
        self.prof_start_time = 0

        # ==========================
        # 히트박스 설정 (10×10)
        # ==========================
        self.elevator1_rect = pygame.Rect(86 - 5, 203 - 5, 10, 10)
        self.elevator2_rect = pygame.Rect(312 - 5, 205 - 5, 10, 10)
        self.stairs_rect     = pygame.Rect(722 - 5, 399 - 5, 10, 10)

        # 시작 딜레이
        self.just_started = True
        self.start_timer = 0

    def update(self, screen):
        # 배경
        screen.blit(self.background, (0, 0))

        # -----------------------------------------
        # face.png 화면 전체 표시 (3초 유지)
        # -----------------------------------------
        if self.prof_showing:
            screen.blit(self.prof_img, (0, 0))

            if time.time() - self.prof_start_time > 3:
                return "gameover"
            return None

        # -----------------------------------------
        # 캐릭터 이동
        # -----------------------------------------
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

        # 캐릭터 그리기
        screen.blit(self.frames[self.frame_index], self.player_rect)

        # -----------------------------------------
        # 엘리베이터 → 교수님 등장
        # -----------------------------------------
        if (self.player_rect.colliderect(self.elevator1_rect) or
            self.player_rect.colliderect(self.elevator2_rect)):
            self.prof_showing = True
            self.prof_start_time = time.time()
            return None

        # -----------------------------------------
        # 계단 → 다음 스테이지
        # -----------------------------------------
        if self.player_rect.colliderect(self.stairs_rect):
            return "next"

        return None
