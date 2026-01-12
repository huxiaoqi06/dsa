from collections import deque
T=int(input().strip())
for _ in range(T):
    R,C=map(int,input().strip().split())
    l=[]
    for i in range(R):
        li=input().strip()
        l.append(li)
        for j in range(C):
            if li[j]=='S':
                sr,sc=i,j
    history=[[float('inf')]*C for i in range(R)]
    history[sr][sc]=0
    q=deque()
    q.append((sr,sc,0))
    time=0
    while q:
        r,c,steps=q.popleft()
        if l[r][c]=='E':
            time=steps
            break
        to_visit=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
        for nr,nc in to_visit:
            if 0<=nr<R and 0<=nc<C:
                if steps+1<history[nr][nc] and l[nr][nc]!='#':
                    q.append((nr,nc,steps+1))
                    history[nr][nc]=steps+1
    if time==0:
        print('oop!')
    else:
        print(time)
