'''M-coloring problem'''

import pygame
import numpy as np
from generation_matrix import generate_adjacency_matrix

with open('palette.txt', 'r', encoding='utf-8') as file:
    NODE_COLORS = [line.strip() for line in file]

# Given an undirected graph and a number m, the task is to color
# the given graph with at most m colors such that no two adjacent
# verticles of the graph are colored with the same color.

class Graph():
    '''Graph class'''
    def __init__(self, graph=None):
        '''Initializes the graph with the number of verticles and an adjacency matrix.'''
        if graph is not None:
            self.graph = graph
        else:
            self.graph = generate_adjacency_matrix()
        self.verticles = len(self.graph)

    def is_safe(self, v, colour, c):
        '''Checks if the colour c can be assigned to the vertice.'''
        for i in range(self.verticles):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graph_colouring_util(self, m, colour, v):
        '''Function to solve if it is possible to colour the graph with m colours.'''
        if v == self.verticles:
            return True

        for c in range(1, m+1):
            if self.is_safe(v, colour, c):
                colour[v] = c
                if self.graph_colouring_util(m, colour, v+1):
                    return True
                colour[v] = 0

    def graph_colouring(self, m):
        '''Searches for the solution of the graph colouring problem.'''
        colour = [0] * self.verticles

        if not self.graph_colouring_util(m, colour, 0):
            return 'Solution does not exist! \nNo colours are assigned.'

        print('Solution exists! The colours assigned to the verticles are: ')
        return colour

    def visualize_graph(self, colors):
        '''Visualizes the graph with assigned colors using Pygame.'''
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        font = pygame.font.SysFont(None, 20)

        node_positions = {}
        for i in range(self.verticles):
            angle = i * (2 * np.pi / self.verticles)
            x = int(800 / 2 + 200 * np.cos(angle))
            y = int(600 / 2 + 200 * np.sin(angle))
            node_positions[i] = (x, y)

        for i in range(self.verticles):
            for j in range(i+1, self.verticles):
                if self.graph[i][j] == 1:
                    pygame.draw.line(screen, (255, 255, 255), node_positions[i], node_positions[j], 2)

        for i in range(self.verticles):
            pygame.draw.circle(screen, NODE_COLORS[colors[i] - 1], node_positions[i], 20)
            text = font.render(str(i), True, (0, 0, 0))
            text_rect = text.get_rect(center=node_positions[i])
            screen.blit(text, text_rect)

        pygame.display.flip()
        pygame.time.delay(1000)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

def main():
    '''Main function'''
    g = Graph()
    print('The graph is: ')
    for i in range(g.verticles):
        print(g.graph[i])
    m = int(input('Enter the number of colours: '))
    colours = g.graph_colouring(m)
    for c in colours:
        print(c, end=' ')
    if colours != 'Solution does not exist! \nNo colours are assigned.':
        g.visualize_graph(colours)

# with open('matrix_1.txt', 'r', encoding='utf-8') as file:
#     matrix = [[int(num.rstrip(',')) for num in line.split()] for line in file]

if __name__ == '__main__':
    main()
