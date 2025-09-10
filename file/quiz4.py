# Q1. score.txt 파일을 읽고
# 합계와 평균을 구하시오.
f = open('score.txt', 'r')

text = f.read()
print(text)
f.close()

# 점수를 하나씩 꺼내기!
# list->for str->split
# 문자열을 쪼개기 위한 구분자를 선택
lis = text.split(' ')
print(lis)

# 총점 구하기
sum = 0
for n in lis:
    sum=sum+int(n)

print('총점:',sum)

# 평균 구하기
cnt = len(lis)
print('평균:', sum/cnt)

# Q2. nubmers.txt 파일을 읽고
# 짝수만 출력하세요

f = open('numbers.txt','r')
lis=f.readlines()
print(lis)
f.close()

for line in lis:
    if int(line)%2 == 0:
        print(line, end = '')

f.close()

# -------------------------
# 파일을 쓰기 모드로 열기
f = open('new.txt', 'w')
f.write('hello world')
f.close()

# 위 코드를 간단하게 작성하기
# with를 사용하면 마지막에 자동으로 close가 실행됨
with open('new.txt', 'w') as f:
    # 블록에는 수행하고 싶은 코드 작성
    f.write('hello wolrd')
