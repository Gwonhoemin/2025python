# 학생 클래스 만들기
class Student:
    # 생성자
    # self는 특별한 매개변수로 함수가 호출될때 자동으로 객체가 들어옴
    # 나머지 매개변수만 입력하면 됨
    def __init__(self, id, name, grade):
        # 학생의 정보를 저장
        # 학생의 멤버변수 = 새로운값
        self.stu_id = id
        self.stu_name = name
        self.stu_grade = grade

    
    def info(self): # 학생의 정보를 출력하는 함수
        print(f'학번:{self.stu_id} 이름:{self.stu_name}')

# 클래스로 객체 생성
# 객체를 생성할때 생성자(__init__)가 호출됨
# 학생의 정보가 없으면 생성이 안됨 => stu1=Student()
# 학생데이터를 강제로 입력시킬때 생성자를 이용
stu1 = Student(101, '둘리', 2)
stu1.info()

# 객체 생성시 무조건 학생의 정보를 입력
stu2 = Student(102,'도우너',2)
# 학생의 정보를 하나씩 출력
print(stu2.stu_id)
print(stu2.stu_name)
print(stu2.stu_grade)
stu2.info()

