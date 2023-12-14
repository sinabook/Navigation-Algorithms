from Hueristic import Heuristic
def a_star_search(matrix,start):
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)
    addresses_of_T = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'T' in cell]
    counter=0
    energySpent=0
    visited=[start]
    print(visited)
    visited.append(Heuristic(matrix,node=start,addresses_of_T=addresses_of_T))
    print(visited)

