# (https://school.programmers.co.kr/learn/courses/30/lessons/120846)

# 문제

# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = 0
    for x in range(n):
        for y in range(x+1):
            (x+1)%y == 0
    return answer

def solve():
    n = 10
    answer = solution(n)
    print("{}".format(answer))
    return

solve()