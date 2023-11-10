from queue import Queue

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]


def generate_possible_moves(current_pos, size):
    possible_moves = []
    for i in range(8):
        new_pos = (current_pos[0] + row[i], current_pos[1] + col[i])
        if (0 <= new_pos[0] < size) and (0 <= new_pos[1] < size):
            possible_moves.append(new_pos)
    return possible_moves


def build_graph(size: int, start: tuple, end: tuple):
    global graph
    graph = {start: []}
    queue = Queue()
    queue.put(start)
    visited = set()

    while not queue.empty():
        current_pos = queue.get()

        for new_pos in generate_possible_moves(current_pos, size):
            if new_pos not in visited:
                graph[current_pos].append(new_pos)
                if new_pos not in graph:
                    graph[new_pos] = []
                queue.put(new_pos)
                visited.add(new_pos)
                if new_pos == end:
                    return graph


def min_distance(graph, start, end) -> int:
    if start not in graph.keys() or end not in graph.keys():
        return -1

    visited = set()
    queue = Queue()
    queue.put((start, 0, [start]))
    moves = 0

    while not queue.empty():
        current_pos, depth, path = queue.get()
        visited.add(current_pos)

        for neighbor in graph[current_pos]:
            if neighbor not in visited:
                if neighbor == end:
                    path.append(neighbor)
                    print("General:", moves)
                    print("Coordinates:", path)
                    return depth + 1
                queue.put((neighbor, depth + 1, path + [neighbor]))
                moves += 1

    return 0


if __name__ == '__main__':
    with open("input.txt", "r") as file:
        size_of_desk = int(file.readline())
        start_point = eval(file.readline())
        end_point = eval(file.readline())

    graph = build_graph(size_of_desk, start_point, end_point)
    min_dist = min_distance(graph, start_point, end_point)
    print("Minimum:", min_dist)

    with open("output.txt", "w") as f:
        f.write(str(min_dist))
