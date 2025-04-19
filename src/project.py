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
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
    
    def get_cell_colors(self):

        dark_grey = (26,31,40)
        green = (47,230,23)
        red = (232,18,18)
        orange = (226,116,17)
        yellow = (237,234,4)
        purple = (166,0,247)
        cyan = (21,204,209)
        blue = (13,64,216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, 
                                        self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

class Block:
    def __init__(self):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0

class Colors:
    dark_grey = (26,31,40)
    green = (47,230,23)
    red = (232,18,18)
    orange = (226,116,17)
    yellow = (237,234,4)
    purple = (166,0,247)
    cyan = (21,204,209)
    blue = (13,64,216)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
def main():
    pygame.init()
    #colors
    dark_blue = (44,44,127)
    screen = pygame.display.set_mode((300,600))

    pygame.display.set_caption("Pytris")

    clock = pygame.time.Clock()
    game_grid = Grid()

    game_grid.grid[0][0] = 1
    game_grid.grid[3][5] = 4
    game_grid.grid[17][8] = 7

    game_grid.print_grid()
    game_running = True
    while game_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #drawing
        screen.fill(dark_blue)
        game_grid.draw(screen)
        pygame.display.update()
        clock.tick(60)
if __name__ == "__main__":
    main()