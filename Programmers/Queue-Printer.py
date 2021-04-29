# Programmers
# Stack/Queue: 프린터
"""Final Solution: Solution 1
테스트 1 〉	통과 (0.42ms, 10.3MB)
테스트 2 〉	통과 (0.60ms, 10.3MB)
테스트 3 〉	통과 (0.42ms, 10.3MB)
테스트 4 〉	통과 (0.10ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.09ms, 10.2MB)
테스트 7 〉	통과 (0.17ms, 10.2MB)
테스트 8 〉	통과 (0.46ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.10ms, 10.2MB)
테스트 11 〉	통과 (0.34ms, 10.2MB)
테스트 12 〉	통과 (0.13ms, 10.3MB)
테스트 13 〉	통과 (0.32ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.06ms, 10.2MB)
테스트 16 〉	통과 (0.04ms, 10.2MB)
테스트 17 〉	통과 (0.54ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.46ms, 10.2MB)
"""
priorities = [1, 1, 9, 1, 1, 1]#[2, 1, 3, 2]
location=0#2

def solution(priorities, location):
    answer = 0
    q=list(zip(priorities,range(len(priorities))))
    sortedlist = []
    while q:
        front = q.pop(0)
        ct = 0
        for pri,idx in q:
            if pri>front[0]:
                ct+=1
                break
        if ct > 0:
            q.append(front)
        else:
            sortedlist.append(front)
    for idx, (pri,loc) in enumerate(sortedlist):
        if loc == location:
            answer=idx+1
    return answer
print(solution(priorities, location))