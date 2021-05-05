# BAEKJOON
# 2178
# 미로 탐색
# BFS:(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수
# 단지 수 세기 문제와 같은 유형이다.
# 좌,우,상,하 방향으로 인접한 node의 값을 조사해야하기 때문에.
# 다른 점은 연결된 모든 1 개수를 세는 것이 아니다.
# 최단 경로를 구해야 한다. -> BFS

"""Final Solution: Solution 2-2-1
메모리: 31736 KB
시간: 104 ms
Solution 2-2-1을 발전시켜 시간과 메모리 단축 시도.
배운 점>
몰라서 못풀었던 포인트> level을 세는 방법
1. 내가 사용한 방법:
* bfs를 사용하며 level=0 으로 두고 다음 level로 넘어갈 때 level+=1로 하나씩 추가하려 했다.
* 이러한 방법은 언제 level을 추가해야되는지 경우를 하나하나 고민하며 예외를 생각하는 복잡한 과정이 필요했다.
2. 더 좋은 방법: visited를 사용하자!!!!
* 즉, visited에 0 or 1만 넣지 말고, level 또는 다양한 flag 값을 넣자.
* 이 문제에서는 모든 자식 노드의 visited 값에 부모 노드의 visited 값에 1을 추가하여,
  자식 노드라면 같은 level을 가지도록 했다.
  따라서 목표 노드에 도달했을 때 level을 자연스럽게 셀 수 있으며,
  같은 level에 있는 자식 노드 처리를 따로 하지 않아도 된다.
"""
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    line = input().split()  # returns list ex>['0110100']
    graph.append(line[0])
visited = [[0] * m for _ in range(n)]
def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        node = q.popleft()
        y, x = node[0], node[1]
        if (y == n - 1) and (x == m - 1):
            return print(visited[y][x])
        nbr_list = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
        for nbr in nbr_list:
            (ny, nx) = nbr
            if (ny >= 0) and (ny <= n - 1) and (nx >= 0) and (nx <= m - 1):
                if visited[ny][nx] == 0 and graph[ny][nx] == '1':
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
bfs()

"""Solution 1
예제 1만 통과
"""
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph=[]
# for i in range(n):
#     graph.append([])
#     line = input().split() # returns list ex>['0110100']
#     for j in line[0]:
#         graph[i].append(int(j))
#
# visited = [[0]*m for _ in range(n)]
# # print(graph)
# # print(visited)
# def bfs():
#     q = deque([(0,0)])
#     path = []
#     answer = 0
#     while q:
#         flag = False
#         node = q.popleft()
#         y,x = node[0], node[1]
#         if (y==n-1) and (x==m-1):
#             # print('=======')
#             # print(path)
#             # return print(len(path))
#
#         if visited[y][x]==0:
#             visited[y][x] = 1
#             if ((y - 1) >= 0) and (visited[y - 1][x] == 0):
#                 if graph[y - 1][x] == 1:
#                     q.append((y - 1, x))
#                     flag = True
#             if ((x - 1) >= 0) and (visited[y][x - 1] == 0):
#                 if graph[y][x - 1] == 1:
#                     q.append((y, x - 1))
#                     flag = True
#             if ((y + 1) <= n-1) and (visited[y + 1][x] == 0):
#                 if graph[y + 1][x] == 1:
#                     q.append((y + 1, x))
#                     flag = True
#             if ((x + 1) <= m-1) and (visited[y][x + 1] == 0):
#                 if graph[y][x + 1] == 1:
#                     q.append((y, x + 1))
#                     flag = True
#             # if flag:
#             #     answer += 1
#             #     path.append((y,x))
# bfs()

"""Solution 2
bfs로 했으나 문제 발생.
문제>
bfs는 모든 자식 노드를 조사하고 다음 level로 넘어가기 때문에 불필요한 이동이 생긴다.
예를 들어 부모 노드가 node (0, 4)인 경우 2개의 자식 노드가 있다.
자식 노드인 node (1, 4)와 node (0, 5) 중 최단 경로로 가는 것은 node (1, 4)이므로
node (0, 5)방문은 불필요하지만 queue의 선입선출 방식 때문에 방문하게 된다.
해결 방법 생각> 같은 부모 노드를 가진 자식 노드들의 방문이 완료될 때까지 level을 count하지 않는다.
"""
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append([])
#     line = input().split()  # returns list ex>['0110100']
#     for j in line[0]:
#         graph[i].append(int(j))
#
# visited = [[0] * m for _ in range(n)]
#
# def bfs():
#     q = deque([(0, 0)])
#     level = 1
#     while q:
#         node = q.popleft()
#         y, x = node[0], node[1]
#         if visited[y][x] == 0:
#             print('node',node)
#             visited[y][x] = 1
#             level+=1
#
#             nbr_list = [(y - 1,x),(y,x - 1),(y + 1,x),(y,x + 1)]
#             ct=0
#             for nbr in nbr_list:
#                 (ny,nx) = nbr
#                 if (ny >= 0) and (ny<=n-1) and (nx >= 0) and (nx <= m - 1):
#                     if visited[ny][nx] == 0:
#                         if graph[ny][nx] == 1:
#                             if (ny == n - 1) and (nx == m - 1):
#                                 level+=1
#                                 return print(level)
#                             q.append((ny, nx))
#                             ct += 1
#                             visited[ny][nx] == 1
#             if ct>=2:
#                 level=level-(n-1)
# bfs()
"""Solution 2-1
최단 경로를 찾기 위해 bfs를 사용하고 level을 적재 적소에 추가하는 코드를 작성하려고 함.
하지만 생각 도중 경우의 수가 많게 느껴지고 간단하게 정리가 되지 않아서 실패,
    # level이 추가 되어야 할 때?
    # >부모 노드의 모든 자식 노드의 탐색이 끝났는데 답을 발견하지 못했을 때->다음 level로 넘어가면서 추가
    # 다음 level로 넘어갈 때는 언제인가?
    # >자식 노드 개수만큼 q에서 pop했는데 답을 못찼았을 때.
    """
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append([])
#     line = input().split()  # returns list ex>['0110100']
#     for j in line[0]:
#         graph[i].append(int(j))
#
# visited = [[0] * m for _ in range(n)]
#
# level = 0
# def find_son(y,x,q):
#     global level
#     nbr_list = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
#     son = 0
#     for nbr in nbr_list:
#         (ny, nx) = nbr
#         if (ny >= 0) and (ny <= n - 1) and (nx >= 0) and (nx <= m - 1):
#             if visited[ny][nx] == 0:
#                 if graph[ny][nx] == 1:
#                     # if (ny == n - 1) and (nx == m - 1):
#                     #     level += 1
#                     #     return False
#                     son += 1
#                     q.append((ny, nx))
#                     visited[ny][nx] == 1
#     return son
#
# def bfs():
#     global level
#     q = deque([(0, 0)])
#     level+=1
#     son = False
#     while q:
#         if son:
#             for _ in range(son):
#                 node = q.popleft()
#                 y, x = node[0], node[1]
#                 if visited[y][x] == 0:
#                     print('---------------')
#                     print('node',node)
#
#                     if (y == n - 1) and (x == m - 1):
#                         return level
#
#                     son = find_son(y, x, q)
#                     visited[y][x] = 1
#             level+=1
#         else: # son=0
#             node = q.popleft()
#             y, x = node[0], node[1]
#             if visited[y][x] == 0:
#                 print('---------------')
#                 print('node', node)
#
#                 if (y == n - 1) and (x == m - 1):
#                     return level
#
#                 son = find_son(y, x, q)
#                 visited[y][x] = 1
# bfs()
"""Solution 2-2
메모리: 32764 KB
시간: 108 ms
몰라서 못풀었던 포인트> level을 세는 방법
1. 내가 사용한 방법: 
* level=0 으로 두고 다음 level로 넘어갈 때 level+=1로 하나씩 추가하려 했다.
* 이러한 방법은 언제 level을 추가해야되는지 경우를 하나하나 고민하며 예외를 생각하는 복잡한 과정이 필요했다.
2. 더 좋은 방법: visited를 사용하자!!!!
* 즉, visited에 0 or 1만 넣지 말고, level 또는 다양한 flag 값을 넣자.  
"""
#
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append([])
#     line = input().split()  # returns list ex>['0110100']
#     for j in line[0]:
#         graph[i].append(int(j))
#
# def find_son(y,x):
#     nbr_list = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
#     for nbr in nbr_list:
#         (ny, nx) = nbr
#         if (ny >= 0) and (ny <= n - 1) and (nx >= 0) and (nx <= m - 1):
#             if visited[ny][nx] == 0 and graph[ny][nx] == 1:
#                 q.append((ny, nx))
#                 visited[ny][nx] = visited[y][x] + 1
#
# def bfs():
#     q.append((0, 0))
#     visited[0][0] = 1
#     while q:
#         node = q.popleft()
#         y, x = node[0], node[1]
#         if (y == n - 1) and (x == m - 1):
#             return print(visited[y][x])
#         find_son(y, x)
#
# visited = [[0] * m for _ in range(n)]
# q = deque()
# bfs()

"""Solution 3
예제 실패
DFS로 구현해도 node (0, 4)에서 node (0, 5)으로 불필요한 이동(정답이 없는 노드로 이동)을 하는 경우가 생긴다.
또한 DFS는 답이 최단 경로가 아닐 수 있다.
# """
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append([])
#     line = input().split()  # returns list ex>['0110100']
#     for j in line[0]:
#         graph[i].append(int(j))
#
# visited = [[0] * m for _ in range(n)]
#
# def dfs():
#     q = deque([(0, 0)])
#     answer_list = []
#     answer = []
#     while q:
#         node = q.pop()
#         y, x = node[0], node[1]
#         if visited[y][x] == 0:
#             print('node', node)
#             answer.append((y, x))
#             visited[y][x] = 1
#
#             nbr_list = [(y - 1,x),(y,x - 1),(y + 1,x),(y,x + 1)]
#             for nbr in nbr_list:
#                 (ny,nx) = nbr
#                 if (ny >= 0) and (ny<=n-1) and (nx >= 0) and (nx <= m - 1):
#                     if visited[ny][nx] == 0:
#                         if graph[ny][nx] == 1:
#                             if (ny == n - 1) and (nx == m - 1):
#                                 answer.append((ny, nx))
#                                 answer_list.append(len(answer))
#                                 answer=[]
#                                 break
#                             else:
#                                 q.append((ny, nx))
#                                 visited[ny][nx] == 1
#     return answer_list #[16, 2]
# print(dfs())