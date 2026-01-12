t=int(input().strip())
num=0
def f(n):
    global num
    jud=0
    i=0
    while i<len(n)-1 and num<k:
        if n[i+1]<n[i]:
            jud=1
            del n[i]
            i-=1
            num+=1
        i+=1
    return jud

for _ in range(t):
    n,k=input().strip().split()
    n=list(n)
    k=int(k)
    num=0
    while f(n):
        continue
    if num<k:
        for _ in range(k-num):
            del n[-1]
    s=''
    for a in n:
        s+=a
    print(int(s))