import heapq

def ucs(network, origin, target):
    queue = []
    heapq.heappush(queue, (0, origin))

    visited_nodes = set()
    min_cost = {origin: 0}
    predecessors = {}

    while queue:
        cost, node = heapq.heappop(queue)

        if node in visited_nodes:
            continue

        visited_nodes.add(node)

        if node == target:
            break

        for neighbor, weight in network.get(node, {}).items():
            total = cost + weight
            if neighbor not in min_cost or total < min_cost[neighbor]:
                min_cost[neighbor] = total
                predecessors[neighbor] = node
                heapq.heappush(queue, (total, neighbor))

    route = []
    current = target
    while current != origin:
        route.append(current)
        current = predecessors[current]

    route.append(origin)
    route.reverse()

    return route, min_cost[target]


graph_map = {
    "S": {"A": 4, "B": 2},
    "A": {"C": 5, "D": 10},
    "B": {"E": 3},
    "C": {"G": 4},
    "D": {"G": 1},
    "E": {"D": 4},
    "G": {}
}

start_node = "S"
goal_node = "G"

path, cost = ucs(graph_map, start_node, goal_node)
print("Minimum Cost Path:", path)
print("Total Cost:", cost)
