# 반대로 파일의 내용을 읽어오기

# 읽기모드로 파일 열기
# 파일이름, 모드
f = open('새파일.txt','r')

# 파일의 내용 읽어오기
# 읽기 함수들 중에서
# readlines는 결과를 리스트로 반환 -> 결과는 리스트로 저장됨
# read는 파일의 내용을 문자열 하나로 반환

# lines = f.readlines()
# print(lines)
text = f.read()
print(text)

# 문자열 안에 있는 알파벳을 하나씩 꺼내기
# 함수의 인자 : 구분자
# split 함수는 공백을 기준으로 문자열을 쪼개고 결과를 리스트로 반환
lis = text.split(' ') # 공백
print(lis)

# 알파벳을 하나씩 출력하기
for ch in lis:
    print(ch)

# 사용이 끝났으면 닫기
f.close()

# ------------------
# 파일에서 내용 읽어오기

# 파일이름, 모드
f = open('file1.txt','r')

lis=f.readlines()
for line in lis:
    print(line, end='')

# print 함수에는 end라는 매개변수가 있고
# 기본값이 \n
print()
# ---------------------------
# 파일 내용 읽어오기
# 
# 파일이름,모드
# 경로가 같을때는 파일이름만 작성
f = open('file2.txt', 'r', encoding='utf-8')

# read 함수로 내용 읽어오기
lis = f.readlines()

# 내용을 한줄씩 출력
for line in lis:
    print(line, end='')

f.close()

# file2.txt의 현재 내용 : 1~10줄
# 새로운 내용 추가 : 11~21줄

# 내용 추가 -> 쓰기 모드(w 또는 a)
# 'w'모드는 기존의 내용을 덮어씌움
# 'a'모드는 이전 내용뒤에 새로운 내용이 추가됨
f = open('file2.txt', 'a', encoding='utf-8')

# 10번줄 뒤에
# 11~20번 줄을 추가!
for i in range(11,21):
    f.write(f'{i}번째 줄입니다\n')

f.close()