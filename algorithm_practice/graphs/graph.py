from collections import deque

class Graph:
    
    # The graph is stored in an adjacency dictionary where each key 
    # represents a node in the graph and each value in the dictionary
    # represents the corresponding key's list of edges
    def __init__(self, adjacency_dict = {}):
        self.adjacency_dict = adjacency_dict

    def bfs(self):
        if not self.adjacency_dict:
            return []

        start_node = list(self.adjacency_dict.keys())[0]
        queue = deque()
        visited = []
        queue.append(start_node)
        visited.append(start_node)
        while queue:
            current = queue.popleft()
            neighbors = self.adjacency_dict[current]
            for node in neighbors:
                if node not in visited:
                    visited.append(node)
                    queue.append(node)

        return visited

    def dfs(self):
        if not self.adjacency_dict:
            return []

        start_node = list(self.adjacency_dict.keys())[0]
        visited = []
        self.dfs_recursive_call(visited,start_node)
        return visited

    def dfs_recursive_call(self, visited, node):
        if node not in visited:
            visited.append(node)
            for neigbor in self.adjacency_dict[node]:
                self.dfs_recursive_call(visited,neigbor)



    def dfs_i(self):
        if not self.adjacency_dict:
            return []

        start_node = list(self.adjacency_dict.keys())[0]
        stack = deque()
        visited = []
        stack.append(start_node)
        while stack:
            current = stack.pop()
            visited.append(current)
            for node in self.adjacency_dict[current]:
                if node not in visited:
                    stack.append(node)

        return visited

