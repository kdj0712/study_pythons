# (https://school.programmers.co.kr/learn/courses/30/lessons/120893)

# 문제

# 문자열 my_string이 매개변수로 주어질 때,

# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answers = []
    for x in range(len(my_string)):
        s = my_string[x]
        if  s.isupper() == True:
            small = s.lower()
            answers.append(small)
        elif s.islower() == True:
            big = s.upper()
            answers.append(big)
        else:
            pass
    answer = ''.join(map(str, answers))
    return answer

def solve():
    my_string = "abCdEfghIJ"
    answer = solution(my_string)
    print("{}".format(answer))
    return

solve()