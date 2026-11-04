from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    new_path = path + [neighbour]
                    queue.append(new_path)

    return None


# Graph representing rooms in a building
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

result = bfs(graph, start, goal)

if result:
    print("BFS Traversal Path:", " -> ".join(result))
    print("Shortest Path:", len(result) - 1, "edges")
else:
    print("Goal not found")
