from algorithm_practice.binary_trees.tree_node import TreeNode
from collections import deque

class Tree:
    def __init__(self, node=None):
        self.root = node 

    #Define base case
    def find_helper(self, current, value):
        # base case1: when we find the value 
        # base case2: when we get to the leaf node and still didn't find the value means the value doesn't exist 
        if not current:
            return None

        if current.value == value:
            return current

        if value < current.value: 
            current = self.find_helper(current.left , value) 
        else:
            current = self.find_helper(current.right , value) 

        return current

    def find_recursive(self, value):
        if not self.root:
            return None 
        return self.find_helper(self.root, value)

        
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

    def get_height(self):
        return self.height_recursive(self.root,0)

    def height_recursive(self, current_node, height):
        if not current_node:
            return height

        height += 1
        max_height_left = self.height_recursive(current_node.left, height)
        max_height_right = self.height_recursive(current_node.right, height)

        if max_height_left > max_height_right:
            return max_height_left
        
        return max_height_right
    
    def findLesserNode(self, node):
        if not node:
            return None
        
        while current.left:
            current = current.left

        return current
    
    def delete_rec(self, current, key):
        if not current:
            return None
        
        if current.key < key:
            current.right = self.delete_rec(current.right, key)

        if current and current.key > key:
            current.left = self.delete_rec(current.left, key)
        
        if current and current.key == key:
            if not current.left:
                return current.right
            if not current.right:
                return current.left
            #there were nodes in both sides
            lesser = current.right
            while lesser.left:
                lesser = lesser.left
            current.key = lesser.key
            current.value = lesser.value
            current.right = self.delete_rec(current.right, current.key) 
        
        return current

    def delete(self, key):
        if not self.root:
            return
        
        self.root = self.delete_rec(self.root, key)

    @staticmethod
    def is_BST(root):
        if not root:
            return True
    
        if root.left:
            if root.left.key > root.key:
                return False

        if root.right:
            if root.right.key < root.key:
                return False
            
        return Tree.is_BST(root.left) and Tree.is_BST(root.right)

    def is_balanced_rec(self, root):
        if not root:
            return True

        left_height = self.height_recursive(self.root.left,1)
        right_height = self.height_recursive(self.root.right,1)

        if abs(left_height-right_height) > 1:
            return False
        
        left_subtree = self.is_balanced_rec(root.left)
        right_subtree = self.is_balanced_rec(root.left)
        
        return left_subtree and right_subtree
    
    def is_balanced(self):
        if not self.root:
            return True
        
        return self.is_balanced_rec(self.root)


    #[5, 10, 15, 20, 25, 30, 35, 40, 45]
def arr_to_bst_rec(arr, start, end, tree):
    if end == -1 or end <= start:
        return
    
    half = (start + end) // 2
    tree.add(arr[half])
    arr_to_bst_rec(arr, start, half-1, tree)
    arr_to_bst_rec(arr,half+1, end, tree)

def arr_to_bst(arr):
    if not arr:
        return None
        
    new_tree = Tree()

    arr_to_bst_rec(arr,0,len(arr),new_tree)
    return new_tree


