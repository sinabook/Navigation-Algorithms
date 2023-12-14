from Hueristic import Heuristic
def a_star_search(matrix,start):
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)
    addresses_of_T = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'T' in cell]
    counter=0
    visited=[start]
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    while(len(visited)<=num_cols*num_rows):
        if(counter<count_of_T):
            node=visited[-1]
            list=Heuristic(matrix,node=node,addresses_of_T=addresses_of_T)
            coordinates=list[0]
            if("T" in matrix[coordinates[0]][coordinates[1]]):
                counter+=1
            matrix=list[1]
            visited.append(list[0])
        if(counter==count_of_T):
            break
    print(visited)
    

