# 상속문제

# Animal 클래스
class Animal:
    def eat(self):
        print('동물이 먹습니다')

# Dog 클래스, Animal클래스 상속받으세요
class Dog(Animal):
    def bark(self):
        print('강아지가 짓습니다.')

# Dog 객체 만들고 모든 기능 실행
d1 = Dog()
d1.eat()
d1.bark()

# ------------
# Book 클래스
class Book:
    def read(self):
        print('책을 읽습니다.')

# EBook class
class EBook(Book):
    def download(self):
        print('전차책을 다운로드합니다.')

ebook = EBook()
ebook.read()
ebook.download()

# ---------------
# Monster class
class Monster:
    def attack(self):
        print('몬스터가 기본 공격을 합니다!')

class Slime(Monster):
    def jump_attack(self):
        print('슬라임이 점프해서 몸통 박치기를 합니다!')

slime1 = Slime()
slime1.attack()
slime1.jump_attack()