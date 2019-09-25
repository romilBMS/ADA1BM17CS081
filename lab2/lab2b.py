def findkl(A,k):
    n=len(A)

    for i in range(k):
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
            
    return A[n-k:]

A=[2,1,3,6,5,4]
print(findkl(A,3))
