# (https://school.programmers.co.kr/learn/courses/30/lessons/120841)

# 문제

# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.

# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers, direction):
    numbers
    answer = []
    if direction == "right":
        answer.append(numbers[len(numbers)-1])
        for x in range(len(numbers)-1):
            answer.append(numbers[x])

    elif direction == "left":
        for y in range(len(numbers)-1):
            answer.append(numbers[y+1])
        answer.append(numbers[0])
    return answer

def solve():
    numbers = [4, 455, 6, 4, -1, 45, 6]
    direction = "left"
    answer = solution(numbers,direction)
    print("{}".format(answer))
    return

solve()