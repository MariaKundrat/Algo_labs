import unittest
from main import server_place

class TestServerPlacement(unittest.TestCase):

    def test_example_1(self):
        input_data = (
            "9 12\n"
            "2 4 6\n"
            "1 2 20\n"
            "2 3 20\n"
            "3 6 20\n"
            "6 9 20\n"
            "9 8 20\n"
            "8 7 20\n"
            "7 4 20\n"
            "4 1 20\n"
            "5 2 10\n"
            "5 4 10\n"
            "5 6 10\n"
            "5 8 10\n"
        )
        expected_output = 10

        self.run_test(input_data, expected_output)

    def test_example_2(self):
        input_data = (
            "3 2\n"
            "1 3\n"
            "1 2 50\n"
            "2 3 1000000000\n"
        )
        expected_output = 1000000000

        self.run_test(input_data, expected_output)

    def run_test(self, input_data, expected_output):
        with self.subTest():
            graph, clients = read_graph_from_string(input_data)
            result = server_place(graph, clients)[1]
            self.assertEqual(result, expected_output)


def read_graph_from_string(input_data):
    lines = input_data.split('\n')
    n, m = map(int, lines[0].split())
    clients = set(lines[1].split())
    graph = {str(i): {} for i in range(1, n+1)}
    for line in lines[2:]:
        if line:
            start, end, latency = line.split()
            graph[start][end] = int(latency)
            graph[end][start] = int(latency)
    return graph, clients


if __name__ == '__main__':
    unittest.main()
