# 변수 n을 선언하고 숫자를 대입하세요
# n의 크기만큼 *별을 출력하세요
# ex) n=5 => *****
# ex) n=3 => ***

num=5
# 문자열 반복 연산 사용
print('*'*num) # *****

# for문 사용
str1 = '' # 결과를 저장할 변수
for _ in range(num):
    str1 = str1 + '*'
print(str1)


# 변수 n을 선언하고 숫자를 대입
# n의 크기만큼 삼각형 그리기
# n=5
# *
# **
# ***
# ****
# *****
n = 5
for a in range(n+1) :
    print('*'* a)


n=5
for a in range(n+1): # 0~5  #5
    print((n-a)*' ' + '*'*a )

# 구구단 중에서 3단을 출력하세요
n = 3
m = range(1,10)

for a in m :
    print( n , 'x', a , '=' ,(n * a))

# 리스트 생성
nums = [5,9,3,8,2]
max = nums[0] #가장 큰값을 저장할 변수
# 리스트에서 가장 큰 값 구하기 => 9
for n in nums:
    if max > n:
        print(max)
    max = n

# 리스트 생성 *
nums = [5,9,3,8,2]
max = nums[0] #가장 큰값을 저장할 변수
# 리스트에서 가장 큰 값 구하기 => 9
for n in nums:
    # 현재 max와 리스트의 요소를 비교하여
    # 리스트의 요소가 더 크면 max를 교체
    if max < n:
        max = n # 교체
print('최대값:', max)
