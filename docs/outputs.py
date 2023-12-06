# 변수 선언  후 정의할 떄 고려할 부분(넣는 값 = 문자 or 숫자)
# 문자 출력
helloworld="hello, world, Deok Jae Kim." #(문자형 변수)
print(helloworld)

# 숫자 합산 출력
numbers = 3 + 5     #(숫자형 변수)
print(numbers)

# 데이터 타입 : 문장형 or 숫자형 등 변수에 대한 정의

# if 구문 사용
print(numbers)

if 5 > 2: # (콜론): 과 tab은 한 쌍의 묶음이다.
  
  print("Five is greater than two!")
print("end")

# 1라인에 출력하기
first = "First"
second = "Second"
print("first : {}".format(first), end=", 다음 줄")
print("second : {}".format(second))
print("End Program!")