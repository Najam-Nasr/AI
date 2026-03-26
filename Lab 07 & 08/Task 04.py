#TASK 04

from ortools.sat.python import cp_model

model = cp_model.CpModel()

A = model.NewIntVar(0, 3, "A")
B = model.NewIntVar(0, 3, "B")
C = model.NewIntVar(0, 3, "C")

model.Add(A != B)
model.Add(B != C)
model.Add(A + B <= 4)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
    print("A =", solver.Value(A))
    print("B =", solver.Value(B))
    print("C =", solver.Value(C))
else:
    print("No solution found.")
