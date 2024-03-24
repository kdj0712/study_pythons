# (https://school.programmers.co.kr/learn/courses/30/lessons/120850)

# 문제

# 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.


def solution(my_string):
    answer = []
    for x in range(len(my_string)):
        try:
            num = int(my_string[x])
            answer.append(num)
        except:
            pass
    answer.sort(reverse=False)
    return answer

def solve():
    my_string = "hi123926"
    answer = solution(my_string)
    print("{}".format(answer))
    return

solve()