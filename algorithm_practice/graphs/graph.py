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

    def bfs_with_tracker(self, start_node, visited_dict):
        queue = deque()
        visited = []
        queue.append(start_node)
        visited.append(start_node)
        visited_dict[start_node]= True
        while queue:
            current = queue.popleft()
            neighbors = self.adjacency_dict[current]
            for node in neighbors:
                if visited_dict.get(node) is None:
                    visited.append(node)
                    visited_dict[node] = True
                    queue.append(node)

        return visited

    def components(self):
        if not self.adjacency_dict:
            return []

        components_list = []
        visited_dict = {}
        for key_node in self.adjacency_dict:
            if visited_dict.get(key_node) is None:
                visited = self.bfs_with_tracker(key_node,visited_dict)
                components_list.append(visited)

        return components_list

