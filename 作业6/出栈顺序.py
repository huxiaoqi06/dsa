import sys
sys.setrecursionlimit(2001)
n=int(input())
dic={}
def f(nums_in_stack,n1,n2):
    if nums_in_stack<0:
        return 0
    if n1==n2==n:
        return 1
    if n1>n or n2>n:
        return 0
    if (nums_in_stack,n1,n2) not in dic:
        dic[(nums_in_stack,n1,n2)]=f(nums_in_stack-1,n1,n2+1)+f(nums_in_stack+1,n1+1,n2)
    return dic[(nums_in_stack,n1,n2)]
print(f(0,0,0))

