# 사람 클래스 만들기
class Person:
    def eat(self) :
        print('밥을 먹는다')
    def sleep(self):
        print('잠을 잔다')

# 학생 클래스 만들기
# 학생 클래스에도 eat과 sleep이라는 함수 추가하기!
class Student(Person):
    def study(self):
        print('학생은 공부를 한다')
# Student 클래스는 Person 클래스를 상속받아
# eat과 sleep을 물려받았음

s = Student()
s.eat()
s.sleep()
s.study()

# 또 다른 자식 클래스 만들기 ex) class Teacher(부모클래스)
class Teacher(Person):
    def teach(self):
        print('학생들을 가르친다')

# 교수 객체 생성
t = Teacher()
t.eat()
t.sleep()
t.teach()