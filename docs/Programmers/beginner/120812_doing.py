# (https://school.programmers.co.kr/learn/courses/30/lessons/120812)

# 문제

# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 

# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

def solution(array):
    a = []
    b = []
    new_answer = [item for item in array if item != array] 
    for i in range(len(array)):
        y = array.count(array[i]) 
        if y == 1:
            s = y
            b.append({str(array[i]):str(s)})
        elif y > 1:
            s = y
            b.append({str(array[i]):str(s)})
            new_answer = [item for item in array if item != array.count(i)] 
            array = new_answer

        pass
    answer = array[s]
    return answer

def solve():
    array = [1, 2, 2 ,3 ,3, 3, 3]
    answer = solution(array)
    print("{}".format(answer))
    return

solve()