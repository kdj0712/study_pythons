#  (https://school.programmers.co.kr/learn/courses/30/lessons/120910)

# 문제

# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

def solution(n, t):
    answer = n
    for i in range(t):
        answer = answer * 2
        pass
    answer
    return answer

def solve():
    n = 2
    t = 10
    answer = solution(n, t)
    print(answer)
    return

solve()