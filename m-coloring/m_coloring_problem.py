'''M-coloring problem'''

import networkx as nx
import matplotlib.pyplot as plt

# Given an undirected graph and a number m, the task is to color
# the given graph with at most m colors such that no two adjacent
# verticles of the graph are colored with the same color.

class Graph():
    '''Graph class'''
    def __init__(self, verticles):
        '''Initializes the graph with the number of verticles and an adjacency matrix.'''
        self.verticles = verticles
        self.graph = [[0 for _ in range(verticles)] for _ in range(verticles)]

    def verify_input(self, v, y, m):
        '''Verifies the input.'''
        if not v.isdigit():
            print('The number of verticles must be an integer!')
            return False
        if int(v) <= 0:
            print('The number of verticles must be a positive integer!')
            return False
        if not m.isdigit():
            print('The number of colours must be an integer!')
            return False
        if int(m) <= 0:
            print('The number of colours must be a positive integer!')
            return False
        if int(m) > int(v):
            print('The number of colours must be less \
or equal to the number of verticles!')
            return False
        y = y.split()
        if len(y) != int(v):
            print('The adjacency matrix must have the same number \
of rows as the number of verticles!')
            return False
        for el in y:
            if len(el) != int(v):
                print('The adjacency matrix must have the same number \
of columns as the number of verticles!')
                return False
            for c in el:
                if c not in ['0', '1']:
                    print('The adjacency matrix must contain only 0s and 1s!')
                    return False
        return True

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

    def visualize_graph(self, colour):
        '''Visualizes the graph with assigned colours.'''
        g = nx.Graph()
        for i in range(self.verticles):
            for j in range(i+1, self.verticles):
                if self.graph[i][j] == 1:
                    g.add_edge(i, j)

        pos = nx.spring_layout(g)
        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_edges(g, pos)
        nx.draw_networkx_labels(g, pos)

        color_map = []
        with open('palette.txt', 'r', encoding='utf-8') as f:
            custom_palette = f.read().split('\n')
        for c in colour:
            if c == 0:
                color_map.append('gray')
            else:
                color_map.append(custom_palette[c % len(custom_palette)])
        nx.draw_networkx_nodes(g, pos, node_color=color_map)

        plt.axis("off")
        plt.show()

def main():
    '''Main function'''
    v = input('Enter the number of verticles: ')
    y = input("Enter the adjacency matrix \n(eg. '0111 1010 1101 1010'): ")
    m = input('Enter the number of colours: ')
    g = Graph(int(v))
    if not g.verify_input(v, y, m):
        return
    m = int(m)
    y = y.split()
    for i, el in enumerate(y):
        g.graph[i] = list(map(int, el))
    print('The graph is: ')
    for i in range(g.verticles):
        print(g.graph[i])
    colours = g.graph_colouring(m)
    for c in colours:
        print(c, end=' ')
    if colours != 'Solution does not exist! \nNo colours are assigned.':
        g.visualize_graph(colours)

main()
