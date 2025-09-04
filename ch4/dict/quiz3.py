cart = {"사과":3, "바나나":5, "딸기":2}

# 장바구니에 포도o -> 포도개수 출력
# 없으면 "포도가 장바구니에 없습니다" 출력

buy = '포도'
if buy in cart:
    print(buy,"가", cart[buy], "개 있습니다.")
else :
    print(buy , "(이)가 장바구니에 없습니다")


scores = {"수학" : 95, "영어":55, "국어":70}
if scores["영어"] >= 60 :
    print("합격")
else:
    print("불합격")