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

# list 초기화 방식
list_fruits_primitive = ["melon", "apple", "banana", "cherry"]

# 튜플은 소괄호를 이용해 값을 집합으로 묶는 방식으로 값을 저장한다.
# 튜플은 생성된 이후에는 그 내용을 변경할 수 없다.
# 그러한 규칙을 불변성이라 하는데 list에 그 값을 넣은 후 값을 추가하거나, 변경하는 것으로 우회할 수 있다.
tuple_fruits = ("melon","apple", "banana", "cherry")
list_fruits_constructer = list(("melon","apple", "banana", "cherry"))
# 특정 데이터를 추가하고자 할 경우
# list_fruits_primitive.append("strawberry")
# list_fruits_constructer.append("watermelon")

# 특정 데이터를 제거하고자 할 경우
# 이 경우는 데이터 값의 length가 줄어든다.(ex: 5개 -> 4개)
# list_fruits_primitive.remove("apple")
# list_fruits_constructer.remove("melon")

# 대상 list의 모든 아이템을 없애고 list를 초기화 하는 방식
# list_fruits_primitive.clear()

pass