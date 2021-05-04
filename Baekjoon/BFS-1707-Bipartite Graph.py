# BAEKJOON
# 1707
# 이분 그래프
""" Final Solution: Solution 5
결과>
메모리: 51852 KB
시간: 1564 ms
잘못한 점> visited와 flag를 둘 다 사용해서 같은 일을 두 번 중복하는 문제가 있었다.
flag 값이 0 or 1 or -1이기 때문에 0이면 방문하지 않은 것과 같다.
따라서 visited를 대신할 확인할 flag 리스트를 사용해야한다.
이유:방문한 node와 child의 flag는 0이 아닌 값을 가지기 때문에, flag가 0인지 아닌지만 확인해주면 된다.
배운 점> 동일한 for loop를 반복하지 않도록 주의하자.
"""
import sys
from collections import deque
def bfs(node):
    flag[node] = 1
    q = deque([node])
    while q:
        node = q.popleft()
        for child in graph[node]:
            if flag[child] == 0:
                q.append(child)
                flag[child] = flag[node] * (-1)
            else:
                if flag[child] == flag[node]:
                    return False
    return True

input = sys.stdin.readline
k = int(input())
for test in range(k):
    v, e = map(int, input().split())
    graph = [[] for i in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = True
    flag = [0] * (v + 1)
    for node in range(1, v + 1):
        if flag[node] == 0:
            result = bfs(node)
            if not result:  # if bfs result is False:
                answer = False
                break
    print("YES" if answer else "NO")
"""Solution 4
결과> 틀렸습니다.
잘못한 점>불필요한 for문이 있었다.
Solution 3에서는 test case 개수만큼 for문으로 graph를 생성을 완료하고, 다시 for문으로 graph를 읽는 구조였다.
하나의 for문에서 첫 번째 테스트 case에서 graph를 완성하고, 그래프 탐색에 들어가면 for문 사용을 줄일 수 있다.
"""
# import sys
# from collections import deque
# def bfs(node,v):
#     q = deque([node])
#     while q:
#         node = q.popleft()
#         visited[node] = 1
#
#         for child in graph[node]:
#             if visited[child]==0:# child가 방문한 적 없는 node라면
#                 q.append(child)
#                 # child의 flag는 0 or flag[node]와 같다 or flag[node]와 다르다.
#                 if flag[child] == flag[node]:
#                     return 0 # break는 필요 없는걸까? return하면 for loop에서 벗어나는 거지?
#                 elif flag[child] == 0:
#                     flag[child] = flag[node] * (-1)
#                 else: #if flag[child] != flag[node]:
#                     continue
#     return 1
#
# input = sys.stdin.readline
# k = int(input())
# for test in range(k):
#     v, e = map(int, input().split())
#     graph = [[] for i in range(v + 1)]
#     graph[0]=v
#     for _ in range(e):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#
#     answer = 0
#     visited = [0] * (v + 1)
#     flag = [0] * (v + 1)
#     for node in range(1, v + 1):
#         if node == 1:
#             flag[node] = 1
#         if visited[node] == 0:
#             # print('node', node)
#             result = bfs(node, v)
#             if result == 0:  # if bfs result is False:
#                 print('N0')
#                 answer += -1
#                 break
#     if answer == 0:  # if bfs result is True:
#         print('YES')

"""Solution 3
실패
예제는 통과
잘못된 생각>
Solution 1에서는 child의 flag를 조사하기 전에 child의 방문 여부를 따지면 안된다고 생각했었다.
이유: 그렇게 생각한 이유는
이전 조사한 node의 child여서 flag가 변경된 적 있는 child라면 1 or -1 값을 가졌을 것이기 때문에,
다른 node가 그 child 가지고 있을 때, 모든 child의 flag와 node의 flag를 비교해야한다고 생각했기 때문에.
생각 수정>
방문한적 없는 child만 flag를 조사해야한다.
이유: 한 번 바꾸준 flag(즉, 0이 아닌 1 or -1의 값을 대입해준)의 값을 바꾸지 않기 위해서.
"""
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# k = int(input())
# graph_list =[[] for _ in range(k)]
# for test in range(k):
#     v, e = map(int, input().split())
#     graph = [[] for i in range(v + 1)]
#     graph[0]=v
#     for _ in range(e):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#     graph_list[test]=graph
#
# def bfs(node,v):
#     q = deque([node])
#     while q:
#         node = q.popleft()
#         visited[node] = 1
#         for child in graph[node]:
#             # if visited[child] == 1:
#             #     break
#             if visited[child]==0:# child가 방문한 적 없는 node라면
#                 q.append(child)
#                 # child의 flag는 0 or flag[node]와 같다 or flag[node]와 다르다.
#                 if flag[child] == flag[node]:
#                     return 0 # break는 필요 없는걸까? return하면 for loop에서 벗어나는 거지?
#                 elif flag[child] == 0:
#                     flag[child] = flag[node] * (-1)
#                 else: #if flag[child] != flag[node]:
#                     continue
#     return 1
# # ct=0
# for g in graph_list:
#     # if ct ==1:
#     answer = 0
#     graph = g
#     v=graph[0]
#     visited = [0] * (v + 1)
#     flag = [0] * (v + 1)
#     # print(g)
#     for node in range(1,v+1):
#         if node == 1:
#             flag[node] = 1
#         if visited[node] == 0:
#             # print('node', node)
#             result = bfs(node, v)
#             if result == 0:#if bfs result is False:
#                 print('N0')
#                 answer+= -1
#                 break
#             # else:
#             #     answer+=result
#     if answer==0:# if bfs result is True:
#         print('YES')
#     # ct+=1

"""Solution 2
시간초과
"""
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# k = int(input())
# graph_list =[[] for _ in range(k)]
# for test in range(k):
#     v, e = map(int, input().split())
#     graph = [[] for i in range(v + 1)]
#     graph[0]=v
#     for _ in range(e):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#     graph_list[test]=graph
#
# def bfs(node,v):
#     q = deque([node])
#
#     while q:
#         node = q.popleft()
#         # if visited[node] == 0:
#         visited[node] = 1
#         for child in graph[node]:
#             if flag[child] == flag[node]:
#                 # print('node, child)', node, child)
#                 # print('flag[child] == flag[node]', flag[child],flag[node])
#                 return 0 # break는 필요 없는걸까? return하면 for loop에서 벗어나는 거지?
#             else:# flag[child]=0 or different with parent node
#                 flag[child] = flag[node] * (-1)
#                 q.append(child)
#     return 1
# # ct=0
# for g in graph_list:
#     # if ct ==1:
#     answer = 0
#     graph = g
#     v=graph[0]
#     visited = [0] * (v + 1)
#     flag = [0] * (v + 1)
#     # print(g)
#     for node in range(1,v+1):
#         if node == 1:
#             flag[node] = 1
#         if visited[node] == 0:
#             # print('node', node)
#             result = bfs(node, v)
#             if result == 0:#if bfs result is False:
#                 print('N0')
#                 break
#             else:
#                 answer+=result
#     if answer:# if bfs result is True:
#         print('YES')
#     # ct+=1
"""Solution 1
실패
예제는 통과"""
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# k = int(input())
# graph_list =[[] for _ in range(k)]
# for test in range(k):
#     v, e = map(int, input().split())
#     graph = [[] for i in range(v + 1)]
#     graph[0]=v
#     for _ in range(e):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#     graph_list[test]=graph
#
# def bfs(node,v):
#     q = deque([node])
#
#     while q:
#         node = q.popleft()
#         if node == 1:
#             flag[node] = 1
#
#         if visited[node] == 0:
#             visited[node] = 1
#             for child in graph[node]:
#                 if flag[child] == flag[node]:
#                     # print('node, child)', node, child)
#                     # print('flag[child] == flag[node]', flag[child],flag[node])
#                     return 0
#                 else:# flag[child]=0 or different with parent node
#                     flag[child] = flag[node] * (-1)
#                     q.append(child)
#
#     return 1
# # ct=0
# for g in graph_list:
#     # if ct ==1:
#     answer = 0
#     graph = g
#     v=graph[0]
#     visited = [0] * (v + 1)
#     flag = [0] * (v + 1)
#     # print(g)
#     for node in range(1,v+1):
#         # print('node', node)
#         result = bfs(node, v)
#         if result == 0:#if bfs result is False:
#             print('N0')
#             break
#         else:
#             answer+=result
#     if answer:# if bfs result is True:
#         print('YES')
#     # ct+=1


