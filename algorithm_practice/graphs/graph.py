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
    
def create_color_dictionary(elements):
    '''Creates a dictionary with the elements of the graph asigned to a non changed status
    '''
    if not elements:
        return []
    
    colors = {}
    for key in elements:
        colors[key] = -1

    return colors

def possible_bipartition(graph):
    if not graph:
        return True
    
    queue = []
    color_dict = create_color_dictionary(graph.keys())
    elements = list(graph.keys())
    current = elements[0]
    color_dict[current] = 1
    queue.append(current)

    while queue or elements:
        if not queue and elements:
            current = elements[0]
            queue.append(current)
            color_dict[current] = 1
        current = queue.pop(0)
        for sibling in graph[current]:
            if color_dict[sibling] == -1: #it hasn't been updated
                queue.append(sibling)
                if color_dict[current] == 1:
                    color_dict[sibling] = 2
                else:
                    color_dict[sibling] = 1
            elif color_dict[sibling] == color_dict[current]:
                return False  
        elements.remove(current)  
    return True



def numIslands(grid: list[list[str]]) -> int:
    '''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
    return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.

        Example 1:

        Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]
        Output: 1
        Example 2:

        Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
        Output: 3
        

        Constraints:

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'.'''
    if not grid:
        return 0

    num_islands = 0
    m = len(grid)
    n = len(grid[0])
    visited = [[0 for x in range(n)] for m in range(m)]
    stack = [] 

    #first we are going to go throght the matrix as if is a graph. We visit each position, if it is a one we added to the queue
    #if it is a zero we just marked it as visited.
    #this will give us a matrix with all the conected nodes. When the queue is done, we found the whole island
    #we continue to look into the visited matrix until we found another 1 that hasn't been visited. That will be another island to traverse as a matrix
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]: ## we start the graph
                stack.append((i,j))
                while stack:
                    island_i, island_j = stack.pop()
                    if island_i >= m or island_i <0  or island_j >= n or island_j <0 or visited[island_i][island_j] or grid[island_i][island_j]=='0':
                        continue
                    visited[island_i][island_j] = 1
                    stack.append((island_i+1,island_j))
                    stack.append((island_i-1,island_j))
                    stack.append((island_i,island_j+1))
                    stack.append((island_i,island_j-1))
                num_islands += 1
                        
    return num_islands