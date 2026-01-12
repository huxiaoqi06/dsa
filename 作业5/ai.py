from collections import deque

R, C, K = map(int, input().split())
grid = []
start = None

for i in range(R):
    line = input().strip()
    grid.append(line)
    if 'S' in line:
        start = (i, line.index('S'))

# 三维距离数组：dist[r][c][k] = 到达 (r,c) 且使用 k 次闪现的最小步数
INF = float('inf')
dist = [[[INF] * (K+1) for _ in range(C)] for __ in range(R)]

# BFS
q = deque()
sr, sc = start
dist[sr][sc][0] = 0
q.append((sr, sc, 0))  # (r, c, k_used)

dirs = [(-1,0), (1,0), (0,-1), (0,1)]
found = False
answer = -1

while q:
    r, c, k_used = q.popleft()
    steps = dist[r][c][k_used]
    
    if grid[r][c] == 'E':
        found = True
        answer = steps
        break

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            nk = k_used
            if grid[nr][nc] == '#':
                nk += 1
                if nk > K:
                    continue
            # 如果这个状态有更优解，跳过
            if steps + 1 < dist[nr][nc][nk]:
                dist[nr][nc][nk] = steps + 1
                q.append((nr, nc, nk))

print(answer if found else -1)
