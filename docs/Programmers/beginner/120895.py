# (https://school.programmers.co.kr/learn/courses/30/lessons/120895)

# 문제

# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,

# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

def solution(my_string,num1,num2):
    a = my_string[num1]
    b = my_string[num2]
    answers = []
    for i in range(len(my_string)):
        if i == num1:
            answers.append(b)
        elif i == num2:
            answers.append(a)
        else:
            answers.append(my_string[i])
    answer = ''.join(map(str,answers))
    return answer

def solve():
    my_string = "hello"
    num1 = 1
    num2 = 2
    answer = solution(my_string,num1,num2)
    print("{}".format(answer))
    return

solve()