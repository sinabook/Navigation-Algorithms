from AStar import a_star_search
from BestFirstSearch import best_first_search
from DFS import dfs_with_backtracking
from BFS import bfs
from IDS import ids_with_backtracking
from UCS import ucs_with_backtracking
import timeit
matrix=[["1R","1","1","5","5","4","2C","1","15","1B"],
        ["1","1","5","3","5","5","4","5","X","X"],
        ["5","1I","1","6","2","2","2","1","1","1T"],
        ["X","X","1","6","5","5","2","1","1","X"],
        ["X","X","1","X","X","50","2","1C","1","X"],
        ["1","1","1","2","2","2T","2","1","1","1"]]
matrix=[["1R","2","3","4","5"],
        ["2B","X","3","4","5"],
        ["1","1I","1","1","1"],
        ["X","1C","X","X","2T"],
        ["1","1","1","1","1"]]
matrix=[["1R","1","1","5","5","4","2I"],
        ["1","1","5","3","20","4T","X"],
        ["5","1","10","6","2","2","2"],
        ["X","X","1","6","5","5","2"],
        ["X","X","1","X","X","50","2"],
        ["1","1","1","2","2","2","2"],
        ["X","X","X","1","1","X","X"]]
addresses_of_R = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'R' in cell]
addresses_of_T = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'T' in cell]

print("**********Welcome to our navigation algorithm project**********")
print("Please type in the number of the algorithm you want to navigate with")
print("1.A*")
print("2.BestFirstSearch")
print("3.BFS")
print("4.DFS")
print("5.IDS")
print("6.UCS")
n=int(input())
if n==1:
        list=a_star_search(matrix,start=addresses_of_R[0])
if n==2:
        list=best_first_search(matrix,start=addresses_of_R[0])
if n==3:
        list=bfs(matrix=matrix,start=addresses_of_R[0],goal=addresses_of_T)
if n==4:
        list=dfs_with_backtracking(matrix=matrix,start=addresses_of_R[0])
if n==5:
        print("Please enter the depth")
        depth=int(input())
        list=ids_with_backtracking(matrix=matrix,start=addresses_of_R[0],max_depth=depth)
if n==6:
        list=ucs_with_backtracking(matrix=matrix,start=addresses_of_R[0],goal=addresses_of_T)
def calculatePath(visited):
    path=[]
    for i in range(0,len(visited)):
        if(i!=len(visited)-1):
                item1=visited[i]
                item2=visited[i+1]
                UpOrDown=item1[0]-item2[0]
                LeftOrRight=item1[1]-item2[1]
                path.append((UpOrDown,LeftOrRight))
        else:
             break
    course=[]   
    for i in range(0,len(path)):
        item=path[i]
        UpOrDown=int(item[0])
        LeftOrRight=int(item[1])
        
        while(abs(LeftOrRight)>0):
                        if(LeftOrRight>0):  
                                LeftOrRight-=1
                                course.append("L")
                                continue
                        if(LeftOrRight<0):                                        
                                course.append("R")
                                LeftOrRight+=1
                                continue
 
        while(abs(UpOrDown)>0):
                        
                        if(UpOrDown>0):
                                course.append("U")
                                UpOrDown-=1
                                continue
                        if(UpOrDown<0):                                        
                                course.append("D")
                                UpOrDown+=1
                                continue

                                
    return course            
def calculateEnergy(matrix,visited):
        energy=0
        for visit in visited:
                x,y=visit
                temp=matrix[x][y]
                h=int(temp[0])
                if(len(temp)>1):
                        if(temp[1]=="I"):
                                h-=12
                        elif(temp[1]=="B"):
                                h-=5
                        elif(temp[1]=="C"):
                                h-=10
                energy+=h
        return energy
                
def convert(set):
    return sorted(set)
visited=convert(list[1])
print(calculatePath(visited=visited))
print("Energy Spent: ",calculateEnergy(matrix=matrix,visited=visited))

# print("************* If you want to see how much time it costs for each of these algorithm's type in the number *************")
# print("Please type in the number of the algorithm you want to navigate with")
# print("1.A*")
# print("2.BestFirstSearch")
# print("3.BFS")
# print("4.DFS")
# print("5.IDS")
# print("6.UCS")
# m=int(input())
# if m==1:
#         time_taken = timeit.timeit(lambda: a_star_search(matrix,start=addresses_of_R[0]))
#         print(time_taken)
# if m==2:
#         time_taken = timeit.timeit(lambda: best_first_search(matrix,start=addresses_of_R[0],goals=addresses_of_T))
#         print(time_taken)
# if m==3:
#         time_taken = timeit.timeit(lambda: bfs(matrix=matrix,start=addresses_of_R,goal=addresses_of_T))
#         print(time_taken)
# if m==4:
#         time_taken = timeit.timeit(lambda: dfs_with_backtracking(matrix=matrix,start=addresses_of_R))
#         print(time_taken)
# if m==5:
#         time_taken = timeit.timeit(lambda: ids_with_backtracking(matrix=matrix,start=addresses_of_R[0],goal=addresses_of_T,max_depth=depth))
#         print(time_taken)
# if m==6:
#         time_taken = timeit.timeit(lambda: ucs_with_backtracking(matrix=matrix,start=addresses_of_R[0],goal=addresses_of_T))
#         print(time_taken)
        
