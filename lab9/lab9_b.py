graph = [   [9999, 2, 9999, 6, 9999], 
            [2, 9999, 3, 8, 5], 
            [9999, 3, 9999, 9999, 7], 
            [6, 8, 9999, 9999, 9], 
            [9999, 5, 7, 9, 9999]] 

def primMST(g):
    mSet=set()
    keys=[0]+[9999]*(len(g)-1)
    minCost=0
    i=0

    while len(g)!=len(mSet)+1:
        # print(minCost)
        mSet.add(i)
        # print(mSet)
        for k in range(len(g[i])):
            keys[k] = min(keys[k], g[i][k]   )
        
        x=9999
        index=9999
        for k in range(len(keys)):
            if k not in mSet:
                x=min(x,keys[k])
                
        
        minCost+=x
        
        i=keys.index(x)
        

    
    return minCost

print(primMST(graph))
    

                

  