# n=5
# visited= [0]*n
# adjacent=[[0,1,1,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0]]

def DFS(v):
    print(v," ",end="")
    visited[v]=1
    for  i in range(0,len(visited)):
        if adjacent[v][i]==1 and visited[i]==0:
            DFS(i)
n=int(input("Enter number of nodes:"))
visited=[0]*n
adjacent=[]
for i in range(n):
    print("Enter row",i,"of adjacency matrix:")
    adjacent.append(list(map(int,input().split())))

print("\nConnected Graphs:\n")  
for i in range(n):
    if visited[i]==0:
        DFS(i)
        print("\n")
