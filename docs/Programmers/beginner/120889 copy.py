# (https://school.programmers.co.kr/learn/courses/30/lessons/120888)

# 문제

# 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.



def solution(my_string):
    answer = []
    my_string
    for x in range(len(my_string)):
        if answer == my_string[x]:
            pass
        elif answer != my_string[x]:
            answer.append(my_string[x])
    answer = ''.join(map(str, answer))
    return answer

def solve():
    my_string = 'We are the world'
    answer = solution(my_string)
    print(answer)
    return

solve()