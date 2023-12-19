# function에 들어가는 값(들) - data type으로 정의된 모든 값들은 입력되는 것이 가능하다.

def add(first, second) : #호출 시 변수에 값이 할당됨
    sum = first + second
    return sum         # 상수 대신 변수 사용

if __name__ == "__main__": # import가 잘 되었는지 확인하는 것이 가능하다.
# __name__                 # import 상태가 아닐 때 debug console에서 확인하면
# '__name__'               # 
# __name__
# 'functions_parameters'

    # num_sum = 0 
    num_sum = add(5,4) # 상수 parameters 사용
    print("add() return의 결과 : {}".format(num_sum))
    third = 6
    fourth = 10
    num_sum = add(third, fourth) # function 호출하면 값들만 전달됨
    print("add() return의 결과 : {}".format(num_sum))

#입력 받은 점수를 계산하여 학점으로 출력하는 Function 
def return_grade(my_score):       # 자신을 호출할 때 값(들)이 들어감.(순서 매칭 가능)
    my_grade = ""
    if my_score >= 90:   # 90점 이상
        my_grade = "A"
    elif my_score > 80:  # 80점 초과 : B
        my_grade = "B"
    else :          # 나머지 : F
        my_grade = "F"
        # return_listbyindex()  # 한 번 만들어진 function은 다른 function 내부에도 호출하는 것이 가능하다.
    return my_grade

if __name__ == "__main__":
    # str_grade = return_grade(99) #호출할 시 값들이 넘어감(순서 매칭)
    # print("당신의 학점 : {}입니다. " .format(str_grade))
    my_score = 88
    str_grade = return_grade(my_score) 
    print("당신의 학점 : {}입니다. " .format(str_grade))