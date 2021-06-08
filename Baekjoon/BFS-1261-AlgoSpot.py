# BAEKJOON
# 1261
# 알고스팟
# BFS : 최소 몇 개 부수어야 하는지
"""Solution 1
메모리:  KB
시간: ms
구현 고민>
최단 경로가 최단 부수기 경로와 일치하지 않을 경우?
최단 경로는 아니지만 1을 만나는 횟수가 가장 작은 경로를 찾아야 한다.
"""
import sys
from collections import deque

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    while q:
        (y, x) = q.popleft()
        if x==m-1 and y==n-1:
            print(visited[y][x])
            return
        for i in range(4):
            ny, nx= y+dy[i], x+dx[i]
            if 0<=nx<m and 0<=ny<n and visited[ny][nx] == -1:
                if graph[ny][nx] == '1':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
                else:
                    visited[ny][nx] = visited[y][x]
                    q.appendleft((ny, nx))

input = sys.stdin.readline
m, n = map(int, input().split())
visited = [[-1]*(m) for _ in range(n)]
graph = [[0]*(m) for _ in range(n)]
for h in range(n):
    line = input().split()
    for i in range(m):
        graph[h][i] = line[0][i]
dx = [1,0, -1, 0]
dy = [0, 1, 0, -1]
bfs()

