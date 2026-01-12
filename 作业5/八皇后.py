import copy
def dfs(i,s,l):
    if i==8:
        ans.append(s)
        return
    for j in range(8):
        if l[i][j]:
            lj=copy.deepcopy(l)
            k=i+1
            while k<8:
                lj[k][j]=False
                if k-i+j<8:
                    lj[k][k-i+j]=False
                if j-(k-i)>=0:
                    lj[k][j-k+i]=False
                k+=1
            dfs(i+1,s+str(j+1),lj)
ans=[]
l=[[True]*8 for _ in range(8)]
dfs(0,'',l)
n=int(input())
for _ in range(n):
    num=int(input())
    print(ans[num-1])