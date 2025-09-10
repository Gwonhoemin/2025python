# 파일 열기

# open(파일이름, 모드)
f = open('file1.txt', 'w')

# 파일에 1부터 10까지 쓰기
for n in range(1,11):
    # write 함수의 매개변수는 int
    # int -> str
    f.write(f'{n}\n')
f.close()

# 파일을 쓰기 모드로 열기
f=open('file2.txt','w', encoding='utf-8')

# f.write('안녕하세요')
# 1부터 10까지 출력하기
for i in range(1,11):
    # i는 정수
    # int -> str
    f.write(f'{i}번째 줄입니다\n')
f.close()