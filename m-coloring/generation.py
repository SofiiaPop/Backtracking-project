'''Generates a random adjacency matrix'''

import random

def generate_adjacency_matrix():
    '''Generates a random adjacency matrix for a graph'''
    num_nodes = random.randint(2, 20)
    num_edges = random.randint(1, num_nodes * (num_nodes - 1) // 2)

    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    edges_generated = 0
    while edges_generated < num_edges:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)

        if node1 != node2 and adjacency_matrix[node1][node2] == 0:
            adjacency_matrix[node1][node2] = 1
            adjacency_matrix[node2][node1] = 1
            edges_generated += 1

    return adjacency_matrix
