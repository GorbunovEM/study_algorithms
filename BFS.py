import collections
def bfs(graph, root): 
    visited = set()
    queue = collections.deque([root])
    visited.add(root)    
    while queue: 
        node = queue.popleft()
        for nb in graph[node]: 
            if nb not in visited: 
                visited.add(nb) 
                queue.append(nb) 
        
graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]} 
bfs(graph, 0)
