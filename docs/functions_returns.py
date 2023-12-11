###### private test ####
# def add(): 
#     first = int(input("합을 구할 첫번째 수를 입력하세요 : "))
#     second = int(input("합을 구할 두번째 수를 입력하세요 : "))
#     sum = first + second
#     print("두 수의 합은 {} 입니다.".format(sum))
#     return 0
# add()
########################

## call by reference ##
# 나오는 값의 처리
# first = 5
# second = 4
# sum = first + second\
def add(): 
    first = 5
    second = 4
    sum = first + second
    # return 0
    return sum        # 리턴은 변수를 대부분 사용한다.(다른 언어는 상수를 쓰는 경우도 있으나, python에서는 대부분 변수)

# num_sum = 0 
num_sum = add()
print("add() return의 결과 : {}".format(num_sum))

# num_first = 4
# num_second = 5
# # 곱셈 연산
# num_first * num_second

# 두 수를 곱해서 결과 리턴하여 출력
def multiply(): 
    num_first = 4
    num_second = 5
    # 곱셈 연산
    result = num_first * num_second
    pass       # 기능할 내용 입력하는 자리
    return result   # call 을 하면 넘어오는 Value의 값을 선언
num_multiply = multiply()
print("num_multiply() return value : {}".format(num_multiply))

list_fruits = ["melon","apple", "banana", "cherry"]
list_fruits[0]
def return_list(): 
    list_fruits = ["melon","apple", "banana", "cherry"]
    return list_fruits  # 묶여있는 값을 1개라고 인식하기 때문에 list를 value로 지정할 수 있다.
print("return_list() return result : {}".format(return_list()))

# 리스트에 입력된 내용 중 특정 값을 index로 return
def return_listbyindex(): 
    list_fruits = ["melon","apple", "banana", "cherry"]
    return list_fruits[0] # 단일 변수로 여김 1차원(행)
print("return_listbyindex() return result : {}".format(return_listbyindex()))

# 인용
# my_score = 79
# if my_score >= 90:   # 90점 이상
#     print("당신의 점수는 {}점 이상이기에 A 등급 입니다.".format(my_score))
# elif my_score > 80:  # 80점 초과 : B
#     print("당신의 점수는 {}점이라 B 등급 입니다.".format(my_score))
# else :          # 나머지 : F
#     print("당신의 점수는 {}점 이하이기 때문에 F 등급 입니다.".format(my_score))

# 반복 print 작업을 줄이기 위한 function 제작
def return_grade(): 
    my_score = 79
    my_grade = ''
    if my_score >= 90:   # 90점 이상
        my_grade = 'A'
    elif my_score > 80:  # 80점 초과 : B
        my_grade = 'B'
    else :          # 나머지 : F
        my_grade = 'F'
        # return_listbyindex()  # 한 번 만들어진 function은 다른 function 내부에도 호출하는 것이 가능하다.
    return my_grade
str_grade = return_grade()
print("당신의 학점 : {}입니다. " .format(str_grade))