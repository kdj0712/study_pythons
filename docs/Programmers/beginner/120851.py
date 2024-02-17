# (https://school.programmers.co.kr/learn/courses/30/lessons/120851)

# 문제

# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.


def solution(my_string):
    import re
    numbers = re.findall(r'\d',my_string)
    answer = 0
    for x in range(len(numbers)):
        number = int(numbers[x])
        answer = answer + number
    return answer

def solve():
    my_string = "1a2b3c4d123"
    answer = solution(my_string)
    print("{}".format(answer))
    return

solve()