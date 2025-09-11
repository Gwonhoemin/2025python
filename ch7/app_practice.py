# 상품 주문

# 주문이력을 저장할 리스트
orders = []

# 주문번호 증가시키는 함수
def generate_order_no():
    if len(orders) == 0:
        return 1
    else :
        return len(orders)+1

# 상품 주문하기 함수
def create_order(name,product,count,price):
    order = {
        'order_no':generate_order_no(),
        'name':name,
        'product':product,
        'count':count,
        'price':price
             }
    return order

# 주문 이력을 조회하는 함수
def all_list():
    for o in orders:
        total = o['count'] * o['price']
        print(
            '주문번호:', o['order_no'],
            '고객명:', o['name'],
            '제품명:', o['product'],
            '수량:', o['count'],
            '단가:', o['price'],
            '총액:', total
        )

# 한 고객의 주문건수 함수
def get_order_count(name):
    cnt = 0
    for o in orders:
        if o['name'] == name:
            cnt += 1
    return cnt

# 한 고객의 주문금액 계산 함수
def get_order_total(name):
    sum = 0
    for o in orders:
        if o['name'] == name:
            total = o['price']*o['count']
            sum = sum + total
    return sum

while True:
    print('\n1. 상품 주문하기')
    print('2. 전체 주문 이력 보기')
    print('3. 고객별 주문 통계')
    print('4. 끝내기')
    
    select = input('옵션을 선택하세요: ')

    if select == '1':
        name = input('고객명: ')
        product = input('제품명: ')
        count = int(input('제품수량: '))
        price = int(input('제품가격: '))

        order = create_order(name,product,count,price)
        orders.append(order)
        print('주문이 완료되었습니다.')

    elif select == '2':
        all_list()

    elif select == '3':
        name = input('고객명을 입력하세요: ')

        print('주문 건수:', get_order_count(name))
        print('주문 금액:', get_order_total(name))

    elif select == '4':
        print('프로그램을 종료합니다')
        break