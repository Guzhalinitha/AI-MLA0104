import heapq

def astar(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return g, path

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbour,
                     path + [neighbour])
                )

    return None, None


# Graph with travel costs
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 3)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

cost, path = astar(graph, heuristic, start, goal)

if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Travel Cost:", cost)
else:
    print("Path not found")
