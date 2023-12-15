import unittest
from Algo_labs.src.main import createStateMachine, findNeedle


class TestNeedleSearch(unittest.TestCase):

    def test_create_state_machine(self):
        needle = "abc"
        transitions = createStateMachine(needle)
        expected_transitions = [
            {'a': 1, 'b': 0, 'c': 0},
            {'a': 1, 'b': 2, 'c': 0},
            {'a': 1, 'b': 0, 'c': 3},
            {'a': 1, 'b': 0, 'c': 0}
        ]
        self.assertEqual(transitions, expected_transitions)

    def test_find_needle(self):
        haystack = " the apple the mouse"
        needle = "the"
        result = findNeedle(haystack, needle)
        expected_result = [0, 32]
        self.assertEqual(result, expected_result)

        haystack = " the apple the mouse"
        needle = "cat"
        result = findNeedle(haystack, needle)
        expected_result = -1
        self.assertEqual(result, expected_result)

        haystack = ""
        needle = "abc"
        result = findNeedle(haystack, needle)
        expected_result = -1
        self.assertEqual(result, expected_result)

        haystack = ""
        needle = ""
        result = findNeedle(haystack, needle)
        expected_result = -1
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
