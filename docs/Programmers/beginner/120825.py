# (https://school.programmers.co.kr/learn/courses/30/lessons/120825)

# 문제

# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

def solution(my_string, n):
    
    i = len(my_string)
    answer = []
    for i in range(len(my_string)):
        answer.append((my_string[i])*(n))
    answer =''.join(map(str, answer))
    return answer

def solve():
    my_string = "hello"
    n = 3
    answer = solution(my_string, n)
    print(answer)
    return

solve()