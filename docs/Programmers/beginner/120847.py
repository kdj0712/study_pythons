# (https://school.programmers.co.kr/learn/courses/30/lessons/120847)

# 문제

# 정수 배열 numbers가 매개변수로 주어집니다.

# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    numbers
    numbers = sorted(numbers,reverse=False)
    a = numbers[len(numbers)-1]
    b = numbers[len(numbers)-2]
    answer = a * b
    return answer

def solve():
    numbers = [0, 31, 24, 10, 1, 9]
    answer = solution(numbers)
    print("{}".format(answer))
    return

solve()