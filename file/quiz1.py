# 두 숫자를 입력받아 곱셈 결과를 출력
n1 = input('첫번째 수를 입력:')
n2 = input('두번째 수를 입력:')
mul = int(n1)*int(n2)
print('결과:', mul)

# 사용자로부터 이름과 나이를 입력받아 자기소개 출력
# ex) 둘리, 7 => "둘리님의 나이는 7세입니다"
name = input('이름 입력:')
age = input('나이입력 :')
say = (f'{name}의 나이는 {age}세입니다')
print('결과:',say)

# 사과 가격과 수량을 입력 받아 총 가격 계산
# ex) 사과가격:1500, 사과개수:5 => 7500원
price = input('가격입력:')
count = input('수량입력:')
total = int(price)*int(count)
print(f'총 가격: {total}원')
