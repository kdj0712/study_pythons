# 같은 폴더에 있는 class and functions 호출
# basic style
# 1. import 
import Classes_format 
# 2. class instance
person = Classes_format.Person() # 변수로 클래스에 내재된 function을 선언한다.
arithmetics = Classes_format.Arithmetics()
class_name = Classes_format.Class_name()
#{기본적으로 내재된 __init__를 호출하면서, Class가 내포하고 있는 모든 자원을(다른Function들을) 불러오는 역할을 한다.}
# 3. call function()
person.add_age()

# import 이후 주로 사용되는 방식
from Classes_format import Person, Arithmetics, Class_name
person = Person()
arithmetics = Arithmetics()
class_name = Class_name()

pass