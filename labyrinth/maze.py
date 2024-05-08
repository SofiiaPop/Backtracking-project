"""
Maze solver. Backtracing algorithm.
"""
from collections import deque
import argparse
import maze_visual

def read_file(filename: str) -> list:
    """Read file"""
    with open(filename, "r", encoding="utf-8") as maze:
        size = maze.readline().strip().strip("ROWS ")
        size = size.split(" COLS ")
        size = tuple([int(coord) for coord in size])

        walls = {}
        for wall in maze.readlines():

            wall = wall.strip().strip("WALL ").split()
            wall = tuple([int(item) for item in wall])

            if wall[0] not in walls:
                walls[wall[0]] = [wall[1]]
            else:
                walls[wall[0]].append(wall[1])

            if wall[1] not in walls:
                walls[wall[1]] = [wall[0]]
            else:
                walls[wall[1]].append(wall[0])

        return size, walls

class Node:
    """Class Node"""
    def __init__(self, value: int, position: tuple) -> None:
        self.value = value
        self.position = position
        self.children = []

    def __repr__(self) -> str:
        return f"{self.value}"

    def __eq__(self, other: "Node") -> bool:
        return self.value == other.value and self.position == other.position

    def __hash__(self):
        return hash(self.value)

def create_path(node: "Node", aim_node: "Node", size: tuple, walls: dict, \
    visited_stack: set = None) -> None:
    """Create path"""
    if visited_stack is None:
        visited_stack = set()
        visited_stack.add(node)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in directions:
        new_i, new_j = node.position[0] + di, node.position[1] + dj
        coef = new_i * size[1] + new_j
        if 0 <= new_i < size[0] and 0 <= new_j < size[1] and \
            (node.value not in walls or coef not in walls[node.value]):
            child = Node(coef, (new_i, new_j))
            if child not in visited_stack:
                node.children.append(child)

    for child in node.children:
        if child == aim_node:
            child.children.append(aim_node)
            return
        visited_stack.add(child)
        create_path(child, aim_node, size, walls, visited_stack)
        visited_stack.remove(child)

def find_path(start_node: "Node", end_node: "Node"):
    """Find path"""
    queue = deque([(start_node, [start_node])])

    while queue:
        cur_node, path = queue.popleft()

        if cur_node == end_node:
            return path

        for child in cur_node.children:
            queue.append((child, path + [child]))

def sovle_maze(source_file: str, destination_file: str) -> None:
    """Generate result"""
    size_, walls_ = read_file(source_file)
    root_n = Node(0, (0, 0))
    end_n = Node((size_[0] - 1) * size_[1] + size_[1] - 1, (size_[0] - 1, size_[1] - 1))
    create_path(root_n, end_n, size_, walls_)

    path = find_path(root_n, end_n)

    with open(source_file, 'r', encoding='utf-8') as src:
        content = src.read()

    with open(destination_file, "w", encoding="utf-8") as f:
        f.write(content)
        for value in path:
            f.write(f"PATH {value}\n")

def main():
    """Main"""
    parser = argparse.ArgumentParser(description='Solve a maze and save the solution to a file')
    parser.add_argument('source_file', type=str, help='Path to the source maze file')
    parser.add_argument('destination_file', type=str, help='Path to the destination file to save the solved maze')
    parser.add_argument('-v', '--visualize', action='store_true', help='Visualize the solution maze')
    args = parser.parse_args()

    sovle_maze(args.source_file, args.destination_file)
    print(f"Maze solved and saved to {args.destination_file}")
    if args.visualize:
        maze_visual.main(args.destination_file)

if __name__ == "__main__":
    main()
