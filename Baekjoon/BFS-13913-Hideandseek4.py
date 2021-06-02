# BAEKJOON
# 13913
# 숨바꼭질 4
# BFS: 찾을 수 있는 가장 빠른 시간

"""Final Solution 1: Solution 3
재귀를 사용하지 않고 반복문을 사용해보자.
메모리: 41364 KB
시간: 236 ms
"""
import sys
from collections import deque

def bfs():
    q = deque([n])
    while q:
        node = q.popleft()
        if node == k:
            return visited[k]
        for child in [node-1, node+1, node*2]:
            if 0<=child<=100000 and visited[child]==0:
                q.append(child)
                visited[child] = visited[node] +1
                parent[child] = node

input = sys.stdin.readline
n, k = map(int, input().split())
max = 100000
visited = [0] * (max+1)
parent = [-1] * (max+1)
time = bfs()
print(time)

move = [k]
for _ in range(time):
    new = move[-1]
    move.append(parent[new])
for _ in move[::-1]:
    print(_, end=" ")

"""Final Solution 2: Solution 4
list print를 print(' '.join(map(str, list))) 방법 사용해보자.
메모리 사용은 증가하고 시간은 단축됐다.

메모리: 48292 KB
시간: 204 ms
"""
import sys
from collections import deque

def bfs():
    q = deque([n])
    while q:
        node = q.popleft()
        if node == k:
            print(visited[k])
            return
        for child in [node-1, node+1, node*2]:
            if 0<=child<=100000 and visited[child]==0:
                q.append(child)
                visited[child] = visited[node] +1
                parent[child] = node

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [0] * (100001)
parent = [-1] * (100001)
bfs()

move = [k]
for _ in range(visited[k]):
    new = move[-1]
    move.append(parent[new])
print(' '.join(map(str,move[::-1])))

"""
Solution 1
실패
BFS 방법을 사용하면 방문한 node를 모두 저장하게 된다.
하지만 문제에서 필요한 것은 답으로 이동하는 직접적인 경로이다. 
해결 방안> DFS 방법으로 구현해야할 것 같다.
"""
# import sys
# from collections import deque
#
# def bfs():
#     q = deque([n])
#     while q:
#         ct = 0
#         node = q.popleft()
#         if node == k:
#             return visited[node]
#         else:
#             if 0<=node-1<=100000 and visited[node-1]==0:
#                 q.append(node-1)
#                 visited[node - 1] = visited[node] +1
#                 ct+=1
#             if 0<=node+1<=100000 and visited[node+1]==0:
#                 q.append(node+1)
#                 visited[node + 1] = visited[node] +1
#                 ct += 1
#             if 0<=node*2<=100000 and visited[node*2]==0:
#                 q.append(node*2)
#                 visited[node*2] = visited[node] +1
#                 ct += 1
#             if ct:
#                 visitlist.append(node)
#
# input = sys.stdin.readline
# n, k = map(int, input().split())
# max = 100000
# visited = [0] * (max+1)
# visitlist = []
# print(bfs())
# for i in visitlist:
#     print(i, end=" ")

"""Solution 2
예제 성공
실패 recursion error
"""
#
# import sys
# from collections import deque
#
# def bfs():
#     q = deque([n])
#     while q:
#         node = q.popleft()
#         if node == k:
#             return
#         for child in [node-1, node+1, node*2]:
#             if 0<=child<=100000 and visited[child]==0:
#                 q.append(child)
#                 visited[child] = visited[node] +1
#                 parent[child] = node
#
# def findparent(node):
#     move.append(node)
#     parentnode = parent[node]
#     if parentnode == n:
#         move.append(n)
#         return
#     else:
#         findparent(parentnode)
#
# input = sys.stdin.readline
# n, k = map(int, input().split())
# max = 100000
# visited = [0] * (max+1)
# parent = [-1] * (max+1)
# move = []
#
# bfs()
# print(visited[k])
# findparent(k)
# for _ in move[::-1]:
#     print(_, end=" ")
