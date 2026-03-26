# TASK 07

from ortools.sat.python import cp_model

N = 4
model = cp_model.CpModel()

queens = [model.NewIntVar(0, N - 1, f"q{i}") for i in range(N)]

model.AddAllDifferent(queens)

for i in range(N):
    for j in range(i + 1, N):
        model.Add(queens[i] - queens[j] != i - j)
        model.Add(queens[j] - queens[i] != i - j)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
    print("4-Queens Solution:\n")
    for r in range(N):
        row = ""
        for c in range(N):
            row += " Q " if solver.Value(queens[r]) == c else " _ "
        print(row)

    print("\nPositions:")
    for i in range(N):
        print(f"Row {i} -> Col {solver.Value(queens[i])}")
else:
    print("No solution found.")
