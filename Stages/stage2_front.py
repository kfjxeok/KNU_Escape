import pygame
import os
import random

class Stage2:
    def __init__(self):
        assets_root = os.path.join(os.path.dirname(__file__), "..", "Assets", "images")

        # ==========================================================
        # 1) 벌 이미지 로드 (1.5배 크기로 적용)
        # ==========================================================
        self.bee_img = pygame.image.load(os.path.join(assets_root, "bee.png")).convert_alpha()
        self.bee_img = pygame.transform.scale(self.bee_img, (68, 53))  # 기존 크기의 1.5배

        # ==========================================================
        # 2) 배경 로드
        # ==========================================================
        bg_path = os.path.join(assets_root, "stage2_front.png")
        self.background = pygame.image.load(bg_path).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # ==========================================================
        # 3) 캐릭터 로드
        # ==========================================================
        self.frames = [
            pygame.image.load(os.path.join(assets_root, f"character{i}.png")).convert_alpha()
            for i in range(1, 4)
        ]
        self.frames = [pygame.transform.scale(f, (80, 100)) for f in self.frames]

        self.frame_index = 0
        self.anim_counter = 0

        # 플레이어 시작 위치
        self.player_rect = self.frames[0].get_rect(center=(65, 541))

        # 시작 딜레이
        self.just_started = True
        self.start_timer = 0

        # ==========================================================
        # 벌이 움직일 수 있는 구역
        # ==========================================================
        self.min_x = 0
        self.max_x = 784
        self.min_y = 386
        self.max_y = 598

        # ==========================================================
        # 벌 리스트 및 초기 스폰
        # ==========================================================
        self.bees = []
        self.spawn_bee()  # 벌 1마리 생성

        # ==========================================================
        # 다음 스테이지 문
        # ==========================================================
        self.door_rect = pygame.Rect(427, 365, 15, 15)

    # --------------------------------------------------------------
    # 벌 생성 함수
    # --------------------------------------------------------------
    def spawn_bee(self, x=None, y=None, generation=1, speed=2):

        W = self.bee_img.get_width()
        H = self.bee_img.get_height()

        # 랜덤 생성
        if x is None:
            x = random.randint(self.min_x + W, self.max_x - W)
        if y is None:
            y = random.randint(self.min_y + H, self.max_y - H)

        dx = random.choice([-1, 1]) * speed
        dy = random.choice([-1, 1]) * speed

        rect = self.bee_img.get_rect(center=(x, y))

        self.bees.append({
            "rect": rect,
            "dx": dx,
            "dy": dy,
            "generation": generation,
            "has_split": False  # ★ 최초 생성 시 분열 없음
        })

    # --------------------------------------------------------------
    # 벌 분열 (1세대만 1번 가능)
    # --------------------------------------------------------------
    def split_bee(self, bee):
        # 이미 한 번 분열한 벌이면 종료
        if bee["has_split"]:
            return

        # 1세대 벌만 분열 가능
        if bee["generation"] != 1:
            return

        # 이제 더 이상 분열하지 않게 설정
        bee["has_split"] = True

        x, y = bee["rect"].center
        next_speed = abs(bee["dx"]) * 1.2

        # 2세대 벌 2마리 생성
        for _ in range(2):
            self.spawn_bee(x, y, generation=2, speed=next_speed)

    # --------------------------------------------------------------
    # 벌 이동 + 벽 충돌 + 분열
    # --------------------------------------------------------------
    def update_bees(self):
        for bee in list(self.bees):
            rect = bee["rect"]
            rect.x += bee["dx"]
            rect.y += bee["dy"]

            hit_wall = False

            # 좌우 벽
            if rect.left <= self.min_x or rect.right >= self.max_x:
                bee["dx"] *= -1
                hit_wall = True

            # 상하 벽
            if rect.top <= self.min_y or rect.bottom >= self.max_y:
                bee["dy"] *= -1
                hit_wall = True

            # 벽에 닿으면 분열 (1세대만)
            if hit_wall:
                self.split_bee(bee)

    # --------------------------------------------------------------
    # 스테이지 UPDATE
    # --------------------------------------------------------------
    def update(self, screen):
        screen.blit(self.background, (0, 0))

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

        screen.blit(self.frames[self.frame_index], self.player_rect)

        # 벌 업데이트
        self.update_bees()

        # 벌 그리기 및 충돌 체크
        for bee in self.bees:
            screen.blit(self.bee_img, bee["rect"])

            # 벌과 닿으면 게임오버
            if self.player_rect.colliderect(bee["rect"]):
                return "gameover"

        # 문 충돌 → 다음 스테이지
        if self.player_rect.colliderect(self.door_rect):
            return "next"

        return None
