import pygame

class Stage1:
    def __init__(self):
        self.player_width = 50
        self.player_height = 50

        # 배경 이미지 로드
        self.background = pygame.image.load("assets/background1.png")
        self.background = pygame.transform.scale(self.background, (800, 600))

    def update(self, screen):
        # 배경 그리기
        screen.blit(self.background, (0, 0))

        # 마우스 위치 가져오기
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # 플레이어를 마우스 위치 중심으로 그림
        player_rect = pygame.Rect(mouse_x - self.player_width//2,
                                  mouse_y - self.player_height//2,
                                  self.player_width,
                                  self.player_height)
        pygame.draw.rect(screen, (255, 0, 0), player_rect)
