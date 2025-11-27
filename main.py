import pygame
import sys

# ==========================
# Screens
# ==========================
from Screens.start import StartScreen
from Screens.gameover import GameOverScreen
from Screens.ending import EndingScreen

# ==========================
# Stages
# ==========================
from Stages.stage1_engineering import Stage1
from Stages.stage2_front import Stage2
from Stages.stage3_bridge import Stage3
from Stages.stage4_shalom import Stage4
from Stages.stage5_select import Stage5
from Stages.stage6_gate import Stage6

# ==========================
# Pygame 기본 설정
# ==========================
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("강남대 탈출")

clock = pygame.time.Clock()

# ==========================
# 초기 상태
# ==========================
current_state = "start"   # 프로그램 실행 시 처음엔 START 화면
current_stage = None

# 화면 객체 생성
start_screen = StartScreen()
gameover_screen = GameOverScreen()
ending_screen = EndingScreen()

# ==========================
# 메인 루프
# ==========================
def main():
    global current_state, current_stage

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        # ============================================
        #  START SCREEN
        # ============================================
        if current_state == "start":
            result = start_screen.update(screen)

            if result == "start_game":
                current_stage = Stage1()
                current_state = "stage"

        # ============================================
        #  STAGE MODE
        # ============================================
        elif current_state == "stage":
            result = current_stage.update(screen)

            # 다음 스테이지 이동 처리
            if result == "next":
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
                    # Stage6 다음은 엔딩 화면
                    current_state = "ending"

            # 게임오버 이동
            elif result == "gameover":
                current_state = "gameover"

        # ============================================
        #  GAMEOVER SCREEN
        # ============================================
        elif current_state == "gameover":
            result = gameover_screen.update(screen)

            if result == "restart":
                # GameOver 후 다시 시작 시에는 START 화면 X
                # 바로 Stage1부터 다시 진행
                current_stage = Stage1()
                current_state = "stage"

        # ============================================
        #  ENDING SCREEN
        # ============================================
        elif current_state == "ending":
            # Ending 화면은 내부에서 버튼 누르면 게임 종료함
            ending_screen.update(screen)

        # 화면 업데이트
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
