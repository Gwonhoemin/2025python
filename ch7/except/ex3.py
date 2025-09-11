# try-except-else 구조
# else: 오류가 발생하지 않으면 실행되는 블록

# 술집에 온 사람의 나이를 확인하고 입장 여부를 판단하는 코드
try:
    # 사람의 나이 입력받기
    age = int(input()) # str -> int
except ValueError as e:
    print('사람의 나이가 정확하지 않습니다')
else:
    # 에러가 발생되지 않았으면
    # 프로그램을 이어서 작성
    # 사람의 나이가 18살 이하면 입장 불가
    if age <= 18:
        print('입장 불가!')
    else:
        print('입장 가능~')

# 잘못된 값이 들어오면 형변환 불가 ex) a
# age = int(input()) # ValueError