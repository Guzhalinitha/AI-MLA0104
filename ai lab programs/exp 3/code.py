import heapq

def ucs(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + weight, neighbour, path)
                )

    return None, None


# Graph representing transportation routes
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 3)],
    'G': []
}

start = 'A'
goal = 'G'

cost, path = ucs(graph, start, goal)

if path:
    print("Least Cost Path:", " -> ".join(path))
    print("Total Transportation Cost:", cost)
else:
    print("No path found")
