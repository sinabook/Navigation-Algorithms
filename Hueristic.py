from Manhatan import manhattan_distance
from Succesor import get_successors
def Heuristic(matrix,node,addresses_of_T):
    
    x=node[0]
    y=node[1]
    AmountOfG=[]
    for i in range(0,len(addresses_of_T)):
        AmountOfG.append(manhattan_distance((x,y),addresses_of_T[i]))
    AmountOfH=[]
    for i in range(len(get_successors(matrix,x,y))):
        temp=get_successors(matrix,x,y)[i]
        addr=[]
        addr.append((x-1,y))
        addr.append((x,y+1))
        addr.append((x+1,y))
        addr.append((x,y-1))
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
    idx=addr[index]
    temp=matrix[idx[0]][idx[1]]
    matrix[idx[0]][idx[1]]=temp[0]
    

    return [idx,matrix]
