# 쇼핑몰 장바구니 딕셔너리 생성
shopping = {"사과":3, "바나나":5, "딸기":2}
print(shopping)
# 사과의 수량 10개로 변경
shopping["사과"] = 10
print(shopping)
# 바나나 삭제
del shopping["바나나"]
print(shopping)

# 시험점수 문제
test = {"수학":95}
test["영어"]=88
test["국어"]=100

# 카페 메뉴문제
cafe = {"아메리카노":2000, "라떼":3000, "케이크":4500}
cafe["아메리카노"]=2500
del cafe["케이크"]