from collections import deque
from collections import defaultdict
from heapq import *
n=int(input().strip())
dq=deque()
A=[]
B=[]
to_del=defaultdict(int)
a=0
b=0

def balance():
    global a,b
    clean()
    if a==b+1:
        heappush(B,-heappop(A))
        a-=1
        b+=1
    if b==a+2:
        heappush(A,-heappop(B))
        b-=1
        a+=1
    clean()


def clean():
    while B and B[0] in to_del:
        to_del[B[0]]-=1
        if to_del[B[0]]==0:
            del to_del[B[0]]
        heappop(B)
    while A and -A[0] in to_del:
        to_del[-A[0]]-=1
        if to_del[-A[0]]==0:
            del to_del[-A[0]]
        heappop(A)

for _ in range(n):
    operation=input().strip()

    if operation=='del':
        num_to_del=dq.popleft()
        to_del[num_to_del]+=1
        if num_to_del>=B[0]:
            b-=1
        else:
            a-=1
        balance()#其实不需要用函数写，反正每次最多偏离1，只要平衡一下即可

    elif operation=='query':
        if b>a:
            print(B[0])
        else:
            m=(B[0]-A[0])/2
            print(int(m) if m.is_integer() else f'{m:.1f}')

    else:
        num=int(operation[4:])
        dq.append(num)
        if b>a:
            heappush(B,num)
            heappush(A,-heappop(B))
            a+=1
        else:
            heappush(A,-num)
            heappush(B,-heappop(A))
            b+=1
        clean()

        
