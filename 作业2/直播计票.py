from collections import defaultdict
l=list(map(int,input().split()))
dic=defaultdict(int)
for i in range(len(l)):
    dic[l[i]]+=1
l1=[]
for key in dic:
    l1.append([dic[key],key])
l1.sort(key=lambda x:(-x[0],x[1]))
i=0
ans=[]
while i<len(l1) and l1[i][0]==l1[0][0]:
    ans.append(l1[i][1])
    i+=1
print(*ans)