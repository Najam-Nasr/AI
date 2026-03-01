def limited_dfs(network, node, target, limit, route, explored):
    explored.append(node)
    route.append(node)

    if node == target:
        return True

    if limit <= 0:
        route.pop()
        return False

    for next_node in network.get(node, []):
        if limited_dfs(network, next_node, target, limit - 1, route, explored):
            return True

    route.pop()
    return False


connections = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": [],
    "F": ["H"],
    "G": [],
    "H": []
}

start_node = "A"
target_node = "H"

print("Depth-Limited Search with limit = 2")
visited_two = []
path_two = []

result_two = limited_dfs(connections, start_node, target_node, 2, path_two, visited_two)

print("Visited:", visited_two)
if result_two:
    print("Path:", path_two)
else:
    print("Target not reached within limit 2")

print("\n--------------------\n")

print("Depth-Limited Search with limit = 3")
visited_three = []
path_three = []

result_three = limited_dfs(connections, start_node, target_node, 3, path_three, visited_three)

print("Visited:", visited_three)
if result_three:
    print("Path:", path_three)
else:
    print("Target not reached within limit 3")
