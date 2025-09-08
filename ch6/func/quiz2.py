# 숫자를 입력받아 양수/음수/0을 판별하는 함수
# ex) 5->"양수"
# ex) -3 -> "음수"
# ex) 0 -> "0입니다"
def func(num):
    if num > 0:
        print("양수")
    elif num < 0:
        print("음수")
    else :
        print("0입니다")

func(5)
func(-3)
func(0)

# 리스트를 입력받아 리스트 안의 숫자를 모두 더해
# 합을 반환하는 함수
# ex) [1,2,3,4,5] -> 15
# ex) [10,20,30] -> 60

# 함수 정의
# 함수이름, 입력값, 반환값
# 매개변수(입력값)의 이름은 자유롭게, 개수는 문제에 맞게
def func(lis) : # lis => 매개변수
    sum = 0
    for i in lis:
        sum = sum + i
    return sum

# 반환값이 있으면 결과를 받고 출력!
lis1 = [1,2,3,4,5]
print(func(lis1))

lis2 = [10,20,30]
print(func(lis2))

# 단을 입력 받아 구구단을 출력하는 함수
# ex) 3단
# 내가 작성한 코드
def func(num):
    for i in range(1,10):
        print(num, 'x', i, '=', num * i)
func(4)

# 풀이
def func(dan) :
    for n in range(1,10):
        print(f'{dan} x {n} = {dan*n}')
func(9)
# 2단부터 9단까지 출력
func(2)
func(3)
func(4)
func(5)
func(6)
func(7)
func(8)
func(9)

# 리스트를 입력받아 그 안에
# 문자열(str) 자료형이 몇 개인지 세는 함수를 만드세요
# ex) [1, "apple", 3.5, "banana", 10, "hi"] -> 3

# 풀이
  # type(item) == str => 자료형은 ''문자열처리x / 예약어로 작성
        # 각 요소가 문자인지 확인
        # print(item, type(item))
        # 조건: if
        # 요소의 타입 == str
def func(lis):
    # 리스트 안에 있는 요소 하나씩 꺼내서 item 변수에 담기
    sum = 0
    for item in lis:
        if type(item) == str :
            print(item, ':문자')

 

# 함수 호출
func([1, "apple", 3.5, "banana", 10, "hi"])
func(["a","b","c"])
func([1,2,3])