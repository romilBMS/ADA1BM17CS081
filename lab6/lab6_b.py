adjMatrix=[
    [0, 0 ,0 ,0 ,0 ,0 ,0, 0],
    [1 ,0, 0, 0, 0, 0, 0, 0],
    [0 ,1, 0, 0, 0 ,0, 0, 0],
    [0, 1 ,0 ,0, 0, 0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0, 0 ,0, 0],
    [0 ,0, 1 ,0 ,1 ,0 ,0 ,0 ],  
    [0 ,0 ,0 ,1 ,1 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,1 ,1 ,0]]


def topologicalSort(adjMatrix):
    order=[]
    N=len(adjMatrix)

    for i in range(N): #col
        count =0
        if(not checkIfDone(adjMatrix)):
            for r in range(N): #row
                if adjMatrix[r][i] == 0:                
                    count+=1

            if count==N:
                order.append(i)
                adjMatrix[i]= [0]*N
                i=-1
        else:
            break
        
    if len(order)==0:
        print("Not possible")
    else:
        print(order)
def checkIfDone(adjMatrix):
    print("IN")
    return adjMatrix.count(0)==len(adjMatrix)**2

# n= int(input("Enter number of nodes "))
# adjMatrix=[]
# for i in range(n):
#     adjMatrix.append(list(map(int,input().split())))


topologicalSort(adjMatrix)




