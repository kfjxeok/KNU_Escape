import pygame
import os
import random

class Stage3:
    def __init__(self):
        assets_root = os.path.join(os.path.dirname(__file__), "..", "Assets", "images")

        # ==========================
        # 1) 배경 이미지
        # ==========================
        bg_path = os.path.join(assets_root, "stage3_bridge.png")
        self.background = pygame.image.load(bg_path).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # ==========================
        # 2) 캐릭터 이미지
        # ==========================
        self.frames = [
            pygame.image.load(os.path.join(assets_root, f"character{i}.png")).convert_alpha()
            for i in range(1, 4)
        ]
        self.frames = [pygame.transform.scale(f, (80, 100)) for f in self.frames]

        self.frame_index = 0
        self.anim_counter = 0

        # 플레이어 시작 위치 (131, 544)
        self.player_rect = self.frames[0].get_rect(center=(131, 544))

        # 시작 딜레이 (무적 시간)
        self.just_started = True
        self.start_timer = 0

        # ==========================
        # 3) CCTV 이미지 (장식)
        # ==========================
        self.cctv_img = pygame.image.load(os.path.join(assets_root, "cctv.png")).convert_alpha()
        self.cctv_img = pygame.transform.scale(self.cctv_img, (50, 50))
        self.cctv_rect = self.cctv_img.get_rect(center=(417, 132))

        # ==========================
        # 4) 빛(light) 설정
        # ==========================
        self.light_img = pygame.image.load(os.path.join(assets_root, "light.png")).convert_alpha()

        # ★ 너가 요청한 크기 적용 (550x250)
        self.light_img = pygame.transform.scale(self.light_img, (550, 250))

        self.light_x = 524
        self.light_min_y = 235
        self.light_max_y = 593

        start_y = random.randint(self.light_min_y, self.light_max_y)
        self.light_rect = self.light_img.get_rect(center=(self.light_x, start_y))

        self.light_speed = 3
        self.light_dir = 1

        # ==========================
        # 5) 도착 지점
        # ==========================
        self.door_rect = pygame.Rect(527 - 10, 206 - 10, 20, 20)

    # ------------------------------
    # 빛 움직임 업데이트
    # ------------------------------
    def update_light(self):
        self.light_rect.centery += self.light_dir * self.light_speed

        if self.light_rect.centery <= self.light_min_y:
            self.light_rect.centery = self.light_min_y
            self.light_dir = 1

        if self.light_rect.centery >= self.light_max_y:
            self.light_rect.centery = self.light_max_y
            self.light_dir = -1

    # ------------------------------
    # 스테이지 업데이트
    # ------------------------------
    def update(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.cctv_img, self.cctv_rect.topleft)

        # 시작 딜레이
        if self.just_started:
            self.start_timer += 1
            if self.start_timer > 60:
                self.just_started = False
        else:
            mx, my = pygame.mouse.get_pos()
            self.player_rect.center = (mx, my)

        # 캐릭터 애니메이션
        self.anim_counter += 1
        if self.anim_counter >= 10:
            self.anim_counter = 0
            self.frame_index = (self.frame_index + 1) % 3

        # 빛 업데이트 + 그리기
        self.update_light()
        screen.blit(self.light_img, self.light_rect.topleft)

        # 캐릭터 그리기
        screen.blit(self.frames[self.frame_index], self.player_rect)

        # -------------------------
        # ● 빛 히트박스 축소 + 충돌 판정
        # -------------------------
        hitbox = self.light_rect.inflate(-350, -150)  # ★ 히트박스 축소
        # pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)  # 디버그용

        if not self.just_started:
            if self.player_rect.colliderect(hitbox):
                return "gameover"

        # -------------------------
        # ● 도착 지점 도달 → 다음 스테이지
        # -------------------------
        if self.player_rect.colliderect(self.door_rect):
            return "next"

        return None
