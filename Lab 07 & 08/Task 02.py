# TASK 02

tree = [
    [[4, 7], [2, 5]],
    [[1, 8], [3, 6]]
]

visited_mm = []
visited_ab = []
node_values = {}
cuts = []

def run_minimax(node, depth, maximizing):
    if depth == 0 or isinstance(node, int):
        visited_mm.append(node)
        return node

    if maximizing:
        value = float("-inf")
        for child in node:
            value = max(value, run_minimax(child, depth - 1, False))
        return value
    else:
        value = float("inf")
        for child in node:
            value = min(value, run_minimax(child, depth - 1, True))
        return value


def alpha_beta(node, depth, alpha, beta, maximizing, label):
    if depth == 0 or isinstance(node, int):
        visited_ab.append(node)
        return node

    if maximizing:
        best = float("-inf")
        for i, child in enumerate(node):
            val = alpha_beta(child, depth - 1, alpha, beta, False, label + str(i))
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                cuts.append(label + " pruned")
                break

        node_values[label] = best
        return best
    else:
        best = float("inf")
        for i, child in enumerate(node):
            val = alpha_beta(child, depth - 1, alpha, beta, True, label + str(i))
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                cuts.append(label + " pruned")
                break

        node_values[label] = best
        return best


mm_val = run_minimax(tree, 3, True)
ab_val = alpha_beta(tree, 3, float("-inf"), float("inf"), True, "R")

print("minimax root =", mm_val)
print("alpha-beta root =", ab_val)

print("\nminimax visited =", len(visited_mm))
print("alpha-beta visited =", len(visited_ab))

print("\nnode values =", node_values)
print("\npruned nodes =", cuts)
