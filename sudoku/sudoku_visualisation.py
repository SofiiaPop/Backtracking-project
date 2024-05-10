"""
Sudoku
"""
import pygame
import sys
import argparse
from collections import deque
from copy import deepcopy
from sudoku import Sudoku

class Solver:
    """
    This class represents a Sudoku solver application.
    """
    def __init__(self):
        """
        Initializes the Sudoku class.
        """
        pygame.init()
        self.screen_height = pygame.display.Info().current_h - 300
        self.grid_size = self.screen_height / 9
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_height))

    def draw_grid(self):
        """
        Draws the grid lines on the screen.
        """
        for i in range(10):
            if i % 3 == 0:
                thick = 5
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.grid_size),
                             (self.screen_height, i * self.grid_size), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.grid_size, 0),
                             (i * self.grid_size, self.screen_height), thick)

    def draw_numbers(self, grid):
        """
        Draws the numbers of the Sudoku grid on the screen.
        """
        cell_color = (255, 255, 255)
        for y in range(9):
            for x in range(9):
                if grid[y][x] != 0:
                    num_text = pygame.font.SysFont(None, 30).\
render(str(grid[y][x]), True, (0, 0, 0))#This line renders the number contained in the cell (y, x) of the grid onto the screen using the pygame library. It converts the number to a string, sets the text color to black (0, 0, 0), and renders the text using a system font with size 30.
                    pygame.draw.rect(self.screen, cell_color,
(x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size))
                    self.draw_grid()
                    self.screen.blit(num_text, (x * self.grid_size + self.grid_size // \
2 - num_text.get_width() // 2, y * self.grid_size + self.grid_size \
// 2 - num_text.get_height() // 2))

    def check_board(self, grid, y_index, x_index, num):
        """
        Checks if a number can be placed in a specific cell on the Sudoku grid.
        """
        grid_copy = deepcopy(grid)
        grid_copy[x_index][y_index] = num

        ratio = set()
        for el in grid_copy[x_index]:
            if el not in ratio and el != 0:
                ratio.add(el)
            elif el != 0:
                return False

        ratio.clear()
        for i in range(9):
            if grid_copy[i][y_index] not in ratio and grid_copy[i][y_index] != 0:
                ratio.add(grid_copy[i][y_index])
            elif grid_copy[i][y_index] != 0:
                return False

        ratio.clear()
        start_x = (x_index // 3) * 3
        start_y = (y_index // 3) * 3
        for i in range(3):
            for j in range(3):
                num = grid_copy[start_y + i][start_x + j]
                if num not in ratio and num != 0:
                    ratio.add(num)
                elif num != 0:
                    return False
        return True

    def complete(self, grid):
        """
        Recursively completes the Sudoku grid.
        """
        empty_cells = deque([])
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    empty_cells.append((y, x))
        if not empty_cells:
            return True
        y, x = empty_cells.popleft()
        for num in range(1, 10):
            if self.check_board(grid, x, y, num):
                grid[y][x] = num
                self.draw_grid()
                self.draw_numbers(grid)
                pygame.display.flip()
                pygame.time.delay(10)
                if self.complete(grid):
                    return True
                grid[y][x] = 0
        return False

    def solve(self, grid):
        """
        Solves the Sudoku grid using backtracking.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_numbers(grid)
            pygame.display.flip()
            self.complete(grid)
            pygame.image.save(self.screen, "sudoku_grid.png")
        pygame.quit()
        sys.exit()

def solve_sudoku(input_file):
    sudoku = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n').split(' ')
            sudoku.append(line)
    if len(sudoku) != 9:
        print("Sudoku grid must contain 9 rows.")
        sys.exit()

    for row in sudoku:
        if len(row) != 9:
            print("Each row in the Sudoku grid must contain 9 digits.")
            sys.exit()

        for digit in row:
            if not digit.isdigit() or int(digit) not in range(0,10):
                print("Sudoku grid must contain only digits from 0 to 9.")
                sys.exit()
    for num, row in enumerate(sudoku):
        for dig_num, digit in enumerate(row):
            sudoku[num][dig_num] = int(digit)
    solver = Solver()
    solver.solve(sudoku)

def main():
    parser = argparse.ArgumentParser(description='Solve a Sudoku puzzle from a file \
or generate a random one')
    parser.add_argument('--input_file', type=str, help='Input file containing the Sudoku puzzle ')
    args = parser.parse_args()

    if args.input_file:
        solve_sudoku(args.input_file)
    else:
        solver = Solver()
        grid = Sudoku(3).difficulty(0.5)
        # solution = grid.solve()
        # solution.show()
        grid = grid.board
        for line_num, line in enumerate(grid):
            for el_num, el in enumerate(line):
                if not el:
                    grid[line_num][el_num] = 0
            print(line)
        solver.solve(grid)

    print("Sudoku solved")
if __name__ == "__main__":
    main()
