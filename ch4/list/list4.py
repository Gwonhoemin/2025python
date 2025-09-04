# 리스트의 CRUD 함수
# 데이터 추가, 조회, 수정, 삭제

lis = [1,2,3]

# append : 새로운 요소를 맨 뒤에 추가
lis.append(4)
print(lis)

# 특정 위치에 새로운 요소를 추가
# 입력값: 위치, 값
lis.insert(0, 4) # 0번 자리에 4추가
print(lis) #[4,1,2,3,4]

# 값 수정하기
lis[2] = 4 # 세번째 숫자를 4로 변경
print(lis) #[4,1,4,3,4]

# 인덱스로 삭제하기
del lis[1]
print(lis) # [4,4,3,4]

# 값으로 삭제하기
# 같은 값이 여러개 있을때는,
# 제일 앞에 있는 요소가 삭제됨!
lis.remove(4)
print(lis) # [4,3,4]

# 마지막 요소를 꺼내면서 삭제
last = lis.pop()
print(lis, last)

# 리스트의 크기 확인
leng = len(lis)
print(leng) #2