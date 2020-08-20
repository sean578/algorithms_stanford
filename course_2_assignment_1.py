from collections import defaultdict, Counter, deque


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

    graph[1].extend([4])
    graph[2].extend([8])
    graph[3].extend([6])
    graph[4].extend([7])
    graph[5].extend([2])
    graph[6].extend([9])
    graph[7].extend([1])
    graph[8].extend([5, 6])
    graph[9].extend([7, 3])

    return graph


def load_test_graph_reversed():
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
    stack = deque()
    stack.append(vertex)
    f = deque()

    while stack:
        v = stack.pop()
        if seen[v] == 0:
            print('visiting', v)
            seen[v] = 1
            print('appending', v)
            f.append(v)
            for n in graph[v]:
                if seen[n] == 0:
                    stack.append(n)

    return seen, f


def dfs_iterative_forward(graph, vertex, seen, groups):

    stack = []
    stack.append(vertex)

    while stack:
        v = stack.pop()
        # attach to group given by initial vertex
        groups[v] = vertex
        if seen[v] == 0:
            seen[v] = 1
            for n in graph[v]:
                if seen[n] == 0:
                    stack.append(n)

    return seen, groups


if __name__ == '__main__':
    print('---------------------Loading graph------------------------')
    file_handle = open('data/test_5.txt')
    graph, graph_r = load_graph_and_reversed(file_handle)

    # graph = load_test_graph()
    # graph_r = load_test_graph_reversed()

    num_verticies = 12
    print_graph('forward', graph)
    print_graph('reverse', graph_r)

    print('--------------------Reverse pass of graph--------------------')
    seen = [0] * (num_verticies + 1)
    order = deque()
    for v in range(num_verticies, 0, -1):
        print('Starting from node', v)
        if seen[v] == 0:
            seen, f = dfs_iterative(graph_r, v, seen)
            order.appendleft(f)

    print('--------------------Forward pass of graph----------------------')
    seen = [0] * (num_verticies + 1)
    groups = [0] * (num_verticies + 1)
    # for i in range(1, len(finish_number)+1):
    for g in order:
        for v in g:
            print(v)
            # v = finish_number.index(i) + 1
            if seen[v] == 0:
                seen, groups = dfs_iterative_forward(graph, v, seen, groups)

    print('--------------------Get group sizes----------------------')
    print('Counting up group sizes')
    counter = Counter(groups[1:])
    print(counter.most_common(5))