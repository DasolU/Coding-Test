# Programmers
# DFS/BFS: 네트워크 문제
"""
알고리즘 설계 아이디어>
* 첫 번째 노드 (임의의 노드) 시작해서 연결된 모든 노드를 방문하며 연결된 모든 노드를 탐색한다. 그리고 visited에 기록한다.
* 이러한 방법을 사용하면 두 번째 노드에서 탐색을 시작할 때, 두 번째 노드와 연결이 되어있지만 이미 방문했던 (= 첫 번째 노드와 연결되어 있는) 노드는 탐색할 필요가 없게 된다.
따라서 이미 연결된 노드들의 리스트를 만들고 그에 연결되지 않은 노드를 찾을 수 있게 된다.
알고리즘 작동 순서>
1. 첫 번째 컴퓨터부터 마지막 컴퓨터까지 조사한다.
2. 첫 번째 컴퓨터를 방문하지 않았었다면 방문한다.
3. 방문해서 첫 번째 컴퓨터와 연결된 모든 자식 컴퓨터들을 탐색 목록에 저장하고, 방문한 목록에 저장한다.
4. 첫 번째 컴퓨터에 대한 조사가 끝나면 네트워크 하나를 추가한다.
6. 두 번째 컴퓨터를 조사하기 전에, 방문한 목록에 있는지 확인한다.
7. 두 번째 컴퓨터가 방문한 목록에 있기 때문에 조사를 하지 않는다.
"""

"""Final Solution: Solution 2-1
문제> 
solution 2에서 if node not in visited 방식의 시간 복잡도는 O(n)으로 클 것으로 예상. 

바꾼점>
1. queue를 list말고 deque로 구현
2. solution 1처럼 visited를 미리 만들고 visited[node]=True로 바꾸는 방법 사용하여 O(1)으로 시간 단축시킴.

성능 비교>
1.solution 2-1와 solution 2
solution 2-1이 테스트 11 케이스의 경우 solution 2에서 걸린 시간을 반정도로 크게 단축된 것을 확인할 수 있었다.
2. solution 2-1와 solution 1
서로 비슷한 시간이 걸렸으며 테스트마다 우위가 달랐다.
하지만 가장 시간이 오래 걸리는 테스트 11의 경우 solution 2-1이 더 빨랐다.

배운점>
visited=[False for i in range(n)]처럼
visited 리스트를 노드 개수만큼 False로 미리 만들어놓고
node를 방문했는지 조사할 때, if visited[node] == False:을 사용하자! 

visted=[]
visited.append(node)
if new_node not in visited:
위의 예시처럼 visited를 빈 list로 만들고 원소들을 append하는 방식을 사용하면, 
새로 방문하는 노드가 visited 목록에 있는지 조사할 때 시간 복잡도가 O(n)으로, 
이미 방문한 node가 많을수록 더 많은 시간을 소모하게 된다.

따라서 visited=[False for i in range(n)]처럼
visited 리스트를 노드 개수만큼 False로 미리 만들어놓고
if visited[node] == False: 처럼 
해당 node의 값이 False인 경우 조사하면 시간 복잡도가 O(1)이므로
시간이 단축된다.

테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.12ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (1.41ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.65ms, 10.4MB)
테스트 9 〉	통과 (0.28ms, 10.1MB)
테스트 10 〉	통과 (0.40ms, 10.3MB)
테스트 11 〉	통과 (3.68ms, 10.3MB)
테스트 12 〉	통과 (1.92ms, 10.3MB)
테스트 13 〉	통과 (1.07ms, 10.2MB)"""
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n=3

from collections import deque

def BFS(n, computers, node, visited):
    q = deque([node])
    while q:
        node = q.popleft()
        visited[node]=True
        for com in range(n):
            if com !=node and computers[node][com] == 1:
                if visited[com] == False:
                    q.append(com)

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for node in range(n):
        if visited[node] == False:
        # if node not in visited:# O(n) 모든 원소들을 확인해야해서 시간 복잡도가 늘었던 것이 문제인 것으로 추측
            BFS(n, computers, node, visited)
            answer +=1
    return answer

print(solution(n, computers))
"""Solution2
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.18ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (2.27ms, 10.1MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (1.00ms, 10.2MB)
테스트 9 〉	통과 (0.82ms, 10.2MB)
테스트 10 〉	통과 (0.47ms, 10.2MB)
테스트 11 〉	통과 (7.29ms, 10.3MB)
테스트 12 〉	통과 (3.57ms, 10.2MB)
테스트 13 〉	통과 (1.35ms, 10.1MB)
"""
# from collections import deque
#
# def BFS(n, computers, node, visited):
#     q = deque([node])
#     while q:
#         node = q.popleft()
#         visited.append(node)
#         for com in range(n):
#             if com !=node and computers[node][com] == 1:
#                 if com not in visited:
#                     q.append(com)
#
# def solution(n, computers):
#     answer = 0
#     visited = deque()
#     for node in range(n):
#         if node not in visited:
#             BFS(n, computers, node, visited)
#             answer +=1
#     return answer


"""Final Solution: Solution 1 
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.09ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (1.37ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.1MB)
테스트 8 〉	통과 (0.74ms, 10.2MB)
테스트 9 〉	통과 (0.28ms, 10.3MB)
테스트 10 〉	통과 (0.39ms, 10.3MB)
테스트 11 〉	통과 (4.00ms, 10.3MB)
테스트 12 〉	통과 (2.10ms, 10.3MB)
테스트 13 〉	통과 (1.06ms, 10.2MB)
"""
# def solution(n, computers):
#     answer = 0
#     visited = [False for i in range(n)]
#     for com in range(n):
#         if visited[com] == False:
#             BFS(n, computers, com, visited)
#             answer += 1
#     return answer
#
# def BFS(n, computers, com, visited):
#     visited[com] = True
#     queue = []
#     queue.append(com)
#     while len(queue) != 0:
#         com = queue.pop(0)
#         visited[com] = True
#         for connect in range(n):
#             if connect != com and computers[com][connect] == 1:
#                 if visited[connect] == False:
#                     queue.append(connect)

