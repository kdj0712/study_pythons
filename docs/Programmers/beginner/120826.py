# (https://school.programmers.co.kr/learn/courses/30/lessons/120825)

# 문제

# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string, letter):
    i = len(my_string)
    answer = []
    for i in range(len(my_string)):
        if my_string[i] != letter:
            answer.append(my_string[i])
        elif my_string[i] == letter:
            pass
    answer =''.join(map(str, answer))
    return answer

def solve():
    my_string = "BCBdbe"
    letter = "B"
    answer = solution(my_string, letter)
    print(answer)
    return

solve()