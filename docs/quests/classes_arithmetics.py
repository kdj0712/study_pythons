class Arithmetics:
    def __init__(self): 
        pass            

    def add(self, first, second) : #호출 시 변수에 값이 할당됨
        sum = first + second
        return sum  

    def minus(self, first, second) :
        result = first - second
        return result
    
    def times(self, first, second) :
        result = first * second
        return result
    
    def devine(self, first, second) :
        dev = first / second
        return float(dev)
    

arithmetics = Arithmetics()
print(arithmetics.minus(7,5))
print(arithmetics.times(7,6))
print(arithmetics.devine(5,3))
pass