class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



def BFS(k):
    visited[k] == 1 
    q.enqueue(k)
    while(q.size()>0):
        x= q.dequeue()
        for i in range(len(adjacent[x])):
            if visited[i]==0:
                q.enqueue(i)
                visited[i] = 1
                print(i)

n=int(input("Enter the number of nodes"))
print("Enter adjacency matrix")
adjacent=[]
visited=[0]*n
q=Queue()
for i in range(n):
    adjacent.append(list(map(int,input("Enter Row:").split())))
# adjacent=[[0,0,0],[1,0,1],[1,1,1]]
s=int(input("Enter Source vertex:"))
BFS(s)



