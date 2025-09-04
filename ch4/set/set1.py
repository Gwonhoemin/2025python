# set 만들기

s1 = {1,2,3}
print(s1, type(s1))
s2 = {} # 빈 셋
print(s2, type(s2)) # type->'dict'

# 형변환
# list -> set
s3 = set([1,2,3])
print(s3)
# string -> set
# 문자열의 문자들이 쪼개져서 set으로 저장됨
# set은 순서가 없다
s4 = set('string')
print(s4)
# set은 중복 불가
s5 = set('hello')
print(s5)