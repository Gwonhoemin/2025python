# 조건문 만들기

age = 16

# if
# 조건을 만족할 때만 수행

# if age>=8 :
#     print("학교에 다닙니다")

# if~else
# 조건을 만족하면 첫번째 블록을 수행
# 만족하지 않으면 두번째 블록을 수행

# if age>=8 :
#     print("학교에 다닙니다")
# else:
#     print("학교에 다니지 않습니다")

# if~elif~else
# 조건이 여러개 일때, 앞에 있는 조건식이 참이면
# 뒤에 있는 조건식은 판단하지 않는다

if age<8:
    print("아동입니다")
elif age < 14:
    print("초등학생입니다")
elif age < 20:
    print("중고등학생입니다")
else:
    print("성인입니다")


