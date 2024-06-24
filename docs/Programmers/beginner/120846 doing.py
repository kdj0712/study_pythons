# (https://school.programmers.co.kr/learn/courses/30/lessons/120846)

# 문제

# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

# def solution(n):
#     answer = 0
#     for x in range(n):
#         for y in range(x+1):
#             (x+1)%y == 0
#     return answer

# def solve():
#     n = 10
#     answer = solution(n)
#     print("{}".format(answer))
#     return

# solve()


def solution(n):
    answer = 0
    for i in range(2, n+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt >= 3:
            answer += 1
    return answer

def solve():
    n = 15
    answer = solution(n)
    print("{}".format(answer))
    return

solve()
