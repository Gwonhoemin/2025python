# for문 안에서 break와 continue 쓰기

# for문에서 break 사용하기
# 1부터 20까지 합 구하기
# 합이 100을 넘으면 반복문 중단 (~하면, ~라면 => if문)
sum = 0 # 합을 저장할 변수
for i in range(1,21) :
    if sum > 100:
        break
    sum = sum + i
print('합계:', sum)



# for문에서 continue 사용하기
# continue: 건너뛰기(skip)

# for문으로 1부터 10까지 출력하세요.
# 홀수는 건너뛰고 짝수만 출력
# 꼭 continue를 사용해야 하나? -> X
for i in range(1,11):
    if i % 2 == 1:
        continue
    print(i)

# continue 사용없이 풀 때
for i in range(1,11):
    if i%2 == 0:
        print(i)