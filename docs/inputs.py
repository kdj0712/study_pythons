# #input()에 대한 기본 사용
# str_start = "Programming Start!"
# print("{}".format(str_start)) #출력
# str_input_desc = "영문이름 입력"
# str_input = input("{}".format(str_input_desc)) #입력
# pass #종료

# input()에 대한 숫자 받아 환산 하기
# 풀기 : 출생년도 입력받아 나이 계산 
# (ex. 2021(올해) - 2000(본인의 출생년도) = 21)
str_start = "Programming Start!"
print("{}".format(str_start)) #출력
str_input_desc = "출생년도 입력"
num_input_birthyear = input("{}".format(str_input_desc)) #입력
num_age = 2023 - int(num_input_birthyear)
print("출생년도 기준 현재 당신의 나이 계산 :{}살".format(num_age))
pass #종료