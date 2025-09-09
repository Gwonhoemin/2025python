# 문자열 정렬
strings = ['foo','card','ba','aaa']

# sort : 목록을 순차적으로 정렬하는 함수
# ex) 1 2 3 4 5 / 5 4 3 2 1
# 문자를 정렬할때는 람다 함수 필요

# sort 함수의 입력값으로 함수 입력
# 문자의 크기를 비교하는 함수
# 변수 = lambda 매개변수 반환값
result = strings.sort(key=lambda x : len(x))

print(result) # None

