step=[(-2,-1),(-2,1),
      (-1,-2),(-1,2),
      (1,-2),(1,2),
      (2,-1),(2,1)]

def name(x,y):
    return chr(ord('A')+x)+str(y+1)

def judge(x,y):
    if 0<=x<q and 0<=y<p and not visited[x][y]:
        return True
    return False

def dfs(x,y):
    visited[x][y]=True
    path.append(name(x,y))
    if len(path)==p*q:
        return True
    nextstep=[]
    for dx,dy in step:
        nx=dx+x
        ny=dy+y
        if judge(nx,ny):
            nextstep.append((nx,ny))
    for nx,ny in nextstep:
        if dfs(nx,ny):
            return True
    visited[x][y]=False
    path.pop()
    return False

n=int(input())
for i in range(n):
    p,q=map(int,input().strip().split())
    visited=[[False]*p for _ in range(q)]
    path=[]
    print(f"Scenario #{i + 1}:")
    if dfs(0,0):
        print(''.join(path))
    else:
        print('impossible')
    print('')
    