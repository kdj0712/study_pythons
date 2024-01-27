# (https://school.programmers.co.kr/learn/courses/30/lessons/120813)

# 문제

# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

def solution(y):
    num_list = [j for j in range(1,int(y)+1)]
    num_list
    answer = [0]
    if y%2 == 0:
        s = y/2
        s = int(s)
    elif y%2 != 0:
        s = (y/2) + 1
        s = int(s)
        pass
    answer = answer * s
    z = 0
    for i in range(y):
        if num_list[i] % 2 != 0:
            answer[z] = num_list[i]
            z = z + 1
        elif num_list[i] %2 == 0:
            pass
    return answer

def solve():
    y = 15
    answer = solution(y)
    print(answer)
    return

solve()