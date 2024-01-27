# (https://school.programmers.co.kr/learn/courses/30/lessons/120854)

# 문제

# 정수 배열 numbers가 매개변수로 주어집니다.

# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

def solution(strlist):
    answer = [0] * len(strlist)
    for i in range(len(strlist)):
        s = len(strlist[i])
        answer[i] = s
    pass
    return answer

def solve():
    strlist = ["I", "Love", "Programmers."]
    answer = solution(strlist)
    print("{}".format(answer))
    return

solve()