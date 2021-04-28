# Programmers
# Stack/Queue: 다리를 지나는 트럭
bridge_length=2
weight=10
truck_weights=[7,4,5,6]#[10]#########

"""Final Solution: Solution 2
테스트 1 〉	통과 (12.64ms, 10.3MB)
테스트 2 〉	통과 (1497.19ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (333.80ms, 10.1MB)
테스트 5 〉	통과 (9075.90ms, 10.1MB)
테스트 6 〉	통과 (1570.12ms, 10.2MB)
테스트 7 〉	통과 (6.79ms, 10.2MB)
테스트 8 〉	통과 (0.36ms, 10.2MB)
테스트 9 〉	통과 (5.54ms, 10.3MB)
테스트 10 〉	통과 (0.42ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.46ms, 10.2MB)
테스트 13 〉	통과 (2.45ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
"""
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time

""" Solutiion 2-1
결과>
deque로 했더니 시간이 더 오래 걸렸다.
왜지??
Solution 2 자체에 시간 복잡도가 늘어날만한게 없어서 그런가보다.
테스트 1 〉	통과 (13.16ms, 10.1MB)
테스트 2 〉	통과 (1653.81ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (350.21ms, 10.2MB)
테스트 5 〉	통과 (9389.23ms, 10.2MB)
테스트 6 〉	통과 (1837.77ms, 10.2MB)
테스트 7 〉	통과 (7.33ms, 10.2MB)
테스트 8 〉	통과 (0.33ms, 10.3MB)
테스트 9 〉	통과 (5.65ms, 10.2MB)
테스트 10 〉	통과 (0.49ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.38ms, 10.2MB)
테스트 13 〉	통과 (2.50ms, 10.4MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
"""
# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     q = deque(0 for _ in range(bridge_length))
#     truck_weights = deque(truck_weights)
#     while q:
#         time += 1
#         q.popleft()
#         if truck_weights:
#             if sum(q) + truck_weights[0] <= weight:
#                 q.append(truck_weights.popleft())
#             else: # sum(q) + truck_weights[0] > weight:
#                 q.append(0)
#     return time
""" Solution 1
정확성: 21.4
합계: 21.4 / 100.0
테스트 1 〉	통과 (0.98ms, 10.2MB)
테스트 2 〉	실패 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	실패 (0.14ms, 10.3MB)
테스트 5 〉	실패 (0.33ms, 10.4MB)
테스트 6 〉	실패 (0.20ms, 10.4MB)
테스트 7 〉	실패 (0.01ms, 10.3MB)
테스트 8 〉	실패 (0.02ms, 10.3MB)
테스트 9 〉	실패 (0.47ms, 10.3MB)
테스트 10 〉	실패 (0.02ms, 10.4MB)
테스트 11 〉	실패 (0.02ms, 10.4MB)
테스트 12 〉	실패 (0.11ms, 10.1MB)
테스트 13 〉	실패 (0.09ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.4MB)"""

# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     num = len(truck_weights)
#     idx = deque(range(num))
#     on = deque()
#     if num == 1:
#         return bridge_length+1
#
#     while len(idx):
#         now = idx.popleft()
#         now_w = truck_weights[now]
#
#         if sum(on) + now_w <= weight:
#             on.append(now_w)
#             if now == len(truck_weights) - 1:   # 마지막 트럭일 경우
#                 answer+= bridge_length
#                 on.popleft()
#             else:
#                 total = sum(on)
#                 if num >= bridge_length:
#                     for i in range(now + 1, (now+1)+(bridge_length-1)): # range(2, 2+1)
#                         total += truck_weights[i]
#                         if total <= weight:
#                             idx.popleft()  # 올라갈 수 있는 최대 트럭까지 삭제
#                             on.append(truck_weights[i])  # # 올라갈 수 있는 최대 트럭까지 목록에 올림
#                         else:
#                             break
#                     answer += (bridge_length+1)
#                     on.popleft()
#                     if len(on)==1:
#                         answer += 1 * (len(on) - 1)
#                         on.popleft()
#                     elif len(on)>1:
#                         answer += 1 * (len(on))
#                         for _ in range(len(on)):
#                             on.popleft()
#
#                 else:   #num < bridge_length:
#                     for i in range(now + 1, num):  # range(2, 2+1)
#                         total += truck_weights[i]
#                         if total <= weight:
#                             idx.popleft()  # 올라갈 수 있는 최대 트럭까지 삭제
#                             on.append(truck_weights[i])  # # 올라갈 수 있는 최대 트럭까지 목록에 올림
#                         else:
#                             break
#                     answer += (bridge_length+1)
#                     on.popleft()
#                     if len(on)==1:
#                         answer += 1 * (len(on) - 1)
#                         on.popleft()
#                     elif len(on)>1:
#                         answer += 1 * (len(on))
#                         for _ in range(len(on)):
#                             on.popleft()
#     return answer
