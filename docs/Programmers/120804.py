# (https://school.programmers.co.kr/learn/courses/30/lessons/120804)

# 문제

# 정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.

def solution(num1, num2):
    answer = num1 * num2
    return answer

def solve():
    num1 = int(input())
    num2 = int(input())
    answer = solution(num1, num2)
    print("{}".format(answer))
    return

solve()