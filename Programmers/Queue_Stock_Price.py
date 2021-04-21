# Programmers
# 스택/큐: 주식 가격
""" Final Solution: Solution 3
비교:
Solution 2과 비슷하지만 효율성이 높다.
Solution 1보다 더 많은 시간이 걸리지만 효율성이 높다.

효율성 높은 이유:
Solution 2에서는 n번 "새로운 list를 만들어" 사용했다.
따라서 메모리 사용 증가하여 문제가 된 것으로 생각된다.

Final Solution에서는 새로운 list를 사용하지 않고
기존 input 리스트를 사용하면서도 새로운 영역을 사용할 수 있도록
"기존 input 리스트의 idx를 바꿔" 사용했다.

배운점:
<효율성을 높이는 방법>
1.새로운 list를 만들지 말고
기존 list를 다르게 사용할 수 있는 idx를 만들자.
<시간 단축하는 방법>
2. for loop 2번 돌리는 것보다, 2개 list에서 pop을 반복하는게 더 빠르다.
"""
"""
정확성: 66.7  
효율성: 33.3  
테스트 1 〉	통과 (109.84ms, 20MB)
테스트 2 〉	통과 (84.72ms, 18.5MB)
테스트 3 〉	통과 (133.52ms, 20.8MB)
테스트 4 〉	통과 (92.46ms, 19.2MB)
테스트 5 〉	통과 (67.19ms, 17.6MB)
"""
def solution(prices):
    answer = [len(prices)-1-i for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j]<prices[i]:
                answer[i]= j-i
                break
    return answer
print(solution([1, 2, 3, 2, 3]))


""" Solution 1
list queue 사용
정확성: 66.7
효율성: 0.0 (시간 초과)
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.09ms, 10.1MB)
테스트 3 〉	통과 (0.97ms, 10.3MB)
테스트 4 〉	통과 (1.17ms, 10.2MB)
테스트 5 〉	통과 (1.37ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.68ms, 10.2MB)
테스트 8 〉	통과 (0.86ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (1.30ms, 10.3MB)
"""
# def solution(prices):
#     answer = []
#     q = prices
#     q_idx = list(range(0,len(prices)))
#     max_idx = len(prices)-1
#     while q:
#         time = 0
#         node = q.pop(0)
#         node_idx = q_idx.pop(0)
#         for i in range(len(q)):
#             if node>q[i]:
#                 time = (i+node_idx+1)-node_idx
#                 break
#         if time == 0:
#             time = max_idx-node_idx
#         answer.append(time)
#     return answer
""" Solution 1-1
Solution 1과 동일하지만 deque로 변경
정확성: 66.7
효율성: 26.7
합계: 93.3 / 100.0

정확성
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.92ms, 10.2MB)
테스트 4 〉	통과 (1.07ms, 10.3MB)
테스트 5 〉	통과 (1.09ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.40ms, 10.2MB)
테스트 8 〉	통과 (0.70ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (1.79ms, 10.3MB)
효율성 테스트
테스트 1 〉	통과 (247.57ms, 21.2MB)
테스트 2 〉	통과 (149.96ms, 19MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (193.79ms, 19.7MB)
테스트 5 〉	통과 (97.84ms, 18.3MB)
"""
# from collections import deque
# def solution(prices):
#     answer = []
#     q = deque(prices)
#     q_idx = deque(list(range(0,len(prices))))
#     max_idx = len(prices)-1
#     while q:
#         time = 0
#         node = q.popleft()
#         node_idx = q_idx.popleft()
#         for i in range(len(q)):
#             if node>q[i]:
#                 time = (i+node_idx+1)-node_idx
#                 break
#         if time == 0:
#             time = max_idx-node_idx
#         answer.append(time)
#     return answer

""" Solution 2
for loop 사용
정확성: 66.7
효율성: 0.0 (시간 초과)
비교: Solution 1보다 시간 더 많이 걸림
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.2MB)
테스트 3 〉	통과 (1.64ms, 10.3MB)
테스트 4 〉	통과 (1.96ms, 10.3MB)
테스트 5 〉	통과 (2.47ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (1.14ms, 10.3MB)
테스트 8 〉	통과 (1.38ms, 10.3MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (2.27ms, 10.4MB)
"""
# def solution(prices):
#     answer = [len(prices)-1-i for i in range(len(prices))]
#     for i in range(len(prices)):
#         search_q = prices[i+1:]
#         for j in range(len(search_q)):
#             if search_q[j]<prices[i]:
#                 answer[i]= (i+1+j)-i
#                 break
#     return answer

