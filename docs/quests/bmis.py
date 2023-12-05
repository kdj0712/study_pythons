num_weight, num_height = input().split()
weight = int(num_weight)
height = int(num_height)*0.01
bmi = weight/height**2

print("BMI{} = 체중{}kg / (키{}m의 제곱)".format(bmi,weight,height) )

if 18 > bmi:
    pass
    print("당신의 BMI 지수 ({}) 는 18 미만이므로 저체중입니다.".format(bmi))
elif 18 <= bmi:
    pass
    print("당신의 BMI 지수 ({}) 는 18 이상 22이하이므로 정상체중입니다.".format(bmi))
elif 23 <= bmi: 
    pass
    print("당신의 BMI 지수 ({}) 는 22 초과 24이하이므로 과체중입니다.".format(bmi))
else :
    pass
    print("당신의 BMI 지수 ({}) 는 25를 넘으므로 비만체중입니다.".format(bmi))
print("End Program!")