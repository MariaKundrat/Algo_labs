from main import BinaryTree, find_func
import unittest


class TestBinaryTree(unittest.TestCase):
    def test_find_successor(self):
        root = BinaryTree(10)

        root.left = BinaryTree(5)
        root.left.parent = root

        root.left.left = BinaryTree(3)
        root.left.left.parent = root.left

        root.left.right = BinaryTree(7)
        root.left.right.parent = root.left

        root.right = BinaryTree(15)
        root.right.parent = root

        root.right.right = BinaryTree(20)
        root.right.right.parent = root.right

        root.right.right.left = BinaryTree(23)
        root.right.right.left.parent = root.right.right

        value_to_find = 23
        node_to_find = self.find_node_with_value(root, value_to_find)

        if node_to_find is not None:
            successor = find_func(root, node_to_find)
            if successor:
                print("Next: " + str(successor.value))
            else:
                print("No next")
        else:
            print(f"Value {value_to_find} not found in the tree.")

    def find_node_with_value(self, root, value):
        stack = []
        stack.append(root)
        while stack:
            current_node = stack.pop()
            if current_node.value == value:
                return current_node
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)


if __name__ == '__main__':
    unittest.main()
