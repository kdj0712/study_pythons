# # 직육면체의 면적을 구하는 프로그램의 제작
# print("가로 세로 높이를 입력하세요")
# str_width = input()
# str_length = input()
# str_height = input()
# print("가로({}) m * 세로 ({})m * 높이({})m =".format(str_width,str_length,str_height))
# num_width = int(str_width)
# num_length = int(str_length)
# num_height = int(str_height)
# print(num_width*num_length*num_height)
# # print("가로 세로 높이를 입력하세요")
# # str_width,str_length,str_height="가로"input("{}".format(str_width))"m *""세로"("{}".format(str_length))"m *""높이"("{}".format(str_heigh))"m = "
# # num_width = int(str_width)
# # num_length = int(str_length)
# # num_height = int(str_height)
# # num_answer = num_width*num_length*num_height
# # print("가로 * 세로 * 높이 = {}m^3".format(num_answer))

print("가로 세로 높이를 입력하세요")
num_width,num_length,num_height = input().split()
width = int(num_width)
length = int(num_length)
height = int(num_height)
answer = width * length * height 
print("가로({})m * 세로({})m * 높이({})m = ({})m^3".format(width,length,height,answer))

