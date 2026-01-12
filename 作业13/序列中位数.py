from heapq import *
A=[]#小的一半的相反数，从而堆顶是小的一半中最大数的相反数
B=[]
def add(num):
    if len(A)>len(B):
        heappush(A,-num)
        heappush(B,-heappop(A))
    else:
        heappush(B,num)
        heappush(A,-heappop(B))

n=int(input().strip())
l=list(map(int,input().strip().split()))
i=0
while i<n:
    add(l[i])
    if i%2==0:
        if len(A)==len(B):
            m=(B[0]-A[0])/2
        else:
            m=-A[0]
        print(m)
    i+=1