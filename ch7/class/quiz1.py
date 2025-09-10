# 도시정보를 저장하기 위한 클래스 만들기
# 속성: 제목, 저자, 가격
# 기능: x
class Book:
    # 클래스에 속성을 넣는 방법
    # setdata 같은 함수 또는 생성자
    # 생성자란 객체에 필요한 값을 초기화 + 객체 생성
    def __init__(self, title, author, price):
        self.book_title = title
        self.book_author = author
        self.book_price = price

    # 책의 정보를 보여주는 함수
    def info(self):
        print(f'제목:{self.book_title} 가격:{self.book_price} 저자:{self.book_author}')

# book 클래스로 책 3권 만들기
# 객체 생성시 생성자 함수가 호출됨!
# 객체 생성시 책 정보를 입력
book1 = Book('파이썬 기초', '홍길동',10000)
book1.info()

book2 = Book('자료구조', '김철수',20000)
book2.info()

book3 = Book('알고리즘', '이영희',30000)
book3.info()

# 같은 클래스로 만든 객체를
# 같은 구조로 만들어졌지만, 각자 다른 데이터를 가지고 있다

# 클래스는 언제 사용할까?
# 구조는 같지만, 각자 고유한 데이터를 가지고 있는
