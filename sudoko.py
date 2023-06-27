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

def create_index(i, j, num):

    # Convert integers to strings
    i_str = str(i)
    j_str = str(j)
    num_str = str(num)

    # Concatenate the strings
    index_str = i_str + j_str + num_str

    # Convert the concatenated string back to an integer
    index = int(index_str)
    
    return index

#creates index row = 1, col = 3, k = 1, ...9 => index = 131, ..., 13k    
def get_cnf(sudoku):
    cnf = []
    for j in range(len(sudoku)) :
        for i in range(len(sudoku[j])):
            temp = []
            for num in range(9):
                temp.append(create_index(i + 1,j + 1,num + 1))
            cnf.append(temp)
            

    for j in range(len(sudoku)) :
        neg_cnf = []
        for i in range(len(sudoku[j])):

            cell = sudoku[j][i]
            #row
            if cell == 0:
                continue
            if cell > 0 and cell<10:
                cnf.append([create_index(i+1,j+1,cell)])
                neg_cnf.append(-1 * create_index(i+1,j+1,cell))

            #col
            for jj in range(len(sudoku)):
               cell = sudoku[jj][i]
            if cell == 0:
                continue
            if cell > 0 and cell<10:
                cnf.append([create_index(i + 1,jj +1 ,cell)])
                neg_cnf.append(-1 * create_index(i + 1,jj + 1,cell))
            #block ???

        cnf.append(neg_cnf)
    return cnf


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
print(cnf)
is_sat, model = solve_cnf(cnf)

if is_sat:
    print("Satisfiable")
    print("Model:", model)
else:
    print("Unsatisfiable")
