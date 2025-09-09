# 함수 만들기
# 두 수의 차를 구하는 함수 정의
# 매개변수: 함수에 필요한 입력값. 숫자 두개
# 반환값: 두 수의 차를 구해서 결과를 반환
def sub(n1, n2):
    return n1-n2

# 함수 호출
# 함수이름(함수에 필요한 값 입력)
result = sub(7,3)
print(result)

# 인자를 순서와 상관없이 인력
# 매개변수의 이름을 직접 지정
result = sub(n2=3, n1=7)
print(result)

# --------------------------------------

# 문자열 두개를 입력받아 연결하는 함수 정의
def add_text(str1, str2):
    # 문자열 연결 방법
    print(str1 + ' ' + str2)
    print(str1, str2)
    print(f'{str1} {str2}')

# 함수 호출
# 매개변수를 순서대로 입력(str1, str2)
add_text('hello', 'world') # hello world

# 매개변수 이름을 지정하여 입력
add_text(str2='world', str1='hello')

# -----------------------------------------------

# 함수 만들기
# 문자를 입력 받고 나쁜 말이 들어오면 종료하는 함수
def say_nick(nick): # 매개변수는 별명
    # 닉네임 검사
    if nick == "바보":
        # return 키워드를 만나면 더이상 코드를 실행하지 않고 함수가 종료됨
        # return 키워드 뒤에 값 생략 가능
        # 값이 return만 있으면 함수만 종료됨
        return # 함수 종료
    print(f'나의 별명은 {nick}입니다')

# 함수 호출
say_nick("짱구") # 나의 별명은 짱구입니다
say_nick("바보") # 나의 별명은 바보입니다 -> x

# ---------------------------------------
# 함수 만들기
def func():
    a=1
    b=2
    c=3
    # 반환값은 무조건 1개
    # return a
    # 한번에 abc를 반환하면 어떻게 될까? -> (1,2,3)
    return a,b,c

# return에 값을 여러개 쓰면 tuple로 묶어서 반환됨
print(func()) # (1,2,3) tuple

# -------------------------------------------
