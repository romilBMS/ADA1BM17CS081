def solveKP(value, weight, w):
    L=[]
    for i in range(len(weight)):
        L.append([0]*(w+1))
    




    for i in range(len(weight)):
        for j in range(1,w+1):
            if weight[i]<=j:
                L[i][j]=max(L[i-1][j], value[i]+L[i-1][j-weight[i]])
            else:
                L[i][j]=L[i-1][j]
        
    print(L[i][j])


value=(1,4,4,5,7)
weight=(1,2,3,4,5)
maxCap=9
solveKP(value,weight,maxCap)

