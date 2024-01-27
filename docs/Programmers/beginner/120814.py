# (https://school.programmers.co.kr/learn/courses/30/lessons/120814)

# 문제

# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 

# 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

def solution(n):
    s = n % 7
    if s == 0:
        answer = n / 7
    elif s != 0:
        answer = (n / 7) + 1
    answer = int(answer)
    return answer

def solve():
    n = int(input())
    answer = solution(n)
    print("{}".format(answer))
    return

solve()