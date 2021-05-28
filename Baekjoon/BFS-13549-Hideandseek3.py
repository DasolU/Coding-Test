# BAEKJOON
# 13549
# 숨바꼭질 3
# BFS: 가장 빠른 시간이 몇 초 후인지 구하는 프로그램

"""Final Solution 1: Solution 4
메모리: 35380 KB
시간: 168 ms
의문점> q.appendleft(node * 2)에 대하여
append left 해도 안해도 답을 찾는 시간엔 영향이 없었다.
"""
import sys
from collections import deque

def bfs(n):
    q = deque([n])
    visited[n]=0
    while q:
        node = q.popleft()
        if node == k:
            return visited[node]
        if node * 2 >= 0 and node * 2<=100000 and visited[node * 2] == -1:
            if node * 2 == k:
                return visited[node]
            visited[node * 2]=visited[node]
            q.append(node * 2)
        if node - 1 >= 0 and node - 1<=100000 and visited[node - 1] == -1:
            if node - 1 == k:
                return visited[node]+1
            visited[node - 1] = visited[node] + 1
            q.append(node - 1)
        if node + 1 >= 0 and node + 1 <= 100000 and visited[node + 1] == -1:
            if node + 1 == k:
                return visited[node]+1
            visited[node + 1] = visited[node] + 1
            q.append(node + 1)

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [-1]*(100001)
print(bfs(n))
"""Final Solution 2: Solution 5
메모리: 35684 KB
시간: 180 ms
배운점 1>
child node에서 답을 발견했을 때 바로 return하도록 해도 시간단축이 되지 않는다.
배운점 2>
child node를 리스트에 담아 for문으로 조사하는 방식은 시간과 메모리를 더 사용한다.
"""
import sys
from collections import deque

def bfs(n):
    q = deque([n])
    visited[n]=0
    while q:
        node = q.popleft()
        if node == k:
            return visited[node]
        for idx, child in enumerate([node * 2, node - 1, node + 1]):
            if child >= 0 and child<=100000 and visited[child] == -1:
                if idx == 0:
                    visited[child]=visited[node]
                    q.appendleft(child)
                else:
                    visited[child]=visited[node]+1
                    q.append(child)

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [-1]*(100001)
print(bfs(n))
# import sys
# from collections import deque
#
# def bfs(n):
#     q = deque([n])
#     visited[n]=0
#     while q:
#         node = q.popleft()
#         if node == k:
#             return visited[node]
#         if node * 2 >= 0 and node * 2<=100000 and visited[node * 2] == -1:
#             if node * 2 == k:
#                 return visited[node]
#             visited[node * 2]=visited[node]
#             q.appendleft(node * 2)
#         if node - 1 >= 0 and node - 1<=100000 and visited[node - 1] == -1:
#             if node - 1 == k:
#                 return visited[node]+1
#             visited[node - 1] = visited[node] + 1
#             q.append(node - 1)
#         if node + 1 >= 0 and node + 1 <= 100000 and visited[node + 1] == -1:
#             if node + 1 == k:
#                 return visited[node]+1
#             visited[node + 1] = visited[node] + 1
#             q.append(node + 1)
#
# input = sys.stdin.readline
# n, k = map(int, input().split())
# visited = [-1]*(100001)
# print(bfs(n))
"""Solution 1
시간초과
"""
# import sys
# from collections import deque
#
# def bfs(n):
#     q = deque([n])
#     while q:
#         node = q.popleft()
#         # print('node, time ', node, visited[node])
#         if node == k:
#             return visited[node]
#         next = [node - 1, node + 1, node * 2]
#         for idx, child in enumerate(next):
#             if child >= 0 and child<=100000:
#                 if visited[child] == 0:
#                     if idx == 0 or idx==1:
#                         visited[child]=visited[node]+1
#                         q.append(child)
#                     if idx == 2:
#                         visited[child]=visited[node]
#                         q.appendleft(child)
# input = sys.stdin.readline
# n, k = map(int, input().split())
# visited = [0]*(100001)
# print(bfs(n))
"""Solution 2
시간초과
"""
# import sys
# from collections import deque
#
# def bfs(n):
#     q = deque([n])
#     while q:
#         node = q.popleft()
#         if node == k:
#             return visited[node]
#         next = [node - 1, node + 1, node * 2]
#         for idx, child in enumerate(next):
#             if child >= 0 and child<=100000 and visited[child] == 0:
#                 if idx == 2:
#                     visited[child]=visited[node]
#                     q.appendleft(child)
#                 else:
#                     visited[child]=visited[node]+1
#                     q.append(child)
# input = sys.stdin.readline
# n, k = map(int, input().split())
# visited = [0]*(100001)
# print(bfs(n))
"""Solution 3
시간초과
# """
# import sys
# from collections import deque
#
# def bfs(n):
#     q = deque([n])
#     while q:
#         node = q.popleft()
#         next = [node - 1, node + 1, node * 2]
#         for idx, child in enumerate(next):
#             if child >= 0 and child<=100000 and visited[child] == 0:
#                 if child == k:
#                     if idx == 2:
#                         return visited[node]
#                     else:
#                         return visited[node]+1
#                 else:
#                     if idx == 2:
#                         visited[child]=visited[node]
#                         q.appendleft(child)
#                     else:
#                         visited[child]=visited[node]+1
#                         q.append(child)
# input = sys.stdin.readline
# n, k = map(int, input().split())
# visited = [0]*(100001)
# print(bfs(n))

