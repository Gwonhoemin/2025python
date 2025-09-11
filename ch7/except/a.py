# try-finally 구조
# finally는 오류와 상관없이 항상 실행됨
# f를 try와 finally 모두 사용하기 위해서
# f를 전역변수로 선언
# 전역변수란? 제일 밖에서 선언되어 모든 곳에서 사용할 수 있는..
# 변수 만들기 = 변수 선언
f = None
try:
    # f가 선언된 곳
    # f는 try 안에서 만 사용가능한 지역 변수
    f=open('test.txt','r') # 왜냐? 'text.txt'파일은 없기 때문에 FileNotFound error 발생
except FileNotFoundError as e:
    print(e)
finally:
    # 에러 발생 여부와 상관없이 항상 실행되야 하는 코드
    # f는 try를 벗어나면 사용할 수 없다
    if f == None:
        print('파일이 없습니다')
    else:
        print('파일을 닫았습니다')
        f.close()
