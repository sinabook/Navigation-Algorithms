from Manhatan import manhattan_distance
from Succesor import get_successors
from Address import get_address
def Heuristic(matrix,node,addresses_of_T,visited):
    x=node[0]
    y=node[1]
    AmountOfG=[]
    for i in range(0,len(get_successors(matrix,x,y,visited=visited))):
        Temp=[]
        for i in range(0,len(addresses_of_T)):
            Temp.append(manhattan_distance((x,y),addresses_of_T[i]))
        AmountOfG.append(max(Temp))
    AmountOfH=[]
    for i in range(len(get_successors(matrix,x,y,visited=visited))):
        temp=get_successors(matrix,x,y,visited=visited)[i]
        h=int(temp[0])
        if(len(temp)>1):
            if(temp[1]=="I"):
                  h-=12
            elif(temp[1]=="B"):
                h-=5
            elif(temp[1]=="C"):
                 h-=10
        
        AmountOfH.append(h)
    AmountOfF=[]
    for i in range(0,len(AmountOfH)):
        AmountOfF.append((AmountOfG[i]+AmountOfH[i]))
    index = None
    for i, element in enumerate(AmountOfF):
        if element == min(AmountOfF):
            index = i
            break
        else:
            continue
    if(index is None):
        return "This is over"
    idx=get_address(matrix,x,y,visited=visited)[index]
    # idx=get_address(matrix,x,y)[index]
    temp=matrix[idx[0]][idx[1]]
    matrix[idx[0]][idx[1]]=temp[0]
    
    print("END")
    return [idx,matrix]
