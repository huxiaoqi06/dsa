n=int(input().strip())
for _ in range(n):
    s=input().strip()
    operator=[]
    output=[]
    ops={'+':0,'-':0,'*':1,'/':1}
    i=0
    l=len(s)
    while i<l:
        if '0'<=s[i]<='9':
            num=''
            while i<l and ('0'<=s[i]<='9' or s[i]=='.'):
                    num+=s[i]
                    i+=1
            i-=1
            output.append(num)
        elif s[i]=='(':
            operator.append('(')
        elif s[i]==')':
            while operator and operator[-1]!='(':
                output.append(operator.pop())
            operator.pop()
        else:
            while operator and operator[-1] in ops and ops[operator[-1]]>=ops[s[i]]:
                output.append(operator.pop())
            operator.append(s[i])
        i+=1
    while operator:
        output.append(operator.pop())
    print(*output)
