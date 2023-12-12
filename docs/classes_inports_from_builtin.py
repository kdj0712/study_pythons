# 내장 함수는 instance 하지 않아도, 기본적으로 사용을 전제하고 있기 때문에
# 별도의 instance를 진행하지 않는다.
import os

# 현재 폴더 위치를 알려주는 function. 'CLI 의 pwd' 와 동일한 기능
current_forder = os.getcwd()
print("현재 실행되는 python의 위치 {}".format(current_forder))

# 현재 위치한 폴더가 가지고 있는 파일과 폴더 '리스트' 출력 - list type
file_folder_list =  os.listdir(current_forder)
print("파일과 폴더 리스트 : {}".format(file_folder_list))

pass

# 'doc api를 통해' api들의 기능들을 확인하는 것이 가능하다.