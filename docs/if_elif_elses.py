# 기본 if else - else 구문
if True : 
    pass

elif True :
    pass

else :
    pass
# 질문 형식(condition) = 변수 + 부등호 + 기준값
# 문자 비교 (기준 예시)
str_name = "deokjae Kim"
# 문자를 긍정형으로 질문
if str_name == "deokjae Kim" :
    pass
    print("name is {}".format(str_name))

# 문자를 부정형으로 질문
if str_name != "deokjae Kim" :
    pass
    print("name is not {}".format(str_name))

# if else 구문 사용 방법
# num_first >= 4 -> 'True = 큼', 'False = 작음'
#  두가지 중 하나를 선택하여 출력

num_first = 5
# if num_first >= 4 : # 무조건 둘 중 하나를 표현해야 하는 경우 사용
if num_first >= 6 : # 무조건 둘 중 하나를 표현해야 하는 경우 사용
    pass # condition이 true라면 실행
    print("{}는 4보다 크다".format(num_first))
else :
    pass # condition이 False라면 실행
    print("{}는 4보다 작다".format(num_first))

# if - elif - else 모두 동시 사용
# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B , 나머지 : F 
my_score = 90

if my_score >= 90:   # 90점 이상
    pass
    print("당신의 점수는 {}점 이상이기에 A 등급 입니다.".format(my_score))
elif my_score > 80:  # 80점 초과 : B
    pass
    print("당신의 점수는 {}점이라 B 등급 입니다.".format(my_score))
else :          # 나머지 : F
    pass
    print("당신의 점수는 {}점 이하이기 때문에 F 등급 입니다.".format(my_score))
print("End Program!")