n=int(input().strip())
l=[]
for i in range(n):
    l.append(list(map(str,input().strip().split())))
    l[i][0]=i+1
m=int(input().strip())
for i in range(m):
    word=input().strip()
    ans=[]
    for j in range(n):
        if word in l[j]:
            ans.append(int(l[j][0]))
    if ans!=[]:
        print(*ans)
    else:
        print('NOT FOUND')