def dfs(graph, root, visited=[]):
    if root not in visited:
        visited.append(root)
        print(visited)
        if root not in graph:
            return visited
        for nb in graph[root]:
            print(graph[root])
            visited = dfs(graph, nb, visited)          
    return visited


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]} 
dfs(graph, 0)
