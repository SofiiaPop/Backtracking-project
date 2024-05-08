"""
Maze visualization
"""
import pygame
import numpy as np

def get_maze(filename: str) -> tuple:
    """
    Read maze from the file
    """
    with open(filename, "r", encoding="utf-8") as maze_file:
        size = maze_file.readline().strip().strip("ROWS ")
        size = size.split(" COLS ")
        size = tuple(int(coord) for coord in size)

        walls = {}
        path_ = []
        for wall in maze_file.readlines():
            if "WALL" in wall:
                wall = wall.strip().strip("WALL ").split()
                wall = tuple(int(item) for item in wall)

                if wall[0] not in walls:
                    walls[wall[0]] = [wall[1]]
                else:
                    walls[wall[0]].append(wall[1])

                if wall[1] not in walls:
                    walls[wall[1]] = [wall[0]]
                else:
                    walls[wall[1]].append(wall[0])
            else:
                path = int(wall.strip("PATH").strip())
                path_.append(path)

        return size, walls, path_

def create_maze(size: tuple, walls: dict) -> list:
    """
    Maze creation
    """
    values = []
    for row in range(size[0]):
        row_ = []
        for col in range(size[1]):
            value = row * size[1] + col
            if value in walls:
                row_.append({value: walls[value]})
            else:
                row_.append({value: []})
        values.append(row_)

    maze = np.array(values)
    return maze

def visualize_maze(screen, maze_data, rows, cols, path, current_step):
    """
    Maze visualization
    """
    cell_size = 30
    maze_width = cols * cell_size
    maze_height = rows * cell_size

    # Create layers
    walls_layer = pygame.Surface((maze_width, maze_height), pygame.SRCALPHA)
    path_layer = pygame.Surface((maze_width, maze_height), pygame.SRCALPHA)

    # Draw walls
    for i in range(rows):
        for j in range(cols):
            cell_data = maze_data[i][j]
            x = j * cell_size
            y = i * cell_size

            pygame.draw.rect(walls_layer, (255, 255, 255), (x, y, cell_size, cell_size), 1)

            cell_value = i * cols + j
            for key, values in cell_data.items():
                for value in values:
                    neighbor_value = value
                    if neighbor_value == cell_value + 1:  # Wall on the right
                        pygame.draw.line(walls_layer, (0, 0, 0), (x + cell_size, y), (x + cell_size, y + cell_size), 2)
                    elif neighbor_value == cell_value - 1:  # Wall on the left
                        pygame.draw.line(walls_layer, (0, 0, 0), (x, y), (x, y + cell_size), 2)
                    elif neighbor_value == cell_value + cols:  # Wall at the bottom
                        pygame.draw.line(walls_layer, (0, 0, 0), (x, y + cell_size), (x + cell_size, y + cell_size), 2)
                    elif neighbor_value == cell_value - cols:  # Wall at the top
                        pygame.draw.line(walls_layer, (0, 0, 0), (x, y), (x + cell_size, y), 2)

    # Draw path
    for idx, cell in enumerate(path[:current_step]):
        row, col = divmod(cell, cols)
        x = col * cell_size
        y = row * cell_size
        # pygame.draw.rect(path_layer, (64, 224, 208), (x, y, cell_size, cell_size))
        pygame.draw.rect(path_layer, (64, 224, 208, 200), (x, y, cell_size, cell_size))


    # Blit layers onto the screen
    screen.blit(walls_layer, (0, 0))
    screen.blit(path_layer, (0, 0))


def main(file_name: str):
    pygame.init()

    data = get_maze(file_name)
    maze = create_maze(data[0], data[1])
    rows, cols = data[0]
    path = data[2]

    cell_size = 30
    maze_width = cols * cell_size
    maze_height = rows * cell_size

    screen_width = maze_width
    screen_height = maze_height
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Visualization")

    clock = pygame.time.Clock()
    running = True
    current_step = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        visualize_maze(screen, maze, rows, cols, path, current_step)
        pygame.display.flip()
        clock.tick(15)

        current_step += 1
        if current_step >= len(path):
            current_step = len(path)

    pygame.quit()
