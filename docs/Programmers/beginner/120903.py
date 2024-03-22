#  (https://school.programmers.co.kr/learn/courses/30/lessons/120903)

# 문제

# 두 배열이 얼마나 유사한지 확인해보려고 합니다.

# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(str1, str2):
    answer = 0
    for x in range(len(str2)):
        if str2[x] in str1: 
            answer = answer + 1
        else:
            answer
    return answer

def solve():
    str1 = ["a", "b", "c"]
    str2 = ["com", "b", "d", "p", "c"]
    answer = solution(str1, str2)
    print(answer)
    return

solve()