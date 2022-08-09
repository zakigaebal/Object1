# 연습문제 2.12.1
# 삼각형의 넓이를 계산하기 위한 클래스를 만든다
# 이 클래스는 다음과 같은 속성을 가진다.
# 밑변의 길이 b와 높이 h
# 삼각형의 넓이를 계산하는 메서드 area

class 삼각형(object):
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        return int(self.b*self.h*0.5)

# 삼각형1=삼각형(8,8)
# 삼각형1.area()
# print(삼각형1.area())

# 연습문제2.12.2
#사각 기둥의 부피를 계산하기 위한 클래스를 만든다. 이 클래스는 다음과 같은 속성을 가진다.
#밑면의 가로 길이 a, 밑면의 세로 길이 b, 높이 h
#부피를 계산하는 메서드 volume
#겉넓이를 계산하는 메서드 surface
class 사각기둥(object):
    def __init__(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h
    def volume(self):
        return self.a*self.b*self.h
    def surface(self):
        return self.a*self.b

# 사각기둥1=사각기둥(2,2,2)
# v=사각기둥1.volume()
# s=사각기둥1.surface()
# print(v)
# print(s)

# 연습문제2.12.3
# 게임 캐릭터 코드에서 attacked 메서드도 
# 오버라이딩을 하여 
# 전사와 마법사가 공격을 받을 때 
# life 속성값이 다르게 감소하도록 한다.
# 먼저 부모클래스 Character부터 만들자
class Character(object):
    def __init__(self):
        self.life = 1000
        self.strength = 10
        self.intelligence = 10
    def attacked(self):
        self.life -= 10
        print(f"공격당함! 생명력 = {self.life}")
    def attack(self):
        print("공격!")

class Warrior(Character):
    def __init__(self):
        super(Warrior,self).__init__()
        self.strength = 15
        self.intelligence =5
    def attack(self):
        print("육탄 공격!")
    def attacked(self):
        self.life -= 110
        print(f"전사공격당함! 생명력 = {self.life}")
        

class Wizard(Character):
    def __init__(self):
        super(Wizard,self).__init__()
        self.strength = 5
        self.intelligence = 15
    def attack(self):
        print("마법공격")
    def attacked(self):
        self.life -= 310
        print(f"마법사공격당함! 생명력 = {self.life}")


# 캐릭터 = Character()
# 전사 = Warrior()
# 마법사 = Wizard()

# 캐릭터.attack()
# 전사.attack()
# 마법사.attack()

# 캐릭터.attacked()
# 전사.attacked()
# 마법사.attacked()


# 다음과 같이 자동차를 나타내는 Car 클래스를 구현한다.
# 이 클래스는 최고 속도를 의미하는 max_speed라는 속성과 현재 속도를 나타내는 speed라는 속성을 가진다.
# 객체 생성시 max_speed 속성은 160이 되고 speed 속성은 0이 된다.
# speed_up, speed_down이라는 메서드를 가진다. speed_up을 호출하면 speed 속성이 20씩 증가하고 speed_down을 호출하면 speed 속성이 20씩 감소한다.
# 스피드 속성 speed의 값은 max_speed 속성 값, 즉 160을 넘을 수 없다. 또 0 미만으로 감소할 수도 없다.
# 메서드는 호출시 속도 정보를 출력하고 명시적인 반환값을 가지지 않는다.
# 위 기능이 모두 정상적으로 구현되었음을 보이는 코드를 추가한다.


class Car(object):
    def __init__(self):
        self.max_speed = 160
        self.speed = 0

    def speed_up(self):
        if(self.speed >= self.max_speed):
            print(self.speed)
        else:
            self.speed += 20
            print(self.speed)
    def speed_down(self):
        if(self.speed <= 0):
            print(self.speed)
        else:
            self.speed -= 20
            print(self.speed)

# 자동차1 = Car()
# 자동차1.speed_up()
# 자동차1.speed_up()
# 자동차1.speed_up()
# 자동차1.speed_up()
# 자동차1.speed_up()
# 자동차1.speed_up()
# 자동차1.speed_up()
# 자동차1.speed_up()
# 자동차1.speed_up()
# 자동차1.speed_up()

# 자동차1.speed_down()
# 자동차1.speed_down()
# 자동차1.speed_down()
# 자동차1.speed_down()
# 자동차1.speed_down()
# 자동차1.speed_down()
# 자동차1.speed_down()
# 자동차1.speed_down()
# 자동차1.speed_down()
# 자동차1.speed_down()


# 연습 문제 2.12.5
# Car 클래스를 기반으로 SportCar와 Truck이라는 두 개의 자식 클래스를 구현한다.
# SportCar 클래스는 max_speed 속성이 200 이고 speed_up, speed_down 호출시 속도가 45씩 증가 혹은 감소한다.
# Truck 클래스는 max_speed 속성이 100 이고 speed_up, speed_down 호출시 속도가 15씩 증가 혹은 감소한다.
# 스피드 속성 speed의 값은 max_speed 속성 값을 넘을 수 없다. 또 0 미만으로 감소할 수도 없다.
# 메서드는 호출시 속도 정보를 출력하고 명시적인 반환값을 가지지 않는다.
# 위 기능이 모두 정상적으로 구현되었음을 보이는 코드를 추가한다.

class SportsCar(Car):
    def __init__(self):
        super(SportsCar,self).__init__()
        self.max_speed = 200
    def speed_up(self):
        if(self.speed <= self.max_speed-45):
            self.speed +=45
            print(self.speed)
        else:
            print(self.speed)
    def speed_down(self):
        if(self.speed >=45):
            self.speed -= 45
            print(self.speed)
        else:
            print("최저속도0")


스포츠카 = SportsCar()

스포츠카.speed_up()
스포츠카.speed_up()
스포츠카.speed_up()
스포츠카.speed_up()
스포츠카.speed_up()
스포츠카.speed_down()
스포츠카.speed_down()
스포츠카.speed_down()
스포츠카.speed_down()
스포츠카.speed_down()
스포츠카.speed_down()