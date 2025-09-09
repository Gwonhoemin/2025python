# 함수 만들기

# 더하기 함수 정의
# 2.입력값(매개변수) => 함수를 설계한다
# 더하기를 하기 위해 두 수를 입력
def add(n1, n2): # 1.함수이름 
    # 3.결과를 만들기 위한 코드를 작성하고
    # 결과를 return 또는 print
    # => 입력받은 두수를 더하고 합계를 리턴
    return n1 + n2
# 위의 함수는 입력값 있고, 반환값도 있는 함수


# 함수 사용하기(호출하기)
# 사용 방법
# 함수이름(필요한 값 입력)
add(3,4)
# 반환값이 있으면 결과를 받고 확인해야 함
result = add(3,4)
print('두 수의 합:', result)

# 함수 만들기
# 값을 하나 입력받고 출력하기
def func(a):
    print(a)

# 함수 호출하기
func(1)

# 값을 두개 입력받고 호출하는 함수 만들기
def func2(a,b):
    print(a,b)

func2(1,2)

# 값을 세개 입력받고 호출하는 함수 만들기
def func3(a,b,c):
    print(a,b,c)

func3(1,2,3)

# 매개변수의 개수가 달라져도 사용할 수 있는 함수 만들기
# 나머지 매개변수
# 나머지 매개변수를 만들때는 **별 두개
def func(**kwargs):
    print(kwargs)

# 함수 호출
# 나머지 매개변수는 딕셔너리 형태로 저장됨
# 따라서 마음대로 데이터를 추가할 수 있음
func(a=1)
func(a=1, b=2)

# 나머지 매개변수를 사용하는 함수 만들기
# 사람의 정보를 입력받아 출력하는 함수 만들기
def info(**kwargs):
    # item 객체에서 요소를 꺼내면 tuple
    # 구조분해로 변수 두개에 key value 저장
    for key, value in kwargs.items():
        print(key, value) # ex) name 둘리

info(name="둘리", age=10) # 주소모름
# {'name': '둘리', 'age': 10} => 2개 크기의 dic 1개
info(name="도우마", age=8, address='서울')
# {'name': '도우마', 'age': 8, 'address': '서울'} => 3개 크기의 dic 1개


# 기존의 딕셔너리 함수
dic = {'name':"둘리", 'age':10}

# dict_keys => 이터러블 객체(순회 가능)
# 이터러블은 for문 사용 가능
print(dic.keys())
print(dic.values())
print(dic.items())
# items 객체의 요소는 tuple ('name', '둘리')
