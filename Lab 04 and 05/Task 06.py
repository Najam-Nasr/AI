import heapq

class AdaptiveAStar:
    def __init__(self, network, heuristics):
        self.network = network
        self.heuristics = heuristics

    def find_path(self, start, goal):
        queue = [(self.heuristics[start], start, [start], 0)]
        visited = {}

        while queue:
            f_score, node, path, g_score = heapq.heappop(queue)

            if node == goal:
                return path, g_score

            if node in visited and visited[node] <= g_score:
                continue

            visited[node] = g_score

            for neighbor, cost in self.network[node].items():
                new_g = g_score + cost
                new_f = new_g + self.heuristics[neighbor]
                heapq.heappush(queue, (new_f, neighbor, path + [neighbor], new_g))

        return None, float("inf")

    def change_edge(self, from_node, to_node, cost):
        print(f"--- Edge {from_node}->{to_node} updated to {cost} ---")
        self.network[from_node][to_node] = cost


graph_data = {
    "A": {"B": 4, "C": 3},
    "B": {"E": 12, "F": 5},
    "C": {"D": 7, "E": 10},
    "D": {"E": 2},
    "E": {"G": 5},
    "F": {"G": 16},
    "G": {}
}

heuristics_map = {"A": 14, "B": 12, "C": 11, "D": 6, "E": 4, "F": 11, "G": 0}

solver = AdaptiveAStar(graph_data, heuristics_map)

path, cost = solver.find_path("A", "G")
print(f"Initial Path: {path} with cost {cost}")

solver.change_edge("B", "E", 7)
path, cost = solver.find_path("A", "G")
print(f"Updated Path: {path} with cost {cost}")

solver.change_edge("A", "B", 8)
path, cost = solver.find_path("A", "G")
print(f"Final Path: {path} with cost {cost}")
