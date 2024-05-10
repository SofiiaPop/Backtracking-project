from collections import deque
from copy import deepcopy

def check_start_board(grid):
    for x_index in range(9):
        ratio = set()
        for el in grid[x_index]:
            if el not in ratio and el != 0:
                ratio.add(el)
            elif el != 0:
                return False

    for y_index in range(9):
        ratio.clear()
        for i in range(9):
            if grid[i][y_index] not in ratio and grid[i][y_index] != 0:
                ratio.add(grid[i][y_index])
            elif grid[i][y_index] != 0:
                return False

    for start_x in range(0, 9, 3):
        for start_y in range(0,9, 3):
            ratio.clear()
            for i in range(3):
                for j in range(3):
                    num = grid[start_y + i][start_x + j]
                    if num not in ratio and num != 0:
                        ratio.add(num)
                    elif num != 0:
                        return False
    return True

def check_board(grid, y_index, x_index, num):
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


def complete(grid):
    empty_cells = deque([])
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                empty_cells.append((y, x))
    if not empty_cells:
        return True
    else:
        y, x = empty_cells.popleft()
        for num in range(1, 10):
            if check_board(grid, x, y, num):
                grid[y][x] = num
                print(grid)
                if complete(grid):
                    return True
                grid[y][x] = 0
        return False

grid = []
grid.append([5, 3, 0, 0, 7, 0, 0, 0, 0])
grid.append([6, 0, 0, 1, 9, 5, 0, 0, 0])
grid.append([0, 9, 8, 0, 0, 0, 0, 6, 0])
grid.append([8, 0, 0, 0, 6, 0, 0, 0, 3])
grid.append([4, 0, 0, 8, 0, 3, 0, 0, 1])
grid.append([7, 0, 0, 0, 2, 0, 0, 0, 6])
grid.append([0, 6, 0, 0, 0, 0, 2, 8, 0])
grid.append([0, 0, 0, 4, 1, 9, 0, 0, 5])
grid.append([0, 0, 0, 0, 8, 0, 0, 7, 9])

if check_start_board(grid):
    if complete(grid):
        print("Sudoku solution")
        for row in grid:
            print(row)
else:
    print("This sudoku has no solution.")
