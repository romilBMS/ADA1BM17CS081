def getmax():
    A=list()
    N=int(input("Enter N"))
    max=0
    for i in range(0,N):
        A.append(int(input("Enter number")))
        if A[i]>max:
            max=A[i]

    print("Maximum number",max)
    
getmax()