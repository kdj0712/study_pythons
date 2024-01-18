# https://www.acmicpc.net/problem/3052

# 문제

# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 입력

# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

# 출력

# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
def conditions():
    numbers=[]
    for i in range(10):
        number = int(input())
        remain = number%42
        numbers.append(remain)
    return numbers

def use_set(numbers):
    numbers_set = set(numbers) #연산을 할 때 결과가 제일 빠르고 구문도 단순한 편이다.
    total = len(numbers_set)
    return print(total)

def not_in(numbers): # 비교군인 입력받는 값이 많아질 경우 모두 비교하기 때문에 연산이 많아져서 속도면에서 불리
    total = 0
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    total = len(unique_numbers)
    return print(total)

def use_if(numbers): # 동일한 것이 있을 경우 바로 구문을 빠져나오기 떄문에 간결한 편이나 구문이 복잡한 편
    unique_numbers = []
    for num in numbers:
        found = False
        for unique_num in unique_numbers:
            if unique_num == num:
                found = True
                break
        if not found:
            unique_numbers.append(num)
    total = len(unique_numbers)
    return print(total)

condition = conditions()   
# not_in(condition)
# use_set(condition)
use_if(condition)