import pygame
import sys

from Stages.stage1_engineering import Stage1
from Stages.stage2_front import Stage2
from Stages.stage3_bridge import Stage3
from Stages.stage4_shalom import Stage4
from Stages.stage5_select import Stage5
from Stages.stage6_gate import Stage6

from Screens.gameover import GameOverScreen

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("강남대 탈출")

clock = pygame.time.Clock()

current_state = "stage"
current_stage = Stage1()
gameover_screen = GameOverScreen()

def main():
    global current_state, current_stage

    while True:
        #print(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        # ============================
        #        ★ 스테이지 모드
        # ============================
        if current_state == "stage":
            result = current_stage.update(screen)

            if result == "next":  # 다음 스테이지로 이동
                if isinstance(current_stage, Stage1):
                    current_stage = Stage2()
                elif isinstance(current_stage, Stage2):
                    current_stage = Stage3()
                elif isinstance(current_stage, Stage3):
                    current_stage = Stage4()
                elif isinstance(current_stage, Stage4):
                    current_stage = Stage5()
                elif isinstance(current_stage, Stage5):
                    current_stage = Stage6()
                elif isinstance(current_stage, Stage6):
                    pass  # 마지막 스테이지

            elif result == "gameover":
                current_state = "gameover"

        # ============================
        #      ★ 게임오버 화면
        # ============================
        elif current_state == "gameover":
            result = gameover_screen.update(screen)

            if result == "restart":
                current_state = "stage"
                current_stage = Stage1()  # 스테이지1로 초기화

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
