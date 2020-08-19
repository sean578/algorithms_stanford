from collections import defaultdict


def load_graph_and_reversed(file_handle):
    graph = defaultdict(list)
    graph_r = defaultdict(list)
    for line in file_handle.readlines():
        u, v = line.strip('\n').split()
        graph[int(u)].append(int(v))
        graph_r[int(v)].append(int(u))
    return graph, graph_r


def load_test_graph():
    graph = defaultdict(list)

    graph[1].extend([7])
    graph[2].extend([5])
    graph[3].extend([9])
    graph[4].extend([1])
    graph[5].extend([8])
    graph[6].extend([3, 8])
    graph[7].extend([9, 4])
    graph[8].extend([2])
    graph[9].extend([6])

    return graph


def print_graph(name, graph):
    print(name)
    for u, v in graph.items():
        print(u, v)


def dfs_iterative(graph, vertex, seen):
    stack = []
    f = []
    stack.append(vertex)

    while stack:
        print('stack ===================================', stack)
        v = stack.pop()
        print('popped', v)
        if seen[v] == 0:
            seen[v] = 1
            f = [v] + f
            for n in graph[v]:
                if seen[n] == 0:
                    stack.append(n)

    return seen, f


if __name__ == '__main__':
    # file_handle = open('data/course_2_assignment_1.txt')
    # graph, graph_r = load_graph_and_reversed(file_handle)

    graph_r = load_test_graph()
    # print_graph('forwards', graph)
    print_graph('reverse', graph_r)

    num_verticies = 9  # 875715
    seen = [0] * (num_verticies + 1)

    all_finish_number = []
    for v in range(9, 0, -1):
        if seen[v] == 0:
            print('Starting dfs at vertex', v)
            seen, f = dfs_iterative(graph_r, v, seen)
            all_finish_number += f
    print('finish number', all_finish_number)

    # if len(finish_number) > len(set(finish_number)):
    #     raise ValueError('Finish numbers not unique')

    # find 'finishing times, t' - when recursion has to back up f(vertex) = t (then increment t)
    # t=0,

    # run DFS on graph
    # outer loop over all nodes (run if haven't seen - keep track), do from vertex with t = n to 1
    # s=None (current source vertex - leader) - put into a set
