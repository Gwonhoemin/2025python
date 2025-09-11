# 예외 처리: 오류가 발생해도 프로그램이 멈추지 않고 계속 실행할 수 있도록 처리하는 것

# try 블록 안에서 오류가 발생하면 except 블록이 실행됨
# 오류가 발생하지 않으면 except 블록 실행 안됨
try:
    # 에러가 발생할 수 있는 코드
    4/0
# 실제로 발생하는 에러의 종류 as 변수
except ZeroDivisionError as e:
    # 에러가 났을 때 처리할 코드
    print(e)

# try:
#     # 에러가 발생할 수 있는 코드
#     4/0
# # 에러타입이 맞지 않으면 에러
# except IndexError as e:
#     # 에러가 났을 때 처리할 코드
#     print(e)

# 확인용 코드
print('프로그램이 정상적으로 종료되었습니다')

lis=[1,2,3]
try:
    lis[3]
except IndexError as e:
    print(e)