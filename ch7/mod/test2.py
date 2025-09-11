# 모듈 불러오기
import mod2

# 가져온 모듈 사용하기
mod2.hello()
mod2.hi()

# 모듈에서 특정 함수만 가져오기
# 여러개 가져올때는 ,컴마 => hello,hi
# 전체 *
from mod2 import *

hello() # 함수이름만 사용
hi()
