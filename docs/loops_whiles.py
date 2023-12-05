# condition이 True인 동안 동작
# while True:
#     pass

# 풀기 : 구구단 5단의 결과 매번 출력
num_virtual = 0
while True :
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    if num_virtual >= 5:
        pass
        break
    pass

num_virtual = 0
# While의 정지가 되는 첫번째 방법 : Case with Break
while True :
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    if num_virtual >= 5:
        pass
        break
    pass

# While의 정지가 되는 첫번째 방법 : Case without Break
num_virtual = 0
while num_virtual < 5:
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    pass
print("End Program!")