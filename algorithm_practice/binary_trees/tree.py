from algorithm_practice.binary_trees.tree_node import TreeNode
from collections import deque

class Tree:
    def __init__(self, node=None):
        self.root = node 

    #Look for a node iterative way
    def find(self, key):  
        current = self.root
        while current is not None:
            if current.key == key:
                break
            if key < current.key:
                #Search on the left
                current = current.left
            elif key > current.key:
                #Search on the right
                current = current.right 
        
        if current:
            return current.value
        else:
            return None

    def add_recursive(self, root, key, value):
        if not root:
            return

        if key == root.key:
            node = TreeNode(key,value)
            if root.right is not None:
                right = root.right
                root.right = node
                node.right = right
            else:
                root.right = node
            return

        if key < root.key:
            if not root.left:
                root.left = TreeNode(key,value)
                return
            self.add_recursive(root.left,key,value)

        else:
            if not root.right:
                root.right = TreeNode(key,value)
                return
            self.add_recursive(root.right,key,value)


    def add_rec(self, key, value = None):
        if not self.root:
            self.root = TreeNode(key,value)
            return

        self.add_recursive(self.root, key, value)
    
    
    def add(self, key, value = None):
        node = TreeNode(key,value)

        if not self.root:
            self.root = node
            return

        current = self.root
        while current is not None:
            if current.key == node.key:
                #add to the right
                if current.right is not None:
                    right = current.right
                    current.right = node
                    node.right = right
                else:
                    current.right = node
                break
            if node.key < current.key:
                #Go left
                if current.left is None:
                    #we arrived to a leaf, we can add
                    current.left = node
                    break
                current = current.left
            else:
                #Go right
                if current.right is None:
                    #We arrived to a leaf, we can add
                    current.right = node
                    break
                current = current.right

    def bfs(self):
        nodes = []
        if not self.root:
            return nodes

        queue = deque()
        queue.append(self.root)
        while queue:
            current = queue.popleft()
            nodes.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return nodes

    def preorder_recursive(self, current_node, visited_list):
        if not current_node:
            return visited_list

        visited_list.append(current_node.value)
        self.preorder_recursive(current_node.left, visited_list)
        self.preorder_recursive(current_node.right, visited_list)

    def preorder(self):
        nodes = []
        self.preorder_recursive(self.root, nodes)
        return nodes

    def inorder_recursive(self, current_node, visited_list):
        if not current_node:
            return visited_list

        self.inorder_recursive(current_node.left, visited_list)
        visited_list.append(current_node.value)
        self.inorder_recursive(current_node.right,visited_list)


    def inorder(self):
        nodes = []
        self.inorder_recursive(self.root, nodes)
        return nodes

    def postorder_recursive(self, current_node, visited_list):
        if not current_node:
            return visited_list

        self.postorder_recursive(current_node.left, visited_list)
        self.postorder_recursive(current_node.right, visited_list)
        visited_list.append(current_node.value)

    def postorder(self):
        nodes = []
        self.postorder_recursive(self.root, nodes)
        return nodes



