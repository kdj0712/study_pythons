# def multiply():
#     while True:
#         first = input("서로 곱할 첫번째 수를 입력하세요 : ")

#         if first == 'q':
#             return 'q'

#         second = input("서로 곱할 두번째 수를 입력하세요 : ")

#         if second == 'q':
#             return 'q'

#         sum = int(first) * int(second)
#         print("두 수의 곱셈의 값은 {} 입니다.".format(sum))
#         return sum

# def repeat():
#     while True:
#         result = multiply()

# #         if result == 'q':
# #            break
# # repeat()



# def repeat():
#     while True:
#         first = input("서로 곱할 첫번째 수를 입력하세요 : ")

#         if first == 'q':
#             break

#         second = input("서로 곱할 두번째 수를 입력하세요 : ")

#         if second == 'q':
#             break

#         multiply(int(first), int(second))

# def multiply(first, second):  
#     sum = first * second
#     print("두 수의 곱셈의 값은 {} 입니다.".format(sum))

# repeat()


list_question = ["1. 문제: Python에서 변수를 선언하는 방법은?", 
                 "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요?", 
                 "3. 문제: Python에서 조건문을 작성하는 방법은?", 
                 "4. 문제: Python에서 함수를 정의하는 방법은?"]

question_grade = [10, 15, 10, 5]  # 문제별 점수를 저장하는 리스트

list_option = ["1) var name, 2) name = value, 3) set name, 4) name == value", 
               "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다", 
               "1) if-else, 2) for-in, 3) while, 4) def", "1) class, 2) def, 3) import, 4) return"]

correct_list = [2,1,1,2] # 문제의 실제 정답 리스트

answer_list = []  #입력받은 정답 리스트 

for i in range(len(list_question)) :
    print("{} (점수: {}점)".format(list_question[i], question_grade[i]))  # 각 문제와 그에 해당하는 점수를 출력합니다.
    print("{}".format(list_option[i]))
    get_num = int(input("정답 : "))
    answer_list.append(get_num)  # 사용자의 답을 리스트에 추가합니다.

print("{}".format(answer_list))

def match_point(correct_list, answer_list, question_grade):
    result = []
    for i in range(len(correct_list)):
        if correct_list[i] == answer_list[i]:
            result.append((question_grade[i],True))
    return result

def check_answers():
    result = match_point(correct_list, answer_list, question_grade)
    sum, right = calculate_score(result)
    str_grade = grade(sum)
    print("당신의 점수는 {}점 입니다.".format(sum))
    print("당신의 학점은 {}입니다.".format(str_grade))


def calculate_score(data):
    sum = 0
    right = 0
    for points, is_correct in data:
        if is_correct:
            sum += points
            right += 1
    return sum, right
    

def grade(sum):
    my_grade = ''
    if sum >= 30:
        my_grade = 'A'
    elif sum > 20:
        my_grade = 'B'
    else:
        my_grade = 'F'
    return my_grade

# 이후에는 앞서 작성하신 후반부 코드를 이어서 작성하시면 됩니다.
check_answers()