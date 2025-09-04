# 리스트 관련 함수

lis = [1,4,3,2]

# 값 정렬하기(기본값:오름차순)
# sort함수는 원본데이터를 변경한다
lis.sort()
print(lis) # 1,2,3,4

# 뒤집기 reverse()
lis2 = ['a','c','b']
lis2.reverse()
print(lis2) # b,c,a

# 값으로 위치(인덱스) 찾기
lis3 = ['a','b','c']
# 입력값: 값
# 반환값: 인덱스
# 'a'의 위치 찾기
index = lis3.index('a')
print(index)

# 리스트 안에 포함된 값의 개수 세기
lis4 = [1,2,3,1]
# 1의 개수 세기
# 입력값: value
# 반환값: count
cnt = lis4.count(1)
print(cnt) #2

