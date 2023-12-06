# 얼마나 반복할 것인가에 대한 값들을 알려줌

#for 리스트의 속성의 값 in 리스트 이름 = 변수
# for number in numerics: # for in = for 문이 작용할 위치를 지정
#     pass
#     print(number)

# 성격이 다른 변수들을 지정하고 추가로 계속 입력하는 것이 가능
# 내가 입력한 변수의 개수 만큼 반복
numerics = [0, 1, 2, 3, 4] # 5개의 값으로 이루어지 리스트 (묶음)

# x = For 구문 내에서만 사용 가능한 변수 
#기본 구문
for x in []:
    pass

# 문자 3개의 항목으로 이루어진 리스트

for x in ["apple","melon", "banana", "cherry"]:  # 반복 대상 리스트 직접 입력
    pass
    print("fruit name : {}!".format(x))
list_fruits = ["apple", "banana", "cherry"]
print("End Program!")

# fruit name : apple!
# fruit name : banana!
# fruit name : cherry!

for str_fruit in list_fruits :  # 반복 대상 리스트 직접 입력
    pass
    print("fruit name : {}!".format(str_fruit))
list_fruits = ["apple","melon", "banana", "cherry"]
print("End Program!")

numerics = [0, 1, 2, 3, 4]
for number in numerics: # for in = for 문이 작용할 위치를 지정
    pass
    #print("Number : {}".format(number))
    print("Number : {}".format(number+2))
print("End Program!")

## 설문답변 받기
# 1. 컴퓨터 사용에 있어 가장 중요하다고 생각하는 요소는 무엇인가요?
# A. 빠른 처리 속도   B. 편리한 사용자 인터페이스   C. 안정적인 시스템 운영   D. 다양한 기능   E 높은 보안성
# 당신은 {} 번을 선택하셨습니다.
# 2. 주로 사용하는 컴퓨터의 운영체제는 무엇인가요?
# A. Windows   B. Mac OS   C. Linux   D. Chrome OS   E 기타
# 당신은 {} 번을 선택하셨습니다.
# 3. 개발자에게 인기있는 운영체제는 무엇인가요?
# A. Windows   B. Mac OS   C. Linux   D. Chrome OS   E 기타
# 당신은 {} 번을 선택하셨습니다.

list_polls =["1. 컴퓨터 사용에 있어 가장 중요하다고 생각하는 요소는 무엇인가요?" 
            ,"A. 빠른 처리 속도   B. 편리한 사용자 인터페이스   C. 안정적인 시스템 운영   D. 다양한 기능   E 높은 보안성"
            ,"2. 주로 사용하는 컴퓨터의 운영체제는 무엇인가요?"
            ,"A. Windows   B. Mac OS   C. Linux   D. Chrome OS   E 기타"
            ,"3. 개발자에게 인기있는 운영체제는 무엇인가요?"
            ,"A. Windows   B. Mac OS   C. Linux   D. Chrome OS   E 기타"
            ]
# for num_count in [0,2,4]:
#     # str_content = list_polls[num_count]
#     # print("{}".format(str_content))
#     str_question = list_polls[num_count]
#     print("{}".format(str_question))
#     str_answer = list_polls[num_count+1]
#     print("{}".format(str_answer))
#     input("당신의 선택은?(A~E를 1,2,3,4,5 중 선택) : ")
#     print("------------------------")
#     pass
# print("End Program!")

# 각 항목 별 많이 입력받은 값의 항목 당 개수를 구하는 방식
list_statistics = [0,0,0,0,0] # 답항의 개수 만큼 0을 기재함

for num_count in [0,2,4]:
    # str_content = list_polls[num_count]
    # print("{}".format(str_content))
    str_question = list_polls[num_count]
    print("{}".format(str_question))
    str_answer = list_polls[num_count+1]
    print("{}".format(str_answer))

    str_questions_result = input("당신의 선택은?(A~E를 1,2,3,4,5 중 선택) : ")
    num_questions_result = int(str_questions_result) #문자를 숫자로 변환
    index = num_questions_result - 1 # index의 위치값
    list_statistics[index] = list_statistics[index] + 1
    
    print("------------------------")
    pass

print("선호하는 답항 : {}".format(list_statistics))

print("End Program!")