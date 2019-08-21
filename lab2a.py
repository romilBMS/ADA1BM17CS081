def findks(A,k):
    if k<len(A):
        for i in range(0,k):
                min=i
                for j in range(i+1,len(A)):
                        if(A[j]<A[min]):
                                min=j
                
                A[min],A[i]=A[i],A[min]

        return A[i]



A=[]
n=int(input("Enter the number of elements"))
for i in range(n):        
        A.append(int(input("Enter number")))

k=int(input("Enter k"))
print("The kth smallest element is",findks(A,k))

