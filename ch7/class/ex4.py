# 학생 클래스 만들기

class Student:
    school = '연희직업학교'

    def __init__(self, id, name):
        self.student_id = id
        self.student_name = name
    
    def info(self):
        print(f'이름: {self.student_id} 학교: {self.school}')

# 학생 2명 만들기
# 객체 생성시 무조건 학생의 정보를 입력해야함!
# 모든 학생의 공통 데이터 : 학교
s1 = Student(101, '둘리')
s1.info()
s2 = Student(102, '도우너')
s2.info()
# 이름: [...] 학교: 연희직업학교

# 멤버변수로 school을 넣었을때 ->
# 모든 객체가 똑같은 데이터를 가짐 -> 메모리 낭비

# 클래스변수로 school을 넣었을때 ->
# 메모리에 딱 한번만 '연희직업학교'가 저장되고
# 모든 객체가 클래스 변수를 공유함

# 정리:
# 클래스 변수 - 모든 객체가 공유하는 데이터
# 인스턴스 변수 - 객체 고유의 데이터

# 클래스 변수 값 변경하기
Student.school='귀살대'
s1.info()
s2.info()