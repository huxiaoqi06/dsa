n, m = 6, 11
edges_input = [
    (1,3),(1,4),(1,5),(1,6),
    (2,3),(2,4),(2,5),(2,6),
    (3,4),(3,5),(3,6)
]

parent = list(range(n))

def root(x):
    if parent[x] != x:
        parent[x] = root(parent[x])
    return parent[x]

def union(x, y):
    parent[root(x)] = root(y)
    root(x)

dic = set()
graph = []
for a, b in edges_input:
    i, j = a-1, b-1
    graph.append((i, j))
    dic.add((i, j))
    dic.add((j, i))

count = 0
print("Adding 0-weight edges:")
for i in range(n):
    for j in range(i, n):   # ⚠️ j from i
        if (i, j) not in dic:
            if root(i) != root(j):
                union(i, j)
                count += 1
                print(i, j, 0)
                if count == n-1:
                    break
    if count == n-1:
        break

ans = 0
print("Adding 1-weight edges:")
for i, j in graph:
    if root(i) != root(j):
        union(i, j)
        ans += 1
        count += 1
        print(i, j, 1)
        if count == n-1:
            break

print("ans =", ans)