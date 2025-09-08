# 값을 하나 입력 받아 타입이 str이면
# "문자입니다"를 출력하는 함수
# 타입이 str이 아니면 아무것도 출력되지 않습니다
msg = input('값을 입력하세요:')
def func(msg):
    if isinstance(msg, str):
        print("문자입니다")
    else:
        print("")
func(msg)

# 값을 하나 입력 받아 0보다 크면
# "양수입니다"를 출력하는 함수
# ex) 10 -> "양수"
# ex) -5 -> x
a = int(input('값을 입력하세요:'))
def func(a):
    if a > 0:
        print("양수입니다")
    else :
        print("")
func(a)

print("")
# ----------------------------------
# 리스트를 입력받아 첫 번째 값을 반환하는 함수 (내가 작성함)
# ex) [10,20,30] -> 10
# ex)["a","b","c"] -> "a"
a = input('리스트를 입력하시오: ')
b = input('리스트를 입력하시오: ')
c = input('리스트를 입력하시오: ')
lis = []
def func(a,b,c):
    for i in a,b,c:
        lis.append(i)
    print(lis[0])
func(a,b,c)

print("")
# 리스트를 입력받아 첫번째 값을 반환하는 함수 (강의 풀이)
def func(lis): # lis : 함수의 매개변수로, 함수 내부에 선언됨
    return lis[0]

# my_lis : 함수에 전달하기 위한 리스트로, 메인에 선언됨
my_lis = [10,20,30]
# result : 함수의 결과를 저장하기 위한 변수로, 메인에 선언됨
result = func(my_lis)
print(result)

print("")

# ------------------------------------
# 문자열을 입력받아 길이를 반환하는 함수 (내가 작성함)
# ex) 'abc' -> 3
# ex) 'hello' -> 5
n = input('문자열을 입력:')
def func(n):
    print(len(n))
func(n)

# 문자열을 입력받아 길이를 반환하는 함수 (강의 풀이)
def func(msg):
    return len(msg)

# my_str1 : func 함수를 호출할때 입력할 문자열
my_str1 = "abc"
my_str2 = "hello"

# result1 : func함수의 결과. "abc"의 길이를 저장할 변수
result1 = func(my_str1) 
result2 = func(my_str2)
print(result1)