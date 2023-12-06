# 사용 이유 : 복수의 값의 모임을 쉽계 전달
# 숫자 5개의 항목으로 이루어진 리스트
list_numerics = [0, 1, 2, 3, 4]
# 문자 3개의 항목으로 이루어진 리스트
list_fruits = ["apple", "banana", "cherry"]
# 숫자와 문자가 융합된 리스트도 가능하기는 하다. 다만 권장하지 않는 사용 방식
list_mixs = [0, 1, 2, 3,"apple", "banana",]
# 디버깅 모드에서 해당 리스트의 항목 개수를 확인할 수 있는 방법
len(list_numerics)
# 5
len(list_mixs)
# 6

## for문 활용 후 다시 오기

# index(색인 = 위치값)
# index 로 값 확인하여 가져오기
# list_fruits [0] # 색인하는 인덱스도 개별적인 변수로 볼 수 있다. = 1차원(행)
# 'melon'
# list_fruits [3]
# 'cherry'
# 보유하고 있는 값의 개수보다 큰 위치값으로 문의하는 경우
# list_fruits [5]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range
list_fruits = ["melon","apple", "banana", "cherry"]
pass