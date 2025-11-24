import pygame
import sys
from Stages.stage1_engineering import Stage1
from Stages.stage2_bridge import Stage2
from Stages.stage3_shalom import Stage3
from Stages.stage4_gate import Stage4

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("강남대 탈출")

clock = pygame.time.Clock()

current_stage = Stage1()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        current_stage.update(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
