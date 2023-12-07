# def multiply():
#     while True:
#         first = input("서로 곱할 첫번째 수를 입력하세요 : ")

#         if first == 'q':
#             return 'q'

#         second = input("서로 곱할 두번째 수를 입력하세요 : ")

#         if second == 'q':
#             return 'q'

#         sum = int(first) * int(second)
#         print("두 수의 곱셈의 값은 {} 입니다.".format(sum))
#         return sum

# def repeat():
#     while True:
#         result = multiply()

#         if result == 'q':
#            break
# repeat()



def repeat():
    while True:
        first = input("서로 곱할 첫번째 수를 입력하세요 : ")

        if first == 'q':
            break

        second = input("서로 곱할 두번째 수를 입력하세요 : ")

        if second == 'q':
            break

        multiply(int(first), int(second))

def multiply(first, second):  
    sum = first * second
    print("두 수의 곱셈의 값은 {} 입니다.".format(sum))

repeat()
