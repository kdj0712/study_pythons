# Class의 기본 구조(Ref)
class Class_name:
    def __init__(self): # 자체적으로 내재되어 있는 function(Class 생성자)
        pass            # (기술하지 않아도 원래 내포하고 있으며 자동으로 반영된다.)
                        # 초기 상태를 설정하는 등의 작업이 필요하므로 직접 작성하여 사용한다.
                        # return을 기재하지는 않지만, 모든 자원을 return한다.(다른 Function들)
    def function_name(self): #self = 이 function이 class에 종속되어 있음을 선언하는 키워드
        pass
        return 0

# 동일한 작업중에 있는 경우 Import가 필요하지 않다.
# 사용하는 기본 순서는 아래와 같다. 
# 1. import (같은 파일에 있을 경우 생략)
# 2. class instance
# 3. function

class Person:
    def add_age(self): # 클래스가 갖고 있는 자원들에 대한 종속의 확인을 위한
        pass
        print("45세")
        return 0

# 2. class instance
person = Person() # 변수에 클래스를 담는다.
#{기본적으로 내재된 __init__를 호출하면서, Class가 내포하고 있는 모든 자원을(다른Function들을) 불러오는 역할을 한다.}
# 3. call function()
person.add_age()


# 사칙 연산 되는 class 생성(덧셈과 뺄셈만 우선 작성)
class Arithmetics:
    def __init__(self): 
        pass            

    def add(self, first, second) : #호출 시 변수에 값이 할당됨
        sum = first + second
        return sum  

    def minus(self, first, second) :
        result = first - second
        return result

arithmetics = Arithmetics()
print(arithmetics.add(5,6))
pass