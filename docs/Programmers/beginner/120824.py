# (https://school.programmers.co.kr/learn/courses/30/lessons/120824)

# 문제

# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(num_list):
    answer = []
    x = 0
    y = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            x = x + 1
        elif num_list[i] % 2 != 0:
            y = y + 1
    answer = [x, y]

    return answer

def solve():
    num_list = [1, 3, 5, 7]
    answer = solution(num_list)
    print(answer)
    return

solve()