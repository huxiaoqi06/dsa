n,m=map(int,input().split())
ans=[]
for _ in range(m):
    ans.append(list(map(int,input().split())))
A={}
B={}
answer=1

while ans:
    judge=0
    i=0
    while i<len(ans):
        a,b,j=ans[i]
        if a in A:
            judge=1
            if j:
                B[b]=1
                if b in A:
                    answer=0
            else:
                A[b]=1
                if b in B:
                    answer=0
            del ans[i]
            continue

        if a in B:
            judge=1
            if j:
                A[b]=1
                if b in B:
                    answer=0
            else:
                B[b]=1
                if b in A:
                    answer=0
            del ans[i]
            continue

        if b in A:
            judge=1
            if j:
                B[a]=1
                if a in A:
                    answer=0
            else:
                A[a]=1
                if a in B:
                    answer=0
            del ans[i]
            continue
        if b in B:
            judge = 1
            if j:
                A[a] = 1
                if a in B:
                    answer=0
            else:
                B[a] = 1
                if a in A:
                    answer=0
            del ans[i]
            continue
        i+=1
    if judge==0:
        jud=0
        for i in range(len(ans)):
            a,b,j=ans[i]
            if j:
                A[a]=1
                B[b]=1
                jud=1
                del ans[i]
                break
        if jud==0:
            break

if answer:
    print("YES")
else:
    print("NO")