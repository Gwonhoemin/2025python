# Animal 클래스
class Animal:
    def bark(self):
        print('동물이 소리를 낸다')

# 부모한테 물려받은 함수를
# 자식클래스에 맞게 고치기!
class Dog(Animal):
    def bark(self):
        print('멍멍')

# Dog 객체 만들고 모든 기능 실행
dog = Dog()
dog.bark()

# 고양이 클래스 만들기
class Cat(Animal):
    def bark(self):
        print('야옹~')

cat = Cat()
cat.bark()