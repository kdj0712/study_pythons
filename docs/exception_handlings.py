# 기본 구문
try :
    pass   # 업무 코드
except:
    pass   # 업무 코드가 문제 발생 시 대처 코드
finally:
    pass   # try or except이 끝난 후 무조건 실행되는 코드
# pure python with calculate

# num_first = '4'
num_first = 4
num_second = 5
# 곱셈 연산

try :
    result = num_first / num_second
    pass   # 업무 코드
except:
    result = int(num_first) / int(num_second)
    pass   # 업무 코드가 문제 발생 시 대처 코드
finally:
    pass   # try or except이 끝난 후 무조건 실행되는 코드

print("{} / {} = {}".format(num_first, num_second, result))
pass
