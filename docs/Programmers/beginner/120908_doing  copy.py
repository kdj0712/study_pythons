#  (https://school.programmers.co.kr/learn/courses/30/lessons/120908)

# 문제

# 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(str1, str2):
    # strs1 = [0] * len(str1)
    # strs2 = [0] * len(str2)
    # for i in range(len(str1)):
    #     strs1[i] = str1[i]
    # for j in range(len(str2)):
    #     strs2[j] = str2[j]
    # pass
    if set(str1,str2) == True:
        answer = 1
    else:
        answer = 2 
    return answer

def solve():
    str1 = "ab6CDE443fgh22iJKlmn1o"
    str2 = "6CD"
    answer = solution(str1, str2)
    print(answer)
    return

solve()