# BAEKJOON
# 1260
# 방문할 수 있는 모든 노드 방문하기->DFS와 BFS

import sys
from collections import defaultdict
from collections import deque

# Make Graph
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(graph, v):
    stack = deque([v])
    visited = []
    while stack:  # stack에 노드가 없을 때까지
        node = stack.pop()
        if node not in visited:  # 방문하지 않은 노드의
            for child in sorted(graph[node], reverse=True): # pop은 오른쪽 원소부터 꺼내므로 내림차순 정렬해준다.
                if child not in visited:  # 방문하지 않은 자식 노드를 큐에 추가한다.
                    stack.append(child)
            visited.append(node)
    return visited

def bfs(graph, v):
    q = deque([v])
    visited = []
    while q:    #큐에 노드가 없을 때까지
        node = q.popleft()
        if node not in visited: #방문하지 않은 노드의
            for child in sorted(graph[node]):
                if child not in visited:    #방문하지 않은 자식 노드를 큐에 추가한다.
                    q.append(child)
            visited.append(node)
    return visited

for i in dfs(graph, v):
    print(i, end=' ')
print()
for i in bfs(graph, v):
    print(i, end=' ')

