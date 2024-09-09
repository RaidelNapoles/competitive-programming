from solver import naive_solver, naive_solver_pruned
from test_case_generator import *


locations = generate_test_case(8)
print(f"{len(locations)}")
for i in locations:
    print(i)
print()

print(naive_solver_pruned(locations))
print(naive_solver(locations))
