A=(0,90,25,10,7,12,255)

def checkMaxHeap(A):
    i=1
    n=len(A)
    while i<=(n//2):
        print(i)
        if (2*i+1)<n:        
            if A[i]<max(A[2*i],A[2*i+1]):
                return False
        elif 2*i<n:
            if A[i]<A[2*i]:
                return False
        
        i+=1
    
    return True

print(checkMaxHeap(A))
