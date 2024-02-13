# (https://school.programmers.co.kr/learn/courses/30/lessons/120849)

# 문제

# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 

# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    y = "aeiou"
    answer = []
    for x in my_string:
        if x not in y:
            answer.append(x)
        else:
            pass
    answer = "".join(answer)
    return answer

def solve():
    my_string = "nice to meet you"
    answer = solution(my_string)
    print("{}".format(answer))
    return

solve()