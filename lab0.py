num_array=list()
def max():
    N=int(input("Enter N"))
    max=0
    for i in range(0,N):
        A[i]=input("Enter number")
        if A[i]>max:
            max=A[i]

    print("Maximum num",max)
