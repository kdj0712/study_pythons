#  (https://school.programmers.co.kr/learn/courses/30/lessons/120905)

# 문제

# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n,numlist):
    answer = []
    for x in range(len(numlist)):
        if numlist[x]%n == 0:
            answer.append(numlist[x])
        else:
            pass
    return answer

def solve():
    n = 3
    numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    answer = solution(n, numlist)
    print(answer)
    return

solve()