# Programmers
# Stack/Queue: 기능개
progresses=[95, 90, 99, 99, 80, 99]#[93, 30, 55]
speeds =[1, 1, 1, 1, 1, 1]#[1, 30, 5]
"""Final Solution: Solution 1
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.58ms, 10.1MB)
테스트 3 〉	통과 (0.77ms, 10.3MB)
테스트 4 〉	통과 (0.32ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.09ms, 10.3MB)
테스트 7 〉	통과 (0.72ms, 10.2MB)
테스트 8 〉	통과 (0.12ms, 10.2MB)
테스트 9 〉	통과 (0.56ms, 10.2MB)
테스트 10 〉	통과 (0.61ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
"""
def solution(progresses, speeds):
    answer = []
    day = 0
    while progresses:
        day+=1
        for i in range(len(progresses)):
            progresses[i] +=speeds[i]

        donelist = []
        for i in range(len(progresses)):
            if progresses[i]>=100:
                donelist.append(i)
            else:
                break
        if len(donelist)>0:
            answer.append(len(donelist))

        for _ in range(len(donelist)):
            progresses.pop(0)
            speeds.pop(0)

    return answer

print(solution(progresses, speeds))