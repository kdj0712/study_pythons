pass
type("deokjaeKim") # 문자 타입
# <class 'str'>
type(2000) # 숫자 타입
# <class 'int'>
name = "deokjaeKim" # 문자 타입
type(name) # 변수 지정
# <class 'str'>
age = 24 # 숫자 타입
type(age) # 변수 지정
# <class 'int'>

#터미널 입력 값에 대한 확인
str_input = input("문자 입력 :")
print("입력({}) type 표시 : {}".format(str_input,type(str_input)))
num_input = input("숫자 입력 :")
print("입력({}) type 표시 : {}".format(num_input,type(num_input)))

# cast = data type 변경
int(num_input)
# 2010
type(int(num_input))
# <class 'int'>

# cast 불가한 경우
# mix_val = "23k"
# int(mix_val)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '23k'
pass