# BAEKJOON
# 14226
# 이모티콘
# BFS: 시간의 최솟값을 구하는 프로그램
"""Final Solution: Solution 2
메모리: 35812 KB
시간: 116 ms
"""
# from collections import deque
#
# n= int(input())
#
# def bfs():
#     q = deque()
#     q.append((1, 0))
#
#     visited = dict()
#     visited[(1, 0)] = 0
#     while q:
#         s,c = q.popleft()
#
#         if s==n:
#             print(visited[(s, c)])
#             return
#         # 연산 1번 (정답)
#         if (s,s) not in visited.keys() and 0<s<=2002:
#             # print(s)
#             visited[(s,s)] = visited[(s,c)] + 1
#             q.append((s,s))
#         # 연산 1번 (오답)
#         # if (2*s,s) not in visited.keys() and 0<2*s<=2002:
#         #     # print(s)
#         #     visited[(2*s,s)] = visited[(s,c)] + 2
#         #     q.append((2*s,s))
#         # 연산 2번
#         if (s+c,c) not in visited.keys() and 0<s+c<=2002:
#             # print(s+c)
#             visited[(s+c,c)] = visited[(s,c)] + 1
#             q.append((s+c, c))
#         # 연산 3번
#         if (s-1,c) not in visited.keys() and 0<s-1<=2002:
#             # print(s-1)
#             visited[(s-1,c)] = visited[(s,c)] + 1
#             q.append((s-1, c))
# bfs()

"""Solution 1
틀린 풀이
풀이 방법> 이 방법은 2번 때문에 실패했다.
1-> 1,1(2)->1,1,1,1(2)->1,1,1,1,1,1,1,1(2)
                      ->1,1,1,1,1,1(1)
1. 원소 하나를 지운다/ 시간 +=1
2. 현재 길이를 더한다=개수*2/ 시간 +=2
3. 이전 길이를 더한다./ 시간 +=1법

틀린 이유 1>
복잡하게 계산한 결과를 구현하지 말고 문제에서 제공한 3가지 연산을 그대로 재현했어야 했다.
현재 개수가 같고 클립보드에 저장된 개수가 다르면 붙여넣기 한 결과 개수가 달라질 수 있으므로
solution2처럼 child의 방문만 조사하지 말고, child와 clipboard의 조합을 방문한 적 있는지에 대한 조사가 필요하다!!
틀린 이유 2>
연산1번의 결과인 (s,s)를 queue에 올렸어야했다.

배운점> 
런타임에러 (IndexError)의 대부분의 원인은  visited = [0]*N에서 발생한다.
visited list의 길이는 주어진 변수의 범위가 아니다!!
visited list의 길이는 주어진 변수의 범위와 변수가 연산되었을 때 최대범위를 고려해서 지정해야함을 명심해야한다.
이 문제에서는 2<=node<=1000의 범위이며, node*2 or node+node연산을 수행한다.
따라서 visited list의 길이의 최대 값은, visited = [0]*(1000+1)*2
"""
# import sys
# from collections import deque
#
# def bfs(s):
#     q = deque([1])
#     while q:
#         node = q.popleft() #화면에 있는 이모티콘 개수
#         next = [node - 1, node * 2, node + clipboard[node]]
#         for idx, child in enumerate(next):
#             if child>=2 and child<=2002:
#                 if visited[child]==0:
#                     print(child)
#                     if child == s:
#                         if idx == 1:
#                             return visited[node] + 2
#                         else:
#                             return visited[node] + 1
#                     if idx == 0 or idx == 2:
#                         visited[child] = visited[node] + 1
#                         clipboard[child] = clipboard[node]
#                     if idx == 1:
#                         visited[child] = visited[node] + 2
#                         clipboard[child] = node
#                     q.append(child)
#
# input = sys.stdin.readline()
# s = int(input)
# visited = [0]*2002
# clipboard = [0]*2002
# print(bfs(s))


