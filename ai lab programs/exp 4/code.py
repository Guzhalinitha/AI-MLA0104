import heapq

def best_first_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start)]
    visited = set()
    parent = {start: None}

    while priority_queue:
        h, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]

            return path[::-1]

        for neighbour in graph[node]:
            if neighbour not in visited:
                parent[neighbour] = node
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbour], neighbour)
                )

    return None


# Graph representing cities
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Estimated distance to destination G
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 3,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

result = best_first_search(graph, heuristic, start, goal)

if result:
    print("Best First Search Path:", " -> ".join(result))
else:
    print("Path not found")
