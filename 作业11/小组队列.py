from collections import deque
t=int(input().strip())
teams=[]
for _ in range(t):
    dic={}
    team=input().strip().split()
    for member in team:
        dic[member]=0
    teams.append(dic.copy())
q=deque()
while True:
    command=input().strip().split()
    if len(command)==1:
        if command[0]=='STOP':
            break
        number=q.popleft()
        print(number)
        for i in range(t):
            if number in teams[i]:
                teams[i][number]=0
        
    else:
        number=command[1]
        judge=0
        for i in range(t):
            if number in teams[i]:
                team=teams[i]
                last=-1
                for member in team:
                    if team[member]==1:
                        last=max(last,q.index(member))
                if last!=-1:
                    q.insert(last+1,number)
                    judge=1
                team[number]=1
        if judge==0:
            q.append(number)
        
    
        

        