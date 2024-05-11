"""
Sudoku generation
"""
import random

class SudokuGenerator:
    """
    A class for generating Sudoku puzzles.
    """
    def __init__(self, difficulty = 0.5):
        """
        Initializes a SudokuGenerator object with the specified difficulty level.
        """
        self.num_to_remove = int(81 * difficulty)
        self.grid = [[0] * 9 for _ in range(9)]

    def generate_sudoku(self):
        """
        Generates a Sudoku puzzle by filling the grid with numbers and then removing
        a specified number of digits to achieve the desired difficulty level.
        """
        self.fill_diagonal()
        self.fill_remaining(0, 0)
        self.remove_numbers()

    def fill_diagonal(self):
        """
        Fills the diagonal cells of the Sudoku grid with random numbers.
        """
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(9):
            self.grid[i][i] = nums[i]

    def is_safe(self, row, col, num):
        """
        Checks if it is safe to place a number in the specified cell of the grid.
        """
        for i in range(9):
            if num in (self.grid[row][i], self.grid[i][col]):
                return False
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def fill_remaining(self, row, col):
        """
        Recursively fills the remaining cells of the Sudoku grid.
        """
        if row == 8 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if self.grid[row][col] != 0:
            return self.fill_remaining(row, col + 1)
        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.grid[row][col] = 0
        return False

    def remove_numbers(self):
        """
        Removes a specified number of digits from the filled Sudoku grid
        to achieve the desired difficulty level.
        """
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)
        for _ in range(self.num_to_remove):
            row, col = cells.pop()
            self.grid[row][col] = 0

if __name__ == "__main__":
    sudoku = SudokuGenerator()
    sudoku.generate_sudoku()
    sudoku.print_sudoku()
