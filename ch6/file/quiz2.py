# 시험 점수를 입력받아 합격여부를 출력
scores = input('시험 점수 입력:')
scores = int(scores)

if scores >=60:
    print("합격")
else :
    print("불합격")

# 학생의 나이를 입력받아 버스 요금 계산
age = input('나이 입력:')
age = int(age)

if age <= 12 :
    print('1000원')
elif age <=18 :
    print('1500원')
else :
    print('2000원')

# 문자를 계속 입력 받다가 0이 들어오면 종료
# ex) 'aaa' -> 계속
# ex) 'bb' -> 계속
# ex) '11' -> 계속
# ex) '0' -> 종료

# 반복문 for while
# for : list tuple range 등 데이터 개수만큼 반복 -> 반복횟수가 명확
# while: 조건이 참인 동안 반복 -> 반복횟수가 모호

# 조건을 잘모르겠을때 : 조건식을 True로 표현
while True:
    text = input('값을 입력하세요:')
    if text == '0':
        break



# 내가 작성한 코드 for문으로는 작성 불가
# lis = []
# num = input('문자를 입력하시오:')
# num = int(num)
# lis.append(num)

# for i in lis:
#     if i == 0:
#         break
#     print("계속")
#     input('문자를 입력하시오')