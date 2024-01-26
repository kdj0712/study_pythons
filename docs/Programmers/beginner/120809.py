# (https://school.programmers.co.kr/learn/courses/30/lessons/120809)

# 문제

# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]*2
    answer = numbers
    return answer

def solve():
    numbers = [1, 2, 100, -99, 1, 2, 3]
    answer = solution(numbers)
    print(answer)
    return

solve()