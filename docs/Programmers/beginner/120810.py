# (https://school.programmers.co.kr/learn/courses/30/lessons/120810)

# 문제

# 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

def solution(num1, num2):
    answer = num1 % num2
    return answer

def solve():
    num1 = int(input())
    num2 = int(input())
    answer = solution(num1, num2)
    print("{}".format(answer))
    return

solve()