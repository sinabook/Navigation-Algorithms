from AStar import a_star_search
matrix=[["1R","1","1","5","5","4","2C","1","15","1B"],
        ["1","1","5","3","5","5","4","5","X","X"],
        ["5","1I","1","6","2","2","2","1","1","1T"],
        ["X","X","1","6","5","5","2","1","1","X"],
        ["X","X","1","X","X","50","2","1C","1","X"],
        ["1","1","1","2","2","2T","2","1","1","1"]
        ]
addresses_of_R = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'R' in cell]
list=a_star_search(matrix,start=addresses_of_R[0])
def calculate(visited):
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
        if(UpOrDown==0 and LeftOrRight !=0):
                if(LeftOrRight>0):                                
                        course.append("L")
                        continue
                if(LeftOrRight<0):                                        
                        course.append("R")
                        continue

        if(LeftOrRight==0 and UpOrDown!=0):
                if(UpOrDown>0):
                        course.append("U")
                        continue

                if(UpOrDown<0):                                        
                        course.append("D")
                        continue
                        
    return course            
               
print(calculate(visited=list[1]))
