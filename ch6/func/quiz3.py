# 문제 1. 나머지 매개변수를 사용하여
# 입력받은 과일의 이름만 출력
# ex) apple, banana, orange

def calc(**kwargs):
    for i in kwargs.keys():
        print(i)

calc(apple=1200, banana=800, orange=1500)

# 문제 2. 나머지 매개변수를 사용하여 입력받은 학생의 점수만 출력
# 결과) 90, 85, 100
def show_scores(**kwargs):
    for i in kwargs.values():
        print(i)

show_scores(철수=90, 영희=85, 민수=100)

# 문제 3. 나머지 매개변수를 사용하여 입력받은 도시 이름과 인구 수를 모두 출력하세요
# (인구 수는 만 명 단위)
# 결과) seoul 950, busan 340, incheon 300

def show_population(**kwargs):
    for (key, value) in kwargs.items():
        print(key, value*10000)

show_population(seoul=950, busan=340, incheon=300)

# 문제 4. 나머지 매개변수를 사용하여 입력받은 상품의 상품명만 출력하세요
# 결과) milk bread egg(가격은 무시하고 상품명만 출력)
def show_items(**kwargs):
    for key in kwargs.keys():
        print(key)
# 함수 호출
show_items(milk=2500, bread=2000, egg=3000)