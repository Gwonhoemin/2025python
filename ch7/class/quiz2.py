# 자동차 클래스를 만들어주세요
# 속성: 모델명, 색상

# 자동차 객체를 2대 만들고 정보를 출력하세요
# 실행결과)
# 소나타 흰색
# 아반떼 검정

class Car:
    # 함수의 매개변수와 클래스의 멤버변수는
    # 이름이 같아도 될까? O
    def __init__(self, model, color):
        self.car_model = model
        self.car_color = color
    def info(self):
        print(f'{self.car_model} {self.car_color}')

car1 = Car('소나타','흰색')
car2 = Car('아반떼', '검정')
car1.info()
car2.info()


# Order 클래스를 만들어주세요
# 속성: 주문번호, 상품명, 수량
# 기능: 주문번호와 상품명 출력
# Order 클래스로 객체를 2개 만들고 출력
# 실행결과)
# 101 노트북 3
# 102 마우스 5
class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
    def info(self):
        print(f'{self.order_id} {self.product} {self.quantity}')

order1 = Order(101, '노트북',3)
order2 = Order(102, '마우스',5)
order1.info()
order2.info()

# -----------------------------------
# 카페에서 커피를 주문하는 프로그램 작성하기

# 커피 클래스 만들기
# 속성: 커피명(예: 아메리카노, 라떼)

class Coffee:
    # 생성자: 객체 생성+데이터 초기화
    def __init__(self, name):
        self.coffee_name = name # 멤버변수=새로운값
        self.cnt = 0
    # 커피를 주문하는 함수
    # 매개변수: 주문수량
    def order(self, num):
        # 누적건수 계산하기!
        self.cnt = self.cnt + num
        print(f'{self.coffee_name}를 {num}잔 추가 주문했습니다')
        print(f'총 {self.cnt}잔')
# Coffee 클래스로 아메리카노와 라떼 생성
c1 = Coffee('아메리카노')
c2 = Coffee('라떼')
# 커피 주문하기!
c1.order(2)
c1.order(3)
c2.order(1)
c2.order(2)

# --------------------------------------------

# Bus 클래스를 만들어주세요
# 속성: 노선번호, 누적 승객수
# 같은 버스에 승객을 여러번 태우면 누적 인원수가 계산됩니다

# 실행결과)
# 9번 버스에 승객 10명이 탑승했습니다. (총10명)
# 9번 버스에 승객 5명이 탑승했습니다. (총 15명)
# 111번 버스에 승객 3명이 탑승했습니다. (총 3명)
# 111번 버스에 승객 6명이 탑승했습니다. (총 9명)

class Bus:
    def __init__(self, line):
        self.line = line
        self.cnt = 0
    def ride(self, people):
        self.cnt = self.cnt + people
        print(f'{self.line}번 버스에 승객 {people}명이 탑승했습니다.')
        print(f'(총 {self.cnt}명)')

b1 = Bus(9)
b2 = Bus(111)
b1.ride(10)
b1.ride(5)
b2.ride(3)
b2.ride(6)

# -----------------------------------------
class Subway:
    def __init__(self, line, fare=1500):
        self.line = line
        self.passengers = 0
        self.fare = fare
        self.total_fare = 0

    def take(self, num):
        self.passengers = self.passengers + num
        # 누적 요금 계산하기
        self.total_fare = self.total_fare + (self.fare*num)
        print(f'{self.line}호선에 승객 {num}명이 탑승했습니다.')
        print(f'총 {self.passengers}명, 요금 {self.total_fare}')
    
s2 = Subway(2)
s9 = Subway(9)

s2.take(5)
s2.take(3)
s9.take(10)
s9.take(4)

# -----------------------------------------------
# Account (예금) 클래스를 만들어주세요
# 속성: 잔액
# 기능: 입금하기 / 출금하기
# 단, 출금시 예금이 부족하면 "잔액이 부족합니다"를 출력하세요.

class Account:
    def __init__(self):
        self.total_balance = 0

    def deposit(self, money):
        self.money = money
        self.total_balance = self.total_balance + self.money
        print(f'{self.money}원 입금완료. 현재 잔액 {self.total_balance}')

    def withdraw(self, money):
        self.money = money
        self.total_balance = self.total_balance-self.money
        if self.total_balance < money :
            print('잔액이 부족합니다.')
        else : 
            print(f'{self.money}원 출금완료. 현재 잔액 {self.total_balance}')
        

user1 = Account()
user1.deposit(10000)
user1.withdraw(3000)
user1.withdraw(8000)