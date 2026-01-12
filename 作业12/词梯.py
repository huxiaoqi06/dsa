from collections import defaultdict,deque
n=int(input().strip())

words=[]
for i in range(n):
    words.append(input().strip())
start,end=input().strip().split()


pattern_map=defaultdict(list)
for word in words:
    for i in range(4):
        pattern=word[:i]+'*'+word[i+1:]
        pattern_map[pattern].append(word)
graph=defaultdict(list)
for word in words:
    neighbors=set()
    for i in range(4):
        pattern=word[:i]+'*'+word[i+1:]
        for neighbor in pattern_map[pattern]:
            if neighbor!=word:
                neighbors.add(neighbor)
    graph[word]=list(neighbors)

history={}
for word in words:
    history[word]=float('inf')
q=deque()
q.append((start,[start],0))
judge=0
while q:
    word,path,steps=q.popleft()
    if word==end:
        judge=1
        break
    for next_word in graph[word]:
        if steps+1<history[next_word]:
            history[next_word]=steps+1
            q.append((next_word,path+[next_word],steps+1))
if judge:
    print(*path)
else:
    print('NO') 
#给单词编号会减少一点复杂度