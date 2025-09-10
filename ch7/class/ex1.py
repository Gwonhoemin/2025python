# 학생 클래스 만들기

# 현실에 존재하는 학생이라는 객체를
# 프로그램에서 관리하기 위해 클래스를 설계하는 것

# 학생이 가지고 있는 데이터와 기능을 클래스로 표현

class Student:
    # self(매개변수)는 특별한 변수로, 함수 호출시 자동으로 생성됨
    # self에는 자기자신. 함수를 포함하고 있는 클래스가 들어감
    # self 매개변수에는 자동으로 객체가 들어감
    # 나머지 매개변수에는 함수를 통해 전달받은 입력값이 들어감
    def setdata(self, id, name, grade):  # 학번,이름,학년 저장하는 함수
        # 학생의 정보를 저장하는 함수
        self.student_id=id
        self.student_name = name
        self.student_grade = grade

    # 학생의 정보를 출력하는 함수
    def info(self):
        print(f'저는 {self.student_grade}학년 {self.student_name}입니다')

# 클래스 사용하기
stu1 = Student()
# 클래스로 객체를 생성하고
# 객체의 함수를 사용
stu1.setdata(101,'둘리',2)
stu1.info()

# 두번째 학생을 만들고 학생의 정보를 초기화
stu2 = Student()
stu2.setdata(102, '도우마', 2)
stu2.info()

# 세번째 학생을 만들고 학생의 정보를 초기화
stu3 = Student()
stu3.setdata(103,'또치',2)
stu3.info()