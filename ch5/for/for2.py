# 0부터 9까지 숫자 10개가 반환됨
# range : 연속된 숫자를 만들어주는 함수
# 반환값 : 숫자를 담고 있는 range 객체
nums = range(10) # 개수
print(nums)
# 사용방법
for n in nums:
    print(n)

# 0부터 10까지 숫자 10개 반환
nums = range(0,11) # 마지막 숫자는 포함x
print(nums)

for n in nums:
    print(n)

# 10부터 20까지 연속된 숫자들을 반환
nums = range(10, 21) # 시작,끝
print(nums)

for n in nums:
    print(n)

# 0부터 9까지 연속된 숫자 10개 반환
nums = range(10)
# range객체를 사용해 "안녕하세요" 10번 출력
# range 값이 필요하지 않는 경우 => _(언더바) 사용
for _ in nums:
    print("안녕하세요")

# input 키보드를 통해 값을 입력받는 함수
# num = input() # 사용자가 값을 입력할때까지 대기
# print('입력받은 값:', num)


# 숫자를 3개 입력받고 합 구하기 -> a.py
sum = 0 # 합을 저장할 변수
num1 = input()
num2 = input()
num3 = input()
# str -> int
sum = int(num1) + int(num2) + int(num3)
print('합계:', sum)

# 숫자 입력받고 sum에 더하기 -> a.py
sum = 0
num1 = input()
sum = sum + int(num1)

num2 = input()
sum = sum + int(num2)

num3 = input()
sum = sum + int(num3)
