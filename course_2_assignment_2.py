def load_graph(filehandle):
    graph = {}
    for line in filehandle.readlines():
        line = line.strip('\n').split()
        split = [l.split(',') for l in line[1:]]
        graph[int(line[0])] = [(int(u), int(v)) for u, v in split]
    return graph


def print_graph(graph):
    for vertex, edges in graph.items():
        print(vertex, edges)


def dijkstra(graph, source, num_verticies, infinity):
    """ Dijkstra's shortest-path algorithm """

    processed_vertices = {source}
    shortest_path = [infinity] * num_verticies
    shortest_path[source] = 0

    while len(processed_vertices) < (num_verticies - 1):

        # pick edge in frontier which minimises len[v] + length
        weight_next = infinity
        for v in processed_vertices:
            for vertex_weight in graph[v]:
                if vertex_weight[0] not in processed_vertices:
                    if (shortest_path[v] + vertex_weight[1]) < weight_next:
                        weight_next = shortest_path[v] + vertex_weight[1]
                        vertex_start = v
                        vertex_next = vertex_weight[0]

        shortest_path[vertex_next] = weight_next
        processed_vertices.add(vertex_next)
    print(processed_vertices)
    return shortest_path


if __name__ == '__main__':
    filehandle = open('data/course_2_assignment_2.txt')
    graph = load_graph(filehandle)
    # print_graph(graph)

    source = 1
    infinity = 1000000
    num_verticies = 201

    shortest_path = dijkstra(graph, source, num_verticies, infinity)
    print(shortest_path)
    # distances required to nodes:
    distances = []
    for node in (7,37,59,82,99,115,133,165,188,197):
        distances.append(shortest_path[node])
    answer = ''
    for d in distances:
        answer += str(d)
        answer += ','
    print('Answer', answer)