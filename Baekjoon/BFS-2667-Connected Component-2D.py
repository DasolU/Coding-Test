# BAEKJOON
# 2667
# 단지번호붙이기
# BFS: connected component(연결 요소) 개수 구하기+ 연결 요소에 연결된 정점 개수 구하기
"""Final Solution: Solution 1
메모리: 32828 KB
시간: 88 ms
"""

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

graph=[]
for i in range(n):
    line = input().split() # returns list ex>['0110100']
    graph.append([])
    for j in line[0]:
        graph[i].append(int(j))


def bfs(y,x):
    q = deque([(y,x)])
    house = 1
    while q:
        node = q.popleft()
        y = node[0]
        x = node[1]

        if ((y - 1) >= 0) and (visited[y - 1][x]==0):
            visited[y - 1][x]=1
            if graph[y-1][x] == 1:
                q.append((y-1,x))
                house+=1
        if ((x - 1) >= 0) and (visited[y][x-1] == 0):
            visited[y][x-1]=1
            if graph[y][x-1] == 1:
                q.append((y,x-1))
                house += 1
        if ((y + 1) <= n-1) and (visited[y+1][x]) == 0:
            visited[y+1][x] = 1
            if graph[y+1][x] == 1:
                q.append((y+1, x))
                house += 1
        if ((x + 1) <= n-1) and (visited[y][x+1]) == 0:
            visited[y][x + 1] = 1
            if graph[y][x + 1] == 1:
                q.append((y, x + 1))
                house += 1
    return house

visited = [[0]*n for _ in range(n)]
connected = 0
house_list = []
for y in range(n):
    for x in range(n):
        if visited[y][x]==0 and graph[y][x]==1:
            visited[y][x] = 1
            house_list.append(bfs(y,x))
            connected+=1
print(connected)
for i in sorted(house_list):
    print(i, end='\n')