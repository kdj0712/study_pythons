# (https://school.programmers.co.kr/learn/courses/30/lessons/120585)

# 문제

# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다.

# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.



def solution(array, height):
    height = int(height)
    answer = []
    answer = array
    if height in answer:
        if answer.count(height) == 1:
            answer = sorted(answer)
            answer = len(answer) - len(range(answer.index(height)+1))
        elif answer.count(height) > 1:
            new_answer = [item for item in answer if item != height] 
            answer = list(set(new_answer)) 
            answer = new_answer.append(height)
            answer = sorted(new_answer)
            answer = len(answer) - len(range(answer.index(height)+1))
    else:
        array = array.append(height)
        answer = sorted(answer)
        answer = len(answer) - len(range(answer.index(height)+1))
    return answer

def solve():
    array = [180, 120, 140, 190, 191, 190, 150, 150, 167]
    height = 167
    answer = solution(array, height)
    print(answer)
    return

solve()