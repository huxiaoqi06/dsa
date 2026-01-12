from collections import deque
dic={}
n,m=map(int,input().strip().split())
starts={}
for _ in range(m):
    u,v=map(int,input().strip().split())
    if u in dic:
        dic[u].append(v)
    else:
        dic[u]=[v]
        starts[u]=1

judge=0
for key in dic:
        path=set()
        path.add(key)
        q=deque()
        q.append(key)

        while q:
            node=q.popleft()
            if node in dic:
                next_nodes=dic[node]
            else:
                 continue
            for next_node in next_nodes:
                if next_node==key:
                    judge=1
                if next_node not in path:
                    path.add(next_node)
                    q.append(next_node)
if judge:
     print("Yes")
else:
     print("No")      



