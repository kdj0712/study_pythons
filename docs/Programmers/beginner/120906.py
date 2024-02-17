#  (https://school.programmers.co.kr/learn/courses/30/lessons/120906)

# 문제

# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

def solution(n):
    n = str(n)
    lists = []
    for x in range(len(n)):
        lists.append(n[x])
    answer = 0
    for y in range(len(lists)):
        add = int(lists[y])
        answer = answer + add
    answer
    return answer

def solve():
    n = 930211
    answer = solution(n)
    print(answer)
    return

solve()