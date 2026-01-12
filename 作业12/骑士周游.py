from  collections import deque
n=int(input())
sr,sc=map(int,input().strip().split())
visited=[[False]*n for _ in range(n)]
visited[sr][sc]=True

def is_valid(r,c):
    if 0<=r<n and 0<=c<n and not visited[r][c]:
        return True
    return False

def next_steps(r,c):
    moves=[[-2,+1],[-2,-1],[-1,+2],[-1,-2],
            [+1,+2],[+1,-2],[+2,+1],[+2,-1]]
    l=[]
    for dr,dc in moves:
        nr,nc=r+dr,c+dc
        if is_valid(nr,nc):
            count=0
            for ndr,ndc in moves:
                nnr,nnc=nr+ndr,nc+ndc
                if is_valid(nnr,nnc):
                    count+=1
            l.append([nr,nc,count])
    l.sort(key=lambda x:x[2])
    return [[r,c] for r,c,count in l]

def dfs(r,c,number):
    if number==n**2:
        return True
    for nr,nc in next_steps(r,c):
        if is_valid(nr,nc):
            visited[nr][nc]=True
            if dfs(nr,nc,number+1):
                return True
            visited[nr][nc]=False
    return False

if dfs(sr,sc,1):
    print('success')
else:
    print('fail')
    