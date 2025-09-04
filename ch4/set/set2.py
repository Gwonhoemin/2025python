# set의 특징
s = {1,2,3}
# set은 순서가 없다 -> 인덱스가 없다
# s[0]

# 자료구조 중에서 인덱스가 있는 것 : 리스트, 튜플
# set -> list
lis = list(s)
print(lis)
print(lis[0]) # 1
# set -> tuple
t = tuple(s)
print(t)
print(t[1]) # 2