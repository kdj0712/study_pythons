# (https://school.programmers.co.kr/learn/courses/30/lessons/120583)

# 문제

# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때,

# array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.



def solution(array, n):
    answers = []
    answers = array
    answer = 0
    for x in answers:
        if x == n:
            answer = answer + 1
        else:
            answer = answer + 0
    return answer

def solve():
    array = [0, 2, 3, 4, 5]
    n = 1
    answer = solution(array, n)
    print(answer)
    return

solve()