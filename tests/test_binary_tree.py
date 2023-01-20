from algorithm_practice.binary_trees.tree import Tree
from algorithm_practice.binary_trees.tree_node import TreeNode

def test_add_node_one_node_tree():
    root = TreeNode(3)
    tree = Tree(root)

    tree.add(4)

    assert tree.find(4)

def test_add_node_empty_tree():
    tree = Tree()
    tree.add(1)

    assert tree.find(1)

