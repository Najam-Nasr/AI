import heapq

network = {
    "S": [("A", 3), ("B", 6), ("C", 5)],
    "A": [("D", 9), ("E", 8)],
    "B": [("F", 12), ("G", 14)],
    "C": [("I", 7)],
    "H": [("I", 5), ("J", 6)],
    "I": [("K", 1)],
    "L": [("M", 2)],
    "D": [], "E": [], "F": [], "G": [], "J": [], "K": [], "M": []
}

goals = ["D", "E", "F", "G", "I", "K"]
start = "S"

def ucs_single(network, start, target):
    heap = [(0, start, [start])]
    visited = set()

    while heap:
        cost, node, path = heapq.heappop(heap)

        if node == target:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in network.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))

    return None, float("inf")

def multi_goal_ucs(network, start, goal_list):
    current = start
    remaining = set(goal_list)
    full_path = [current]
    total_cost = 0

    while remaining:
        nearest_goal = None
        shortest_cost = float("inf")
        best_route = []

        for g in remaining:
            route, cost = ucs_single(network, current, g)
            if route is not None and cost < shortest_cost:
                shortest_cost = cost
                nearest_goal = g
                best_route = route

        if nearest_goal is None:
            break

        full_path.extend(best_route[1:])
        total_cost += shortest_cost
        current = nearest_goal
        remaining.remove(nearest_goal)

    return full_path, total_cost

path, cost = multi_goal_ucs(network, start, goals)
print("Complete path:", path)
print("Total cost:", cost)
