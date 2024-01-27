# (https://school.programmers.co.kr/learn/courses/30/lessons/120822)

# 문제

# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = [0]
    answer = answer * len(my_string)
    for i in range(len(my_string)):
        s = 0
        s = len(my_string)-(i+1)
        answer[i] = my_string[s]
        pass
    answer = ''.join(map(str, answer))
    return answer

def solve():
    my_string = "jaron"
    answer = solution(my_string)
    print(answer)
    return

solve()