# BAEKJOON
# 13023
# ABCDE
# 노드 5개가 연결된 경로가 존재하는지 안하는지 구하라->DFS

import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())

# Make Graph
graph = collections.defaultdict(list) #{}

for _ in range(m):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for i in range(n)]

def dfs(node, level): # 자식 노드가 있는지 확인하고, 있다먄 level을 추가한다.
    global answer
    visited[node]=True

    if level>=4:
        answer = True
        return answer

    else:
        for child in graph[node]:
            if not visited[child]:# not False==True 일때, 방문한 적 없는 node일 때
                dfs(child, level+1)
                visited[child] = False
answer = False
for node in range(n): # 모든 노드 방문
    dfs(node,0)
    visited[node]=False
    if answer:
        break
if answer:
    print(1)
else:
    print(0)






