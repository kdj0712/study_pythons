# Class 초기화 방법
dict_initial = {} # empty
dict_initial = dict() # empty

list_car_info = ["Ford", "Mustang", 1964]
# data type의 종류가 다른 List는 사용성이 좋지 않다.
# dictionary는 값을 부여하면서 값의 정보(key)를 함께 저장할 수 있다.
# key(str로 거의 구성),value(여러 종류 가능str, float, int, list, dic, etc ....)
# key : value , 를 계속 이어붙여서 항목을 추가로 입력한다.
dict_carinfo = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "items" : [],
    }
# 리스트로 데이터를 access할 때는 주로 dictionary를 사용하자
model = dict_carinfo["model"]
print("dict_carinfo에 있는 model name : {}".format(model))

# key 값을 이용하여 value를 변경
dict_carinfo["year"] = 1970
# 새로워진 key와 key 값의 정의
dict_carinfo["color"] = "red"
dict_carinfo["color"] = {"red","yellow","brown"}

pass
