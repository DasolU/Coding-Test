# BAEKJOON
# 7562
# 나이트의 이동
# BFS : 최소 몇 번 만에 목표에 도착할 수 있는가?

"""Final Solution: Solution 1
메모리:  32460 KB
시간: 2696 ms
배운 점 1> queue에 2D node를 queue에 넣을 때는 시간 단축을 위해서,q.append((sy, sx))와 (y, x) = q.popleft()를 사용하자.
    q.append([sy, sx])와 y, x = q.popleft()은 시간이 더 걸린다.
    두 가지 방법 모두 [2D node, 2D node...] 처럼 추가되는 것은 동일하지만,
    node를 pop해서 읽을 때 시간 차이가 나는 것으로 추측된다.

배운점 2> 노드 방문 여부를 확인할 때 가능한을 등호를 포함하지 않는 비교 부호인 < 또는 > 을 사용하자!!
if 0<=nx<=l-1 and 0<=ny<=l-1 보다 if 0<=nx<l and 0<=ny<l이 시간 효율이 높다.
이유는 l-1 연산을 하지 않아도 되기 때문에!!

배운점 3>
q = deque([(sy, sx)])보다 q = deque()로 정의하고 추가하는 것이 q.append((sy, sx)) 메모리 효율이 높다.
따라서 2D node를 queue에 넣을 때는
1. q = deque()
2. q.append((sy, sx))
3. (y, x) = q.popleft()
4. q.append((ny, nx))
"""
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]
def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 0
    while q:
        (y, x) = q.popleft()
        if x==ex and y==ey:
            print(visited[y][x])
            return
        for i in range(8):
            ny, nx= y+dy[i], x+dx[i]
            if 0<=nx<l and 0<=ny<l and visited[ny][nx] == -1:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

tc = int(input())
for _ in range(tc):
    l = int(input())
    visited = [[-1] * l for _ in range(l)]
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    bfs(sx, sy, ex, ey)
"""Solution 2
메모리:  32460 KB
시간: 2752 ms
"""
# import sys
# from collections import deque
# input = sys.stdin.readline
# dx = [-1,-2,-2,-1,1,2,2,1]
# dy = [2,1,-1,-2,-2,-1,1,2]
# def bfs(sx, sy, ex, ey):
#     q = deque()
#     q.append([sy, sx])
#     visited[sy][sx] = 0
#     while q:
#         y, x = q.popleft()
#         if x==ex and y==ey:
#             print(visited[y][x])
#             return
#         for i in range(8):
#             ny, nx= y+dy[i], x+dx[i]
#             if 0<=nx<l and 0<=ny<l and visited[ny][nx] == -1:
#                 q.append([ny, nx])
#                 visited[ny][nx] = visited[y][x] + 1
#
# tc = int(input())
# for _ in range(tc):
#     l = int(input())
#     visited = [[-1] * l for _ in range(l)]
#     sx, sy = map(int,input().split())
#     ex, ey = map(int,input().split())
#     bfs(sx, sy, ex, ey)

"""Solution 1
메모리:  32460 KB
시간: 2776 ms
"""
# import sys
# from collections import deque
# input = sys.stdin.readline
# dx = [-1,-2,-2,-1,1,2,2,1]
# dy = [2,1,-1,-2,-2,-1,1,2]
# def bfs(sx, sy, ex, ey):
#     q = deque()
#     q.append((sy, sx))
#     visited[sy][sx] = 0
#     while q:
#         (y, x) = q.popleft()
#         if x==ex and y==ey:
#             print(visited[y][x])
#             return
#         for i in range(8):
#             ny, nx= y+dy[i], x+dx[i]
#             if 0<=nx<=l-1 and 0<=ny<=l-1 and visited[ny][nx] == -1:
#                 q.append((ny, nx))
#                 visited[ny][nx] = visited[y][x] + 1
#
# tc = int(input())
# for _ in range(tc):
#     l = int(input())
#     visited = [[-1] * l for _ in range(l)]
#     sx, sy = map(int,input().split())
#     ex, ey = map(int,input().split())
#     bfs(sx, sy, ex, ey)
