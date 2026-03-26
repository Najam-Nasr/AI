# TASK 03

tree = [
    [[4, 7], [2, 5]],
    [[1, 0], [3, 6]]
]

visited_ab = []
cuts = []
values = {}

def track_minimax(node, depth, maximizing, path):
    if depth == 0 or isinstance(node, int):
        return node, path

    if maximizing:
        best = float("-inf")
        best_path = []
        for i, child in enumerate(node):
            val, p = track_minimax(child, depth - 1, False, path + [i])
            if val > best:
                best = val
                best_path = p
        values[str(path)] = best
        return best, best_path
    else:
        best = float("inf")
        best_path = []
        for i, child in enumerate(node):
            val, p = track_minimax(child, depth - 1, True, path + [i])
            if val < best:
                best = val
                best_path = p
        values[str(path)] = best
        return best, best_path


def alpha_beta_simple(node, depth, alpha, beta, maximizing):
    if depth == 0 or isinstance(node, int):
        visited_ab.append(node)
        return node

    if maximizing:
        best = float("-inf")
        for child in node:
            best = max(best, alpha_beta_simple(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                cuts.append("pruned")
                break
        return best
    else:
        best = float("inf")
        for child in node:
            best = min(best, alpha_beta_simple(child, depth - 1, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                cuts.append("pruned")
                break
        return best


val, best_path = track_minimax(tree, 3, True, [])
ab_val = alpha_beta_simple(tree, 3, float("-inf"), float("inf"), True)

print("updated minimax value =", val)
print("optimal path =", best_path)
print("pruned nodes =", cuts)
