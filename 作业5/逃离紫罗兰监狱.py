R,C,K=map(int,input().strip().split())
l=[]
for i in range(R):
    li=input().strip()
    l.append(li)
    for j in range(C):
        if li[j]=='S':
            sr=i
            sc=j
        
history=[[[float('inf')]*(K+1) for i in range(C)]for _ in range(R)]
history[sr][sc][0]=0
from collections import deque
q=deque()
q.append((sr,sc,0))
ans=-1
while q:
    r,c,k=q.popleft()
    n=history[r][c][k]
    if l[r][c]=='E':
        ans=n
        break
    next_steps=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
    for nr,nc in next_steps:
        if 0<=nr<R and 0<=nc<C:
            nk=k#一定要另外用一个变量，不能随意改变k，因为k还要继续进入另一个方向的循环
            if l[nr][nc]=='#':
                nk+=1
                if nk>K:
                    continue#此时这一步已经不能走了，不加入队列
            if n+1<history[nr][nc][nk]:
                history[nr][nc][nk]=n+1
                q.append((nr,nc,nk))
print(ans)