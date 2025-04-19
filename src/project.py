import pygame, sys
import random
#tutorial im following
#https://www.youtube.com/watch?v=nF_crEtmpBo&t=1s
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()


def main():
    pygame.init()
    #colors
    dark_blue = (44,44,127)
    screen = pygame.display.set_mode((300,600))

    pygame.display.set_caption("Pytris")

    clock = pygame.time.Clock()
    game_grid = Grid()
    game_grid.print_grid()
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