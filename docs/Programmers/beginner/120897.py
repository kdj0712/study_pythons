# (https://school.programmers.co.kr/learn/courses/30/lessons/120897)

# 문제

# 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    for x in range(n+1):
        if  n % (x+1) == 0:
            answer.append(x+1)
    return answer

def solve():
    n = 24
    answer = solution(n)
    print("{}".format(answer))
    return

solve()