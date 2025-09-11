# 계산기 클래스 만들기

# 클래스가 가질 수 있는 변수의 종류
# 클래스변수와 인스턴스변수(멤버변수)
# 클래스 변수 : 모든 객체의 공통 데이터
# 인스턴스 변수 : 객체 마다 고유한 데이터

# 계산기 클래스의 속성: color(색)
class Calc:
    # 클래스 변수
    type = '기본 계산기'

    # 생성자
    # 멤버변수 만드는 방법!
    def __init__(self, color):
        # 인스턴스 변수(멤버변수)
        self.calc_color = color

    # self 매개변수는 기본으로 작성할 것
    def add(self,a,b):
        print('결과:', a+b)
    def sub(self,a,b):
        print('결과:', a-b)

# 새로운 계산기 만들기
# 이전 계산기 상속받기
class NewCalc(Calc):

    # 계산기 종류(클래스 변수)
    calc_type = '공학용 계산기'

    # 곱하기 함수
    def mul(self,a,b):
        print('결과:', a*b)

    # 부모가 물려준 함수 업그레이드하기!
    # 부모가 물려준 함수가 자식과 맞지 않을때는
    # 자식에 맞게 재정의 할수 있다 => 메소드 오버라이드
    def add(self,a,b):
        print('결과:', a+b)
    


# 새로운 계산기로 객체 생성하기
new1 = NewCalc('red')
print(new1.calc_color)
print(new1.calc_type)

new2 = NewCalc('black')
print(new2.calc_color)
print(new2.calc_type)
# 계산기가 가지고 있는 기능 확인
new1.add(10,5)
new1.sub(10,5)
new1.mul(10,5)

# 클래스변수 사용하기
# 클래스이름.클래스변수
print(NewCalc.calc_type)

print("")

# Calc --------------------
# 클래스 사용하기
# 계산기 클래스로 객체 생성
calc = Calc('white') 
# 객체가 가지고 있는 함수 사용하기
# 객체변수.함수
calc.add(10,5)
calc.sub(10,5)

# 첫번째 계산기
calc1 = Calc('white')
print(calc1.calc_color)
print(calc1.type)

# 두번째 계산기
calc2 = Calc('red')
print(calc2.calc_color)
print(calc2.type)