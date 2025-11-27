import pygame
import os
import time

class Stage5:
    def __init__(self):
        assets_root = os.path.join(os.path.dirname(__file__), "..", "Assets", "images")

        # ==========================
        # 배경 이미지
        # ==========================
        bg_path = os.path.join(assets_root, "stage5_select.png")
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

        # 캐릭터 시작 위치 (600, 588)
        self.player_rect = self.frames[0].get_rect(center=(600, 588))

        # 시작 딜레이
        self.just_started = True
        self.start_timer = 0

        # ==========================
        # face.png (전체 화면)
        # ==========================
        self.prof_img = pygame.image.load(os.path.join(assets_root, "face.png")).convert_alpha()
        self.prof_img = pygame.transform.scale(self.prof_img, (800, 600))

        self.prof_showing = False
        self.prof_start_time = 0

        # ==========================
        # 히트박스 (10×10)
        # ==========================
        # 게임오버 좌표: (269, 375)
        self.gameover_rect = pygame.Rect(269 - 5, 375 - 5, 10, 10)

        # 다음 스테이지 좌표: (486, 322) (그대로 유지)
        self.next_rect = pygame.Rect(486 - 5, 322 - 5, 10, 10)

    def update(self, screen):
        # 배경
        screen.blit(self.background, (0, 0))

        # face 이미지 표시 중이면 3초 후 게임오버
        if self.prof_showing:
            screen.blit(self.prof_img, (0, 0))
            if time.time() - self.prof_start_time > 3:
                return "gameover"
            return None

        # 캐릭터 이동
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

        # ----- 충돌 판정 -----

        # 1) 게임오버 구역 → face 3초 표시
        if self.player_rect.colliderect(self.gameover_rect):
            self.prof_showing = True
            self.prof_start_time = time.time()
            return None

        # 2) 다음 스테이지 이동
        if self.player_rect.colliderect(self.next_rect):
            return "next"

        return None
