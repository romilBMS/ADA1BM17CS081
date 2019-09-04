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
                count+=1
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