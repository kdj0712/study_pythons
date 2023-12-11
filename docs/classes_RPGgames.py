# function만 사용해 적 캐릭 만들기
# first 적 캐
name_first = "first"
health_first = 120
damage_first = 0

def attack(health, damage) :
    health = health - damage
    return health

# damage_first = attack(5)

# second 적 캐릭
name_second = "second"
health_second = 200
damage_second = 0

# damage_second = attack(10)
# 제한 극복 => Class 사용하지 않는 한 

class Enemy:
    def __init__(self, name, health,) :
        self.name = name    # 외부 변수 지정값이 내부변수 self.name에 할당
        self.health = health
        self.damage = 0
        pass

    def attack(self, damage) :
        self.health = self.health - damage
        return self.health
    def name():
        
        return
    def health():

        return
    def damage():

        return
# first_enemy = Enemy('first',150) #자신의 내재된 자원(function 과 variables)을 확인    
first_enemy = Enemy('first',150) #자신의 내재된 자원(function 과 variables)을 확인
second_enemy = Enemy('second',300)
  
pass