from algorithm_practice.binary_trees.tree import Tree
from algorithm_practice.binary_trees.tree_node import TreeNode

def test_find_node_recursively():
    tree = Tree()
    tree.add(17)
    tree.add(14)
    tree.add(20)
    tree.add(19)
    tree.add(52)

    node = tree.find_recursive(19)

    assert node.value == 19

def test_find_node_recursively_not_there():
    tree = Tree()
    tree.add(17)
    tree.add(14)
    tree.add(20)
    tree.add(19)
    tree.add(52)

    node = tree.find_recursive(11)

    assert node == None

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

def test_height_more_than_one_node():
    tree = Tree()
    tree.add(22)
    tree.add(10)
    tree.add(6)
    tree.add(3)
    tree.add(8)
    tree.add(12)
    tree.add(43)
    tree.add(38)
    tree.add(55)

    height = tree.get_height()

    assert height == 4

def test_delete_node_leaf():
    tree = Tree()
    tree.add(17)
    tree.add(14)
    tree.add(20)
    tree.add(19)
    tree.add(52)

    tree.delete(52)

    assert tree.inorder() == [14,17,19,20]

def test_delete_node_no_leaf():
    tree = Tree()
    tree.add(17)
    tree.add(14)
    tree.add(20)
    tree.add(19)
    tree.add(52)

    tree.delete(20)

    assert tree.inorder() == [14,17,19,52]

def test_delete_node_single_element_tree():
    tree = Tree()
    tree.add(17)

    tree.delete(17)

    assert tree.inorder() == []


