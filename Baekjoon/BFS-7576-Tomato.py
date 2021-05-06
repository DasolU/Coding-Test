# BAEKJOON
# 7576
# 토마토
# BFS: 며칠이 지나면 다 익게 되는지, 그 최소 일수
# 단지번호붙이기, 미로탐색과 비슷한 유형
"""Final Solution: Solution 1
메모리: 107056 KB
시간: 2308 ms
몰랐던 점> 모든 시작점들에서 동시에 bfs를 진행하는 방법.
동시에 하기 위해서는 queue안에 모든 시작점을 올리면 된다.
그렇다면 차례로 bfs를 진행하게된다.
"""
# import sys
# from collections import deque
# import numpy as np
#
# def find_start(n,m):
#     numoffalse = 0
#     for y in range(n):
#         for x in range(m):
#             if graph[y][x]==1:
#                 q.append((y,x))
#                 visited[y][x]=1
#             if graph[y][x]==-1:
#                 numoffalse+=1
#                 visited[y][x]=-1
#     numoftrue = len(q)
#     return (numoftrue, numoffalse)
#
# def check_all_visited(n):
#     for i in range(n):
#         if not all(visited[i]):
#             return False
#     return True
#
# def find_max(n,m):
#     maxlist = []
#     for i in range(n):
#         maxlist.append(max(visited[i]))
#     answer = sorted(maxlist, reverse=True)[0] - 1
#     return answer
#
# def bfs():
#     while q:
#         (y, x) = q.popleft()
#         # print(y, x)
#         nbr_list = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
#         for nbr in nbr_list:
#             (ny, nx) = nbr
#             if (ny >= 0) and (ny <= n - 1) and (nx >= 0) and (nx <= m - 1):
#                 if visited[ny][nx] == 0 and graph[ny][nx] == 0:
#                     q.append((ny, nx))
#                     visited[ny][nx] = visited[y][x] + 1
#         # print(np.matrix(visited))
#
# input = sys.stdin.readline
# m,n = map(int, input().split())
# graph = []
# for i in range(n):
#     line = input().split()
#     graph.append([])
#     for j in line:
#         graph[i].append(int(j))
# visited = [[0] * m for _ in range(n)]
#
# q = deque()
# (numoftrue, numoffalse)=find_start(n,m)
# if n*m-numoftrue == numoffalse:
#     print(0)
# else:
#     bfs()
#     if check_all_visited(n):
#         print(find_max(n, m))
#     else:
#         print(-1)

"""Solution 2
Solution 1에서 시간단축하고자 함.
함수를 제거하고 반복되는 for loop를 합쳤는데, 메모리와 시간이 늘어남. 왜지?  
메모리: 107644 KB
시간: 2664 ms
"""
# import sys
# from collections import deque
#
# def check_all_visited(n):
#     for i in range(n):
#         if not all(visited[i]):
#             return False
#     return True
#
# def find_max(n,m):
#     maxlist = []
#     for i in range(n):
#         maxlist.append(max(visited[i]))
#     answer = sorted(maxlist, reverse=True)[0] - 1
#     return answer
#
# def bfs():
#     while q:
#         (y, x) = q.popleft()
#         nbr_list = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
#         for nbr in nbr_list:
#             (ny, nx) = nbr
#             if (ny >= 0) and (ny <= n - 1) and (nx >= 0) and (nx <= m - 1):
#                 if visited[ny][nx] == 0 and graph[ny][nx] == 0:
#                     q.append((ny, nx))
#                     visited[ny][nx] = visited[y][x] + 1
#
# input = sys.stdin.readline
# m,n = map(int, input().split())
# graph = []
# q = deque()
# visited = [[0] * m for _ in range(n)]
#
# numoffalse = 0
# for y in range(n):
#     line = input().split()
#     graph.append([])
#     for x in range(m):
#         graph[y].append(int(line[x]))
#         if int(line[x]) == 1:
#             q.append((y, x))
#             visited[y][x] = 1
#         if int(line[x]) == -1:
#             numoffalse += 1
#             visited[y][x] = -1
#     numoftrue = len(q)
#
# if n*m-numoftrue == numoffalse:
#     print(0)
# else:
#     bfs()
#     if check_all_visited(n):
#         print(find_max(n, m))
#     else:
#         print(-1)