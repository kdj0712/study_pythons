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