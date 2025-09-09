# 키보드로 값 입력받기

a = input() # 사용자가 입력할때까지 대가
print('입력받은 값:',a)

# 숫자 두개 입력받기
n1 = input('첫번째 숫자를 입력하세요: ')
n2 = input('두번째 숫자를 입력하세요: ')
# 두 수의 합 구하기
# 먼저 형변환을 하고 더하기 str->int
sum = int(n1) + int(n2)
print('결과: ', sum)

# n1 n2 자료형 확인
print(type(n1), type(n2))

