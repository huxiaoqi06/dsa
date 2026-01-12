from collections import defaultdict,deque
n,m=map(int,input().strip().split())

graph=defaultdict(set)
for _ in range(m):
    i,j=map(int,input().strip().split())
    i-=1
    j-=1
    graph[i].add(j)
    graph[j].add(i)

unvisited=set(range(n))
def bfs(start):
    q=deque([start])
    while q:
        i=q.popleft()
        to_remove=[]
        for j in unvisited:
            if j!=i and j not in graph[i]:
                q.append(j)
                to_remove.append(j)
        for j in to_remove:
            unvisited.remove(j)
count=0
while unvisited:
    count+=1
    bfs(unvisited.pop())
print(count-1)

