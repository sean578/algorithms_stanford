import random
import copy
import matplotlib.pyplot as plt


def get_graph(file):
    al = {}
    for line in file.readlines():
        line = [int(i) for i in line.strip('\n').split()]
        al[line[0]] = line[1:]
    return al


def get_test_graph():
    graph = {}
    graph['A'] = ['C', 'D']
    graph['B'] = ['D']
    graph['C'] = ['A', 'D']
    graph['D'] = ['A', 'B', 'C']
    return graph


def get_test_graph_2():
    graph = {}
    graph[0] = [2, 3, 1]
    graph[1] = [0, 2, 3]
    graph[2] = [0, 1]
    graph[3] = [0, 1]
    return graph


def contraction(graph, edge, new_vertex_name):

    # 1. remove the edge from both nodes
    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])

    # 2. combine the nodes
    graph[new_vertex_name] = graph[edge[0]] + graph[edge[1]]
    del graph[edge[0]]
    del graph[edge[1]]

    # 3. replace all occurances of old node names with new
    for key, value in graph.items():
        if edge[0] in value:
            for i, v in enumerate(value):
                if v == edge[0]:
                    value[i] = new_vertex_name
        if edge[1] in value:
            for i, v in enumerate(value):
                if v == edge[1]:
                    value[i] = new_vertex_name

    # 4. remove any self loops
    graph[new_vertex_name] = list(filter(lambda i: i != new_vertex_name, graph[new_vertex_name]))

    # 4. return updated graph
    return graph


def print_graph(title, graph):
    print(title)
    for key, value in graph.items():
        print(key, value)


def generate_new_vertex(graph, seed):

    random.seed(seed)

    # first choose a random vertex
    vertex_1 = list(graph.keys())[random.randrange(len(list(graph.keys())))]

    # now choose a random attached vertex
    vertex_2 = graph[vertex_1][random.randrange(len(graph[vertex_1]))]

    return vertex_1, vertex_2


def algorithm_step(graph, seed, new_vertex_name):
    edge = generate_new_vertex(graph, seed)
    graph = contraction(graph, edge, new_vertex_name)
    seed += 1
    return graph, seed


def full_contract(graph, seed, new_vertex_name):
    while len(graph.keys()) > 2:
        graph, new_vertex = algorithm_step(graph, seed, new_vertex_name)
        new_vertex_name += 1

    # get number of cuts
    return len(list(graph.values())[0])


if __name__ == '__main__':
    file = open('data/course_1_assignment_4.txt')
    graph_orig = get_graph(file)

    # graph_orig = get_test_graph_2()
    # print_graph('Initial', graph_orig)

    num_repeats = 1000

    num_cuts_all = []
    new_vertex_name = 201
    for initial_seed in range(num_repeats):
        graph = copy.deepcopy(graph_orig)
        num_cuts = full_contract(graph, initial_seed, new_vertex_name)
        num_cuts_all.append(num_cuts)

    print('Minimium number of cuts', min(num_cuts_all))
    plt.hist(num_cuts_all, bins=20)
    plt.show()