# (https://school.programmers.co.kr/learn/courses/30/lessons/120802)

# 문제

# 정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.

def solution(num1, num2):
    answer = num1 + num2
    return answer

def solve():
    num1 = int(input())
    num2 = int(input())
    answer = solution(num1, num2)
    print("{}".format(answer))
    return

solve()