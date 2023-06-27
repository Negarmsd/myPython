from pysat.solvers import Glucose3

def solve_cnf(cnf):
    solver = Glucose3()
    
    # Add each clause to the solver
    for clause in cnf:
        solver.add_clause(clause)
    
    # Solve the CNF formula
    is_sat = solver.solve()
    
    if is_sat:
        model = solver.get_model()
        return True, model
    else:
        return False, None
    
def get_cnf(sudoku):
    cnf = grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9]  for _ in range(81)]
    print(cnf)
    for j in range(sudoku) :
        for i in range(sudoku.get(j)):
            cell = sudoku.get(j).get(i)
            if cell == 0:
                continue
            if cell > 0 and cell<10:
                cnf.append([-1 * cell])
            



sudoku = [[0, 5, 0, 3, 0, 0, 0, 6, 0],
          [9, 2, 0, 0, 0, 1, 4, 5, 3],
          [4, 0, 0, 2, 5, 6, 9, 0, 8],
          [7, 0, 4, 0, 9, 8, 6, 2, 1],
          [2, 0, 0, 7, 0, 0, 0, 8, 0],
          [0, 0, 0, 0, 0, 0, 7, 9, 4],
          [0, 6, 0, 0, 0, 7, 1, 3, 0],
          [0, 4, 2, 0, 1, 0, 0, 0, 6],
          [1, 0, 0, 0, 0, 0, 0, 0, 2]]

cnf = get_cnf(sudoku)
is_sat, model = solve_cnf(cnf)

if is_sat:
    print("Satisfiable")
    print("Model:", model)
else:
    print("Unsatisfiable")
