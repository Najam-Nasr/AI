# TASK 01

tree = [
    [[4, 7], [2, 5]],
    [[1, 8], [3, 6]]
]

visited = []

def minimax(node, depth, maximizing):
    if depth == 0 or isinstance(node, int):
        visited.append(node)
        return node

    if maximizing:
        best = float("-inf")
        for child in node:
            best = max(best, minimax(child, depth - 1, False))
        return best
    else:
        best = float("inf")
        for child in node:
            best = min(best, minimax(child, depth - 1, True))
        return best

root_value = minimax(tree, 3, True)

print("part 1:")
print("root value =", root_value)

print("\npart 2:")
print("visited nodes =", visited)


def limited_minimax(node, depth, maximizing):
    if depth == 0:
        if isinstance(node, list):
            return node[0][0] if isinstance(node[0], list) else node[0]
        return node

    if isinstance(node, int):
        return node

    if maximizing:
        best = float("-inf")
        for child in node:
            best = max(best, limited_minimax(child, depth - 1, False))
        return best
    else:
        best = float("inf")
        for child in node:
            best = min(best, limited_minimax(child, depth - 1, True))
        return best

print("\npart 3:")
print("depth limited value =", limited_minimax(tree, 2, True))
