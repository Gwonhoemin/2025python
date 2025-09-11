# app.py
# 쇼핑몰의 상품 주문을 관리하는 프로그램

# 주문이력을 저장할 리스트
orders = []

# find_order_name [test-data]
# orders = [{'order_no':1, 'name':'둘리', 'product':'셔츠', 'count':1,'price':2000},
#           {'order_no':2, 'name':'도우너', 'product':'바지', 'count':2,'price':6000},
#           {'order_no':3, 'name':'둘리', 'product':'치마', 'count':3,'price':5000},
#           {'order_no':4, 'name':'또치', 'product':'치마', 'count':3,'price':5000},
#           {'order_no':5, 'name':'도우너', 'product':'치마', 'count':3,'price':5000}
#           ]


# 주문번호를 자동으로 생성하는 함수
# 새로운 주문번호를 만들어서 반환
def generate_order_no():
    # 만약 리스트에 주문정보가 하나도 없다면 => 1번
    # 아니라면 리스트의 현재 크기를 확인하고 +1
    if len(orders) == 0:
        return 1
    else:
        return len(orders) + 1 # next

# 주문 이력 만들기
# 고객명, 상품명, 수량, 가격을 묶어서 하나로 만들기
# -> 딕셔너리
def create_order(name, product, count, price):
    # 함수를 사용해서 다음번호 생성
    new_no = generate_order_no()

    # 주문번호
    # 나머지는 사용자에게 입력받은 그대로 저장
    order = {
                'order_no': new_no, #주문번호
                'name':name,
                'product':product,
                'count':count,
                'price':price
            } # key:value
    return order

# 주문 이력을 조회하는 함수
def all_list():
    # 리스트에 담긴 값들을 출력
    for o in orders:
        total = o['count'] * o['price']
        print(
            '주문번호:', o['order_no'],
            '주문자명:', o['name'], 
            '상품명:', o['product'],
            '수량:', o['count'], 
            '가격:', o['price'],
            '총액:', total
        )

# 특정 회원의 주문 건수와 주문금액 구하기

# 매개변수: 회원의 이름
# 결과 : 총 건수
def get_order_count(customer):
    # 주문이력 리스트에서 해당 회원의 이름이 있는 데이터 건수 세기
    # 총 주문 건수를 담을 변수를 선언
    cnt = 0
    # 리스트 안에 있는 주문이력을 하나씩 꺼내기
    for o in orders:
        if o['name'] == customer:
            cnt+=1
    # 함수가 끝나기전에 결과를 리턴
    return cnt
        
# 특정 고객의 총 주문 금액을 구하는 함수
# 매개변수: 고객의 이름
# 결과: 총 주문 금액
def get_order_price(name):
    # 전체 금액 구하기
    sum = 0
    for o in orders:
        if o['name'] == name:
            total = o['price']*o['count']
            sum = sum + total # 누적
    # 구한 결과(총금액)을 리턴
    return sum

# print(get_order_count('둘리'))
print(get_order_price('도우너'))

while True:
     
    # 메뉴 보여주기
    print('\n1. 상품 주문하기')
    print('2. 전체 주문 이력 보기')
    print('3. 고객별 주문 통계')
    print('4. 끝내기')

    # 메뉴 입력받기
    select = input('옵션을 선택하세요: ')

    # 사용자가 선택한 옵션에 따라 작업
    if select == '1':
        # 상품 주문
        # 사용자로부터 주문 정보 받기
        # 고객명, 상품명, 수량, 가격
        name = input('고객명: ')
        product = input('상품명: ')
        count = int(input('수량:'))
        price = int(input('가격:'))
        # 주문 정보 만들기
        order = create_order(name,product,count,price)
        orders.append(order)

    elif select == '2':
        # 전체 주문 이력 조회
        all_list()

    elif select == '3':
        # 1. 고객명 입력받기
        name = input('검색할 고객의 이름을 입력하세요: ')

        # 2. 해당 고객의 주문건수와 주문금액 구하기
        cnt = get_order_count(name)
        print('주문건수: ', cnt)

        total = get_order_price(name)
        print('주문금액: ', total)


    elif select == '4':
        print('프로그램을 종료합니다')
        break


    