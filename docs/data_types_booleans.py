bool_flag = True   # = yes
pass
bool_flag = False
type(bool_flag)
# <class 'bool'>

# 문자 판단 
str_name = "deokjae kim" # 입력된 값
str_name == "deokjae Kim" # 동일한 것을 확인할 때
True
str_name == "deokjaeKim" # 다른것을 확인할 때
False
## 같지 않음 기호 '!='
str_name != "deokjaeKim" # 동일하지 않다는 의미로 질문하였을 때 나오는 결과값
True
# str_name = "deokjae Kim" 인데  "deokjaeKim"은 동일하지 않고,
# 동일하지 않다는 질문을 하였으므로 True가 나오는 것이 맞다.

# 숫자에 대한 판단 ( 변수 + 부등호 + 기준값 )
# 컴퓨터의 입장을 확인
# True = Yes = 1, False = No = 0
5 == 4
# False
num_first = 5
num_first == 4
# False
num_first != 4
# True
num_first > 4    # 초과
# True
num_first >= 4   # 이상
# True

# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B , 나머지 : F 
# 90<=A<=100
# b<90
# c<80
my_score = 90
my_score >= 90
# True
my_score = 89
my_score >= 90
# False
my_score = 80
my_score > 80
# False


# 인간의 언어로 Yes, No 를 판단하는 근거
# ex) 정의는 정의하기 어렵다. -> 부정적(No)
# 정의는 정의하기 어렵지 아니하다. -> 긍정적(Yes)

# 50점 이상부터 60점 이하는 C 학점이다. -> 대상이 없을 경우 판단이 어려움

# 컴퓨터는 상태를 확인할 때 논리 연산자(True, False)를 사용.

# 75점 이상부터 85점 이하는 C 학점이다. (and 조건)
my_score >= 75
# True
my_score <= 85
# True
my_score >= 75 and my_score <= 85
# True

# 논리(True or False) 연산자(결과값)
# and : 1 and 1 -> 나머지는 0
# or : (~도 되고, ~도 된다) 0 or 0 -> 나머지는 1
# not : 반대로 변환
not my_score <= 85
# False
not (my_score <= 85)
# False

pass