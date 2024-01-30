# (https://school.programmers.co.kr/learn/courses/30/lessons/120833)

# 문제

# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 

# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    a = 0
    for i in range(n):
        if (n % (i+1)) == 0:
            a = a + 1
        elif (n % (i+1)) != 0: 
            pass
    answer = a
    return answer

def solve():
    n = 100
    answer = solution(n)
    print("{}".format(answer))
    return

solve()