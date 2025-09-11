# 오류 여러개 처리하기
try:
    lis=[1,2,3]
    lis[3]
    4/0
except (IndexError,ZeroDivisionError) as e:
    print(e)


# lis = [1,2,3]
# lis[3] # IndexError

# 4/0 #ZeroDivisionError