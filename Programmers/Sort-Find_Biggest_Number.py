# Programmers
# Sort: 가장 큰 수
numbers = [3, 30, 34, 5, 9]

""" Solution 1: 시간 초과
# 순열과 조합은 input으로 iterable(list, dic, tuple, str)만을 받는다.
# 대표적으로 range(n)은 list를 return한다.
# nPr 순열 이용
"""
# from itertools import permutations # 순열 (순서 상관 있게 r개 뽑는 경) nPr
# from itertools import combinations # 조합 (순서 상관 없이 r개 뽑는 경우) nCr

# def nPr(numbers):
#     idx = range(len(numbers))
#     save = []
#     for idx in permutations(idx, len(numbers)):
#         candidate = ''
#         for i in idx:
#             candidate +=str(numbers[i])
#         save.append(candidate)
#     save = [int(i) for i in save]
#     answer = str(max(save))
#     return answer


""" Solution 2 """
def sort(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


