from collections import deque, defaultdict

layout = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

rows = len(layout)
cols = len(layout[0])

start = (0, 0)
goal = (3, 3)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

graph = defaultdict(list)

for r in range(rows):
    for c in range(cols):
        if layout[r][c] == 1:
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and layout[nr][nc] == 1:
                    graph[(r, c)].append((nr, nc))

print("Graph Connections:")
for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")

queue = deque([start])
visited = {start}
parent = {}
order = []

while queue:
    current = queue.popleft()
    order.append(current)

    if current == goal:
        break

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = current
            queue.append(neighbor)

path = []
step = goal

while step != start:
    path.append(step)
    step = parent[step]

path.append(start)
path.reverse()

print("\nBFS Order:")
print(order)

print("\nShortest Path:")
print(path)
