# (https://school.programmers.co.kr/learn/courses/30/lessons/120833)

# 문제

# 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, 

# numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(numbers,num1,num2):
    answer=[]
    for i in range(num1,(num2+1)):
        answer.append(numbers[i])
    return answer

def solve():
    numbers = [1, 2, 3, 4, 5 , 6 , 7 , 8 , 9 , 10 ]
    num1 = 3
    num2 = 8
    answer = solution(numbers,num1,num2)
    print("{}".format(answer))
    return

solve()