def limited_search(tree, node, target, depth_limit, route, seen):
    seen.append(node)
    route.append(node)

    if node == target:
        return True

    if depth_limit <= 0:
        route.pop()
        return False

    for child in tree.get(node, []):
        if limited_search(tree, child, target, depth_limit - 1, route, seen):
            return True

    route.pop()
    return False


def deepening_search(tree, origin, target, max_level):
    for level in range(max_level + 1):
        print(f"\nChecking at depth {level}")

        visited_nodes = []
        current_path = []

        result = limited_search(tree, origin, target, level, current_path, visited_nodes)

        print("Nodes visited:", visited_nodes)

        if result:
            print("Target reached")
            print("Path:", current_path)
            return

    print("Target not found within given depth range")


network = {
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
end_node = "G"

deepening_search(network, start_node, end_node, 5)
