def beam_search():
    goal = 20
    k = 2

    def h(n):
        return abs(goal - n)

    def get_neighbors(n):
        return [n + 2, n + 3, n * 2]

    beam = [(1, [1])]
    level = 1

    while True:
        print("Level " + str(level) + ": " + str([state for state, path in beam]))

        candidates = []
        for state, path in beam:
            for neighbor in get_neighbors(state):
                candidates.append((neighbor, path + [neighbor]))

        candidates.sort(key=lambda x: h(x[0]))

        for state, path in candidates:
            if state == goal:
                print("Goal reached: " + str(goal))
                print("Path: " + " -> ".join(map(str, path)))
                return

        beam = candidates[:k]
        level += 1

beam_search()
