# 기본 function 형식 - stand-bying. 호출되었을 때만 기능.
def function_name(): 
    pass       # 기능할 내용 입력하는 자리
    return 0

## 그냥 연습
def my_function():
  print("Hello from a function")

# function의 호출
my_function()
pass

# 문항과 답항을 출력하는 function으로서의 역할을 부여
def print_question_and_answer():
    str_anyone="1. 컴퓨터 사용에 있어 가장 중요하다고 생각하는 요소는 무엇인가요?"
    print(str_anyone)
    str_anyone="1.1. 빠른 처리 속도 1.2. 편리한 사용자 인터페이스  1.3. 안정적인 시스템 운영  1.4. 다양한 기능  1.5. 높은 보안성"
    print(str_anyone)
    return 0

# print_question_and_answer()
