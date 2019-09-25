# n=5
# # visited= [0]*n
# # adjacent=[[0,1,1,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0]]
# import sys
# def DFS(v):
#     print(v," ",end="")
#     visited[v]=1
#     for  i in range(0,len(visited)):
#         if adjacent[v][i]==1:
#             if visited[i]==0:
#                 DFS(i)
#             else:
#                 print("CYCLE")
#                 sys.exit()


# n=int(input("Enter number of nodes:"))
# visited=[0]*n


# adjacent=[]
# for i in range(n):
#     print("Enter row",i,"of adjacency matrix:")
#     adjacent.append(list(map(int,input().split())))

# print("\nConnected Graphs:\n")  
# for i in range(n):
#     if visited[i]==0:
#         DFS(i)
#         print("\n")

def countIslands(M):
    row=len(M)
    col=len(M[0])
    count=0
    visited=[]
    
    for i in range(row):
        visited.append([0]*col)
    for i in range(row):
        for j in range(col):
            if M[i][j] and visited[i][j]==0:
                
                DFS(M,i,j,visited)
                
    return count
def DFS(M,i, j,visited):
    rowMoves=[-1,-1,-1,0,0,1,1,1]
    colMoves=[-1,0,1,-1,1,-1,0,1]
    
    visited[i][j]= 1

    for k in range(8):
        if(isSafe(M,i+rowMoves[k],j+colMoves[k],visited)):
            DFS(M,i+rowMoves[k],j+colMoves[k],visited)

def isSafe(M,i,j,visited):
    return i>=0 and j>=0 and i<len(M) and j<len(M[0]) and M[i][j] and visited[i][j]==0

M=[[1,0,1,0,1],[1,1,0,0,0],[0,1,0,1,1]]
print(countIslands(M))