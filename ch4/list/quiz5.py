shopping = ["우유","빵","달걀"]

# 1) "사과"추가
shopping.append("사과")
# 2) 두번째 요소(빵)를 "치즈"변경
shopping[1] = "치즈"
# 3) "우유"삭제
del shopping[0]

scores = [60, 75, 80, 90]
# 1) 100 추가
scores.append(100)
print(scores)
# 2) 세번째요소(80)를 85 수정
scores[2]=85
print(scores)
# 3) 마지막 요소 꺼내면서 삭제
scores.pop()
print(scores)

animals = ["강아지", "고양이", "토끼", "햄스터"]
# 1) 고양이 -> 고슴도치 변경
animals[1] = "고슴도치"
print(animals)
# 2) 첫번째요소 삭제
del animals[0]
print(animals)
# 3) 마지막 요소 꺼내면서 삭제
animals.pop()
print(animals)