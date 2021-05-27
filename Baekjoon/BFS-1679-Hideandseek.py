# BAEKJOON
# 1697
# 숨바꼭질
# BFS: 찾을 수 있는 가장 빠른 시간
# +1을 2번 가는 것과 2배 하는 것이 겹치므로, 항상 2배 하는 것이 더 빠르게 간다.
# 최단시간을 구하는 것이므로 2배씩으로 최대한 간 다음 +1 or -1하는 것이 최단 시간이 될 것이다.
# 하지만 3이상의 수에서는 2로 나눌 수 있을 만큼 많이 이동하는 것이 먼저겠지만,
# 2 미만으로 차이난다면 1 or -1이 최단이 되므로 몫과 나머지로 코드를 짜는 것이 옳지 않아 보인다.

"""Final Solution: Solution 1
메모리: 35472 KB
시간: 176 ms
몰랐던 점> 주어진 입력이 가지는 최대 and 최소 범위에 대한 test case를 생각해보는 것이 필요했다.
child node의 visited 여부를 조사할 때 index error 발생을 막기 위해서,
index min <= child node <= index max 인지 조사하는 과정을 추가해야한다.
"""

import sys
from collections import deque

def bfs(n):
    q = deque([n])
    while q:
        node = q.popleft()
        if node == k:
            return visited[node]
        next = [node - 1, node + 1, node * 2]
        for child in next:
            if child >= 0 and child<=100000:
                if visited[child] == 0:
                    if child == k:
                        return visited[node]+1
                    q.append(child)
                    visited[child]=visited[node]+1

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [0]*(100001)
print(bfs(n))

