def multiply():
    while True:
        number = input("확인할 구구단을 입력해 주세요 : ")
        if number == 'q':
            break
        for num_base in [1,2,3,4,5,6,7,8,9]:
            pass
            num_number = int(number)
            print("{} * {} = {}".format(num_number,num_base,num_number*num_base))
            pass
#하단 코드 없이도 작동 했음

# def repeat():  
#     while True:
#         result = multiply()

#         if result =='q':
#             break
multiply()