# (https://school.programmers.co.kr/learn/courses/30/lessons/120862)

# 문제

# 정수 배열 numbers가 매개변수로 주어집니다.

# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    numbers.sort()
    answer =  max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
    # 가장 작은 두 음수의 곱과 가장 큰 두 양수의 곱 중 더 큰 값 반환
    return answer

def solve():
    numbers = [1, 2, -3, 4, -5, -500]
    answer = solution(numbers)
    print("{}".format(answer))
    return

solve()



# # 이하는 원래 풀던 방식이지만, 음수에 대한 처리를 하지 않는다는 이유로 오답처리였던 내용

# def solution(numbers):
#     answer = 0 
#     for i in range(len(numbers)):
#         for x in range(len(numbers)):
#             if numbers[i] == numbers[x]:
#                 pass
#             elif numbers[i] != numbers[x]:
#                 a = numbers[i] * numbers[x]
#                 if a > answer:
#                     answer = a
#     return answer

# def solve():
#     numbers = [1, 2, -3, 4, -5, -500]
#     answer = solution(numbers)
#     print("{}".format(answer))
#     return

# solve()