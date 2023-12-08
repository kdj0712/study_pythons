def multiply(): #펑션에 multiply라는 이름을 부여합니다.
    while True: #아래의 조건이 참인지 확인합니다.
        first = input("서로 곱할 첫번째 수를 입력하세요 : ") # 첫번째 숫자를 입력받습니다.

        if first == 'q': # 입력받은 숫자에 'q'라는 문자가 있는지를 확인합니다.
            return 'q'   # 'q'를 입력받은 것을 호출할수 있도록 합니다.

        second = input("서로 곱할 두번째 수를 입력하세요 : ") # 두번째 숫자를 입력받습니다.

        if second == 'q': # 입력받은 숫자에 'q'라는 문자가 있는지를 확인합니다.
            return 'q'    # 'q'를 입력받은 것을 호출할수 있도록 합니다.
        sum = int(first) * int(second) 
        # 첫번째 숫자와 두번째 숫자를 문자형 타입에서 숫자형 타입 정수로 변경한 뒤 이를 곱합니다.
        print("두 수의 곱셈의 값은 {} 입니다.".format(sum)) # 두 수의 곱셈의 결과를 지정된 문구와 함께 출력합니다.
        return sum # 계산한 결과값을 호출할 수 있도록 합니다.

def repeat(): #펑션에 repeat라는 이름을 부여합니다.
    while True: #아래의 조건이 참인지를 확인합니다.
        result = multiply() # 펑션multiply의 기능을 호출합니다. 그리고 result라는 변수로 지정합니다.

        if result == 'q': #입력받은 값에서 'q'라는 문자가 있는지 확입합니다.
           break          #만약 'q'를 입력 받았다면 정지
repeat()
