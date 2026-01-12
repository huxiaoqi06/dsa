from collections import deque,defaultdict
n,p=map(int,input().strip().split())
graph=[[0]*n for _ in range(n)]
l=[]
rudu=[0]*n
chudu=[0]*n

for _ in range(n):
    l.append(list(map(int,input().strip().split())))

for _ in range(p):
    a,b,c=map(int,input().strip().split())
    if graph[a-1][b-1]==0 and c!=0:
            rudu[b-1]+=1
            chudu[a-1]+=1
    graph[a-1][b-1]+=c


q=deque()
to_ans=[]
count=0
for i in range(n):
    if rudu[i]==0:
        q.append(i)
        count+=1

    if chudu[i]==0:
        to_ans.append(i)

while q:
    i=q.popleft()
    for j in range(n):
        if graph[i][j]!=0:
            if l[i][0]>0:
                l[j][0]+=graph[i][j]*l[i][0]
            rudu[j]-=1
            if rudu[j]==0:
                count+=1
                q.append(j)
                l[j][0]-=l[j][1]

i=0
while i<len(to_ans):
    if l[to_ans[i]][0]<=0:
        del to_ans[i]
        i-=1
    i+=1
if count==n and to_ans:
    for i in to_ans:
        print(*[i+1,l[i][0]])
else:
    print('NULL')