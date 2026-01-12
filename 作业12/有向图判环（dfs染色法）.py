from collections import defaultdict
dic=defaultdict(list)
n,m=map(int,input().strip().split())
color=[0]*n
for _ in range(m):
    u,v=map(int,input().strip().split())
    dic[u].append(v)


def dfs(node):
    if color[node]==1:
        return True
    elif color[node]==2:
        return False
    color[node]=1
    for next_node in dic[node]:
        if dfs(next_node):
            return True
    color[node]=2
    return False

judge=0
for i in range(n):
    if color[i]==0:
        if dfs(i):
            print('Yes')
            judge=1
            break
if judge==0:
    print("No")
    
