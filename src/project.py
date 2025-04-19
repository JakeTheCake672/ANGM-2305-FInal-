import pygame, sys
import random
#tutorial im following
#https://www.youtube.com/watch?v=nF_crEtmpBo&t=1s

def main():
    pygame.init()
    screen = pygame.display.set_mode((300,600))

    pygame.display.set_caption("Pytris")

    clock = pygame.time.Clock()
    game_running = True
    while game_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main()