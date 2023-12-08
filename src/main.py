import sys


def dijkstra(graph, start_vertex):
    visited = {start_vertex: 0}
    path = {}

    nodes = set(graph.keys())

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for line in graph[min_node]:
            weight = current_weight + graph[min_node][line]
            if line not in visited or weight < visited[line]:
                visited[line] = weight
                path[line] = min_node

    return visited, path


def server_place(graph, clients):
    max_latency = sys.maxsize
    server = None

    for node in graph:
        if node not in clients:
            latencies = dijkstra(graph, node)[0]
            current_max_latency = max(latencies[client] for client in clients)
            if current_max_latency < max_latency:
                max_latency = current_max_latency
                server = node

    return server, max_latency


def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().split())
        clients = set(file.readline().split())
        graph = {str(i): {} for i in range(1, n+1)}
        for _ in range(m):
            start, end, latency = file.readline().split()
            graph[start][end] = int(latency)
            graph[end][start] = int(latency)
    return graph, clients


def write_result_to_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


graph, clients = read_graph_from_file('gamsrv.in')

server, max_latency = server_place(graph, clients)

write_result_to_file('gamsrv.out', max_latency)

print(f"Server: {server}, max latency: {max_latency} ms")
