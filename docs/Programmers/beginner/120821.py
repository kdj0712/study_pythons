# (https://school.programmers.co.kr/learn/courses/30/lessons/120821)

# 문제

# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        s = 0
        s = (len(numbers))-(i+1)
        answer[i] = numbers[s]
    return answer

def solve():
    numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    answer = solution(numbers)
    print(answer)
    return

solve()