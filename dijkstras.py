# Takes a adjacency list command line argument
# and runs Dijkstra's algorithm on the first node

import sys

def dijkstras(graph):
    visited = {1}
    path_lengths = [1000000] * (len(graph) + 1)
    path_lengths[1] = 0

    while len(visited) != len(graph):
        min_edge = None
        min_distance = 1000000
        for vertex in visited:
            for edge in graph[vertex]:
                if edge[0] not in visited:
                    criterion = path_lengths[vertex] + edge[1]
                    if criterion < min_distance:
                        min_edge = edge
                        min_distance = criterion
        visited.add(min_edge[0])
        path_lengths[min_edge[0]] = min_distance

    print(",".join(str(length) for length in path_lengths[1:]))

def main():
    with open(sys.argv[1], 'r') as file:
        data = file.readlines()
        graph_as_array = [i.strip().split() for i in data]

    graph_as_dict = {}

    for line in graph_as_array:
        vertex = int(line[0])
        edges = [line[i].split(",") for i in range(1, len(line))]

        graph_as_dict[vertex] = []

        for edge in edges:
            edge_as_tuple = (int(edge[0]), int(edge[1]))
            graph_as_dict[vertex].append(edge_as_tuple)

    dijkstras(graph_as_dict)

main()