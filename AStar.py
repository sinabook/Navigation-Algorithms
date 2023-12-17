from Hueristic import Heuristic
def a_star_search(matrix,start):
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)
    addresses_of_T = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'T' in cell]
    counter=0
    visited=[start]
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    while(len(visited)<=num_cols*num_rows):
        node=visited[-1]
        list=Heuristic(matrix,node=node,addresses_of_T=addresses_of_T,visited=visited)
        length=len(visited)-1
        if(list[0]==None):
            while(list[0]==None):
                length-=1
                if(length<0):
                    print("We Have reached to the node that we started from")
                    return [matrix,visited]
                node=visited[length]
                list=Heuristic(matrix=matrix,node=node,addresses_of_T=addresses_of_T,visited=visited)
                if(list[0]!=None):
                    if(list[2]==True):
                        counter+=1
                        if(counter==count_of_T):
                            print("We have reached the asnwer")
                            return [matrix,visited]
                    matrix=list[1]
                    visited.append(list[0])
                else:
                    continue
            if(list[2]==True):
               counter+=1
               if(counter==count_of_T):
                    print("We have reached the asnwer")
                    return[matrix,visited]
        else:
            matrix=list[1]
            visited.append(list[0])


 

