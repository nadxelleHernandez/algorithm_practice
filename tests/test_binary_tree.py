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

def test_inorder_function():
    tree = Tree()
    tree.add(17)
    tree.add(14)
    tree.add(20)
    tree.add(19)
    tree.add(52)

    nodes = tree.inorder()

    assert len(nodes) == 5
    assert nodes == [14,17,19,20,52]

def test_postorder_function():
    tree = Tree()
    tree.add(17)
    tree.add(14)
    tree.add(20)
    tree.add(19)
    tree.add(52)

    nodes = tree.postorder()

    assert len(nodes) == 5
    assert nodes == [14,19,52,20,17]

def test_preorder_function():
    tree = Tree()
    tree.add(17)
    tree.add(14)
    tree.add(20)
    tree.add(19)
    tree.add(52)

    nodes = tree.preorder()

    assert len(nodes) == 5
    assert nodes == [17,14,20,19,52]


