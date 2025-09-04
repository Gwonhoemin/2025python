# 형변환
# 자료형을 다른 자료형으로 바꾸는 것

# list -> tuple
t1 = tuple([1,2,3])
print(t1)
# 정확한 자료형 확인
print(type(t1))

# string -> tuple
# 문자열의 문자가 하나씩
t2 = tuple('string')
print(t2)

# 반대로 튜플을 리스트로 변환 가능
t = (1,2,3)
print(list(t)) #[1,2,3]