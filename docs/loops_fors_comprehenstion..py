

# 압축된 For문
numerics = [0, 1, 2, 3, 4]
numerics_list = []
for number in numerics: # for in = for 문이 작용할 위치를 지정
    result = number + 2
    numerics_list.append(result)
    pass
print(numerics_list)

print ([number+2 for number in numerics])
pass