# 반복문으로 숫자3개 입력하고 합구하기

# sum = 0
# for _ in range(3):
#     num = input()
# sum = sum + int(num)
# print('합계:', sum)


# 퀴즈
# 다음과 같이 리스트를 만들고
# for문으로 요소를 하나씩 출력하세요
mixed = [1,"apple",3.14,True]

# for 변수 in 자료구조(list tuple dic iter)
for m in mixed:
    print(m)

# 다음과 같이 리스트를 만들고
# for문으로 요소를 하나씩 출력
fruits = ["apple", "banana", "cherry"]
for n in fruits:
    print(n)

# key값 꺼내기
students = {"이름":"둘리", "나이":20, "주소":"인천"}
for n in students:
    print(n)

# value값 꺼내기
coffee_menu = {"아메리카노":"2500원", "라떼":"3000원", "케이크":"4500원"}
for value in coffee_menu.values():
    print(value)

# for문으로 11부터20까지 출력
# range(개수) 또는 range(시작,끝)
num1 = range(11,21)
for n in num1:
    print(n)

# for문으로 5부터15까지 출력
num2 = range(5,16)
for n in num2:
    print(n)

# for문으로 "hi" 5번 출력
num3 = range(5)
for _ in num3:
    print('hi')

# for문으로 nums의 모든 요소 더해서 합구하기
nums = [10,20,30,40,50]
sum = 0
for n in nums:
    sum = sum + n
print('합계:', sum)

# for문을 사용해서
# 1부터 100까지 숫자 중에서 3의 배수만 구하세요
nums = range(1,101)
print(nums)
for n in nums:
    if n % 3 == 0:
        print(n)

# for문을 사용해서
# 1부터 100까지 숫자 중에서 3의 배수의 합계 구하세요
nums = range(1,101)
sum = 0
print(nums)
for n in nums:
    if n % 3 == 0:
        sum = sum + n
print(sum)
