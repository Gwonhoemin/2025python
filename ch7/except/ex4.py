# raise : 에러를 강제적으로 발생시키는
# 함수 오버라이드를 강제할때 사용하는 코드

# 먼저 클래스 만들기
class Bird:
    def fly(self):
        # 이 코드는 자식 클래스에서 함수를 사용하지 못하게 할때 사용
        # NotImplementedError 에러를 강제로 발생시키기!
        raise NotImplementedError

# Bird를 상속받는 자식 클래스 만들기
class Eagle(Bird):
    # 자식은 물려받은 함수를 쓰려면
    # 무조건 재정의를 해야함!
    def fly(self):
        print('fly~~~~')

# 일단 객체를 만들고 물려받은 함수 쓰기
eagle = Eagle()
eagle.fly()