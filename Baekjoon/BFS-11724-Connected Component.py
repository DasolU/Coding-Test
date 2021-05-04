# BAEKJOON
# 11724
# 연결 요소의 개수
# 알고리즘: 연결 요소 (Connected Component)의 개수를 구하기->BFS
# 구현: 모든 노드를 방문해봐야 아나? 모든 노드를 방문하도록 하되, 방문했던 노드의 방문을 막으면 된다.
# 예상 연결 요
# 예제 1
# {1: [2, 5], 2: [1, 5], 5: [2, 1], 3: [4], 4: [3, 6], 6: [4]})
    #1-2-5
    #3-4-6
# 예제 2
# {1: [2, 5], 2: [1, 5, 4, 3], 5: [2, 1, 4], 3: [4, 2], 4: [3, 6, 5, 2], 6: [4]})
    # 1-2-5-4-3-6

"""Final Solution:Solution 2-1
메모리:62968 KB
시간:824 ms
배운점>
1. graph를 만드는 효율적인 방법
from collections import defaultdict을 사용한
-> graph=defaultdict(list)은 시간이 더 오래 걸린다.
graph=[[]for i in range(N+1)]가 더 빠르다.
2. q를 정의하는 방법
q=deque([v])
v=q.popleft()
메모리도 더 사용하고 시간도 더 오래걸린다!
이론적으로 이해가 되지 않는다.
3. print에서 시간 단축하는 방법
sys.stdout.write(str(answer))를 사용하니 시간이 단축됨을 확인했다.
"""

import sys

N,M=map(int,sys.stdin.readline().split())

graph=[[]for i in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visit_list=[0]*(N+1)

def bfs(v):
    q=[v]
    while q:
        v=q.pop(0)
        visit_list[v] = 1
        for i in graph[v]:
            if visit_list[i]==0:
                q.append(i)
                visit_list[i]=1

answer=0
for i in range(1,N+1):
    if visit_list[i]==0:
        bfs(i)
        answer+=1

sys.stdout.write(str(answer))
"""Solution 1
메모리: 67324
시간: 8616
"""
# import sys
# from collections import defaultdict
# from collections import deque
#
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = defaultdict(list)
#
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# total_visited=[False for _ in range(n+1)]
# def bfs(node):
#     q = deque([node])
#     visited = []
#     while q:
#         n = q.popleft()
#         if n not in visited:
#             for child in graph[n]:
#                 if child not in visited:
#                     q.append(child)
#             visited.append(n)
#             total_visited[n]=True
#     return visited
#
# answer=0
# for node in range(1,n+1):
#     if not total_visited[node]:
#         visited = bfs(node)
#         if len(visited):
#             # print('visited',visited)
#             answer+=1
# print(answer)
"""Solution 2
메모리: 	62968
시간: 832
"""
# import sys
#
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = [[] for i in range(n+1)]
#
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# visited=[False]*(n+1)
# def bfs(node):
#     q = [node]
#     while q:
#         n = q.pop(0)
#         visited[n]=True
#
#         for child in graph[n]:
#             if not visited[child]:
#                 q.append(child)
#                 visited[child]=True
#
# answer=0
# for node in range(1,n+1):
#     if not visited[node]:
#         bfs(node)
#         answer+=1
# print(answer)