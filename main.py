class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


    def __str__(self):
        return f'BinaryTree: {self.value}, {self.left}, {self.right}, {self.parent}'


def find_func(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node and node.right:
        return get_right_child(node.right, node.value)
    else:
        return get_left_child(node, node.value)


def get_right_child(node: BinaryTree, target_value) -> BinaryTree:
    current_node = node
    while current_node:
        if current_node.value > target_value:
            return current_node
        current_node = current_node.right
    return None


def get_left_child(node: BinaryTree, target_value) -> BinaryTree:
    current_node = node
    while current_node.parent:
        if current_node.parent.value > target_value:
            return current_node.parent
        current_node = current_node.parent
    return None
