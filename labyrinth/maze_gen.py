"""
Maze generation
"""
from random import choice
import argparse

class Node:
    """Node class"""
    def __init__(self, value: int, position: tuple) -> None:
        self.value = value
        self.position = position
        self.connected = []
        self.children = []
        self.parents = []

    def __eq__(self, other: "Node") -> bool:
        return self.position == other.position

    def __repr__(self) -> str:
        return f"{self.position}"

    def __hash__(self) -> int:
        return hash((self.value, self.position))

def create_path(start_node: "Node", rows: int, cols: int) -> "Node":
    """Create path"""
    visited = []
    visited.append(start_node)
    to_visit = []

    find_children(start_node, (rows, cols))
    start_node.parents = start_node.children[::]

    for child in start_node.children:
        if child not in visited:
            to_visit.append(child)

    while to_visit:
        node_to_connect = choice(to_visit)
        find_children(node_to_connect, (rows, cols))

        to_visit.remove(node_to_connect)
        visited.append(node_to_connect)

        parent_to_connect = choice(node_to_connect.parents)
        parent_to_connect.connected.append(node_to_connect)

        for child in node_to_connect.children:
            if child not in visited and child not in to_visit:
                to_visit.append(child)

def find_children(node: "Node", size: tuple) -> None:
    """Find children"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in directions:
        new_i, new_j = node.position[0] + di, node.position[1] + dj
        coef = new_i * size[1] + new_j
        if 0 <= new_i < size[0] and 0 <= new_j < size[1]:
            child = Node(coef, (new_i, new_j))
            node.children.append(child)
            child.parents.append(node)

def find_walls(cur_node: "Node", walls: set = None) -> list:
    """Find walls"""
    if walls is None:
        walls = set()

    for child in cur_node.children:
        if child not in cur_node.connected and child not in cur_node.parents:
            if (child.value, cur_node.value) not in walls:
                walls.add((cur_node.value, child.value))

    for child in cur_node.children:
        find_walls(child, walls)
    return walls

def generate_maze(rows: int, cols: int, output_file: str) -> None:
    """Generate maze"""

    start_n = Node(0, (0, 0))
    create_path(start_n, rows, cols)
    walls = find_walls(start_n)

    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(f"ROWS {rows} COLS {cols}\n")
        for wall in walls:
            f.write(f"WALL {wall[0]} {wall[1]}\n")

def main():
    """Main"""
    parser = argparse.ArgumentParser(description='Generate a maze and save it to a file')
    parser.add_argument('rows', type=int, help='Number of rows in the maze')
    parser.add_argument('cols', type=int, help='Number of columns in the maze')
    parser.add_argument('output_file', type=str, \
                    help='Output file to save the maze (e.g., maze.txt)')
    args = parser.parse_args()

    generate_maze(args.rows, args.cols, args.output_file)
    print(f"Maze generated and saved to {args.output_file}")

if __name__ == "__main__":
    main()
