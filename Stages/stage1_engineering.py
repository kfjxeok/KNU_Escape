import pygame
import os

class Stage1:
    def __init__(self):
        assets = os.path.join(os.path.dirname(__file__), "..", "Assets")
        img_path = os.path.join(assets, "images", "stage1_engineering.png")

        self.background = pygame.image.load(img_path).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # 캐릭터 이미지 로드
        self.frames = [
            pygame.image.load(os.path.join(assets, "images", f"character{i}.png"))
            for i in range(1, 4)
        ]
        self.frames = [pygame.transform.scale(frame, (80, 100)) for frame in self.frames]

        self.frame_index = 0
        self.animation_counter = 0

        # ★ 캐릭터 시작 위치
        self.player_rect = self.frames[0].get_rect(center=(32, 487))

        # -------------------------
        # ★ 게임 시작 후 10프레임 정지
        # -------------------------
        self.just_started = True
        self.start_timer = 0

        # 책상 충돌 박스 (size = 30x20)
        self.blocks = [
            # 상단 (더 작게 20x15)
            pygame.Rect(209 - 10, 193 - 7, 10, 5),
            pygame.Rect(316 - 10, 217 - 7, 10, 5),
            pygame.Rect(444 - 10, 253 - 7, 10, 5),
            pygame.Rect(582 - 10, 288 - 7, 10, 5),
            pygame.Rect(736 - 10, 321 - 7, 10, 5),

            # 나머지 30x20
            pygame.Rect(88 - 15, 237 - 10, 20, 10),
            pygame.Rect(202 - 15, 275 - 10, 20, 10),
            pygame.Rect(339 - 15, 312 - 10, 20, 10),
            pygame.Rect(484 - 15, 358 - 10, 20, 10),

            # 수정된 책상
            pygame.Rect(668 - 15, 431 - 10, 20, 10),

            pygame.Rect(62 - 15, 335 - 10, 20, 10),
            pygame.Rect(195 - 15, 387 - 10, 20, 10),
            pygame.Rect(348 - 15, 440 - 10, 20, 10),
            pygame.Rect(549 - 15, 515 - 10, 20, 10),
            pygame.Rect(745 - 15, 562 - 10, 20, 10),
            pygame.Rect(196 - 15, 545 - 10, 20, 10),
        ]

        # 문 충돌 (5x5)
        self.door_rect = pygame.Rect(683, 241, 5, 5)

    def update(self, screen):
        screen.blit(self.background, (0, 0))

        # -------------------------
        # ⭐ 첫 10프레임 동안 캐릭터는 그대로
        # -------------------------
        if self.just_started:
            self.start_timer += 1
            if self.start_timer > 60:
                self.just_started = False
        else:
            mx, my = pygame.mouse.get_pos()
            self.player_rect.center = (mx, my)

        # 캐릭터 애니메이션
        self.animation_counter += 1
        if self.animation_counter >= 10:
            self.animation_counter = 0
            self.frame_index = (self.frame_index + 1) % 3

        screen.blit(self.frames[self.frame_index], self.player_rect)

        # -------------------------
        # ● 충돌 체크
        # -------------------------
        for block in self.blocks:
            if self.player_rect.colliderect(block):
                return "gameover"

        # -------------------------
        # ● 다음 스테이지로 이동
        # -------------------------
        if self.player_rect.colliderect(self.door_rect):
            return "next"

        return None
