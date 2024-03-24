#  (https://school.programmers.co.kr/learn/courses/30/lessons/120904)

# 문제

# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

def solution(num,k):
    s = str(num)
    answer = 0
    for x in range(len(s)):
        if str(k) == s[x]:
            answer = x+1
            break            
        else:
            answer = -1
    return answer

def solve():
    num = 123456
    k = 7
    answer = solution(num, k)
    print(answer)
    return

solve()