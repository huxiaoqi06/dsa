from collections import defaultdict,deque
n,m=map(int,input().split())
dic=defaultdict(list)
indegree=[0]*n
for i in range(m):
    u,v=map(int,input().split())
    dic[u].append(v)
    indegree[v]+=1
q=deque()
for i in range(n):
    if indegree[i]==0:
        q.append(i)
count=0
while q:
    node=q.popleft()
    count+=1
    for next_node in dic[node]:
        indegree[next_node]-=1
        if indegree[next_node]==0:
            q.append(next_node)
if count<n:
    print('Yes')
else:
    print('No')