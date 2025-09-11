# 파이썬의 함수
# 모듈을 불러와서 사용해야 하는 것: math.floor 등
# 모듈을 불러오지 않고 바로 사용 가능한 것: print 등

# len: 자료구조의 길이를 구하는 함수
print(len('python'))
print(len([1,2,3]))
print(len((1, 'a')))

# max: 제일 큰 값 구하기
print(max([1,5,3,4]))
print(max(4,2,1))

# min: 제일 작은 값 구하기
print(min([1,5,3,4]))

# round : 반올림 0.5 이상이면 -> 1
print(round(4.6))
print(round(4.2))
print(round(5.578,2))

# sort: 리스트를 순차적으로 정렬
print(sorted([3,1,2]))
print(sorted(['a','c','b']))

# reversed: 역순으로 정렬
print(list(reversed([3,1,2]))) # object -> list

# sum : 합계
print(sum([1,2,3]))

# type: 자료형 확인
print(type(123))
print(type('abc'))
print(type([1,2,3]))

# abs: 절대값 구하기
print(abs(-3))
print(abs(-1.2))

# enumerate : 리스트에 인덱스 붙이기
for i, value in enumerate(['a','b','c']):
    print(i, value)

# zip : 튜플 묶기. 위치를 기반으로 조합
t1 = ('a','b','c')
t2 = ('c','d','e')
print(list(zip(t1, t2))) # object -> list

# -------------
# 날짜와 시간

# 모듈 불러오기
from datetime import datetime, date, time

# 시간 생성하기
# 연도,월,일,시,분,초
dt = datetime(2025,9,11,12,38,00)
print(dt)

# 날짜와 시간 꺼내기
print(dt.day)
print(dt.minute)

# 언제 활용할까?
# 상품의 주문시간을 저장
# 사용자가 업로드한 파일을 날짜별로 저장

# 날짜와 시간으로 분리
print(dt.date())
print(dt.time())

# 문자열 -> 시간 객체로 변환
date_str = '20250911'
# 문자열, 포맷
# 포맷은 왜 필요할까?
# 날짜 - 연도, 월, 일, 시, 분, 초
print(datetime.strptime(date_str, '%Y%m%d'))