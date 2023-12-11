class Arithmetics:
    def __init__(self): 
        pass            

    def add(self) : 
        first = int(input("첫번째 : "))
        second = int(input("두번째 : "))
        sum = first + second
        print("두 수의 합계는 {} 입니다.".format(sum))
        return sum

    def minus(self) :
        first = int(input("첫번째 : "))
        second = int(input("두번째 : "))
        result = first - second
        print("두 수의 차이는 {} 입니다.".format(result))
        return result
    
    def times(self) :
        first = int(input("첫번째 : "))
        second = int(input("두번째 : "))
        result = first * second
        print("두 수의 곱은 {} 입니다.".format(result))
        return result
    
    def devine(self) :
        first = int(input("첫번째 : "))
        second = int(input("두번째 : "))
        dev = first / second
        print("두 수를 나눈 값은 {} 입니다.".format(float(dev)))
        return dev
    

arithmetics = Arithmetics()
arithmetics.add()
arithmetics.minus()
arithmetics.times()
arithmetics.devine()
pass