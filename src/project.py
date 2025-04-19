import pygame, sys
import random
#tutorial im following
#https://www.youtube.com/watch?v=nF_crEtmpBo&t=1s

def main():
    pygame.init()
    #colors
    dark_blue = (44,44,127)
    screen = pygame.display.set_mode((300,600))

    pygame.display.set_caption("Pytris")

    clock = pygame.time.Clock()
    game_running = True
    while game_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #drawing
        screen.fill(dark_blue)
        pygame.display.update()
        clock.tick(60)
if __name__ == "__main__":
    main()