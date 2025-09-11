# math 모듈 가져오기
# math란? 파이썬에서 제공하는 기능 중 하나로
# 수학 함수를 가지고 있음(abs, sum 등)
# import math
from math import ceil, floor

# math 모듈의 ceil과 floor 함수 사용하기
# ceil: 올림
# floor: 내림
# print(math.ceil(3.14))
# print(math.floor(3.14))

# 함수 이름 그대로 사용가능
ceil(3.14)
floor(3.14)

# -----------------------------------
# random 모듈을 가져와서 randint(시작,끝) 함수로
# 1~6 사이의 랜덤 숫자를 6개를 뽑아보세요
from random import randint
i=0
while i<6 :
    print(randint(1,6))
    i+=1

print("")

for _ in range(6):
    n = randint(1,6)
    print('1~6 중에 랜덤한 값:',n)

# -----------------------------------
from time import sleep
sleep(2)
print("끝!")

# -----------------------------------
from os import getcwd
print(getcwd())