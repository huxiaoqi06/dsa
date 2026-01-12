from collections import defaultdict,deque
P=int(input().strip())
positions=[]
for _ in range(P):
    positions.append(input().strip())


graph=defaultdict(list)
Q=int(input().strip())
for _ in range(Q):
    p1,p2,distance=input().strip().split()
    graph[p1].append((p2,int(distance)))
    graph[p2].append((p1,int(distance)))
R=int(input().strip())
for _ in range(R):
    start,end=input().strip().split()
    q=deque()
    q.append((start,0,[]))
    min_distance=float('inf')
    history={}
    for position in positions:
        history[position]=float('inf')
    history[start]=0
    while q:
        position,length,path=q.popleft()
        if position==end:
            min_distance=min(min_distance,length)
        answer=path
        for next_position,distance in graph[position]:
            if length+distance<history[next_position]:
                history[next_position]=length+distance
                q.append((next_position,length+distance,path+[next_position]))
    for i in range(len(answer)):
        