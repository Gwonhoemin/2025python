# 빈 리스트 생성 후 차례대로 추가
fruits = []
fruits.append("사과")
fruits.append("바나나")
fruits.append("포도")
print(fruits)

# 두번째 요소(20)을 99로 변경 
numbers = [10,20,30,40]
numbers[1] = 99
print(numbers)

# 첫번째 요소 삭제
animals = ["강아지", "고양이", "토끼"]
del animals[0]
print(animals)

# "영어" 삭제
subjects = ["국어","영어","수학","과학"]
subjects.remove("영어")
print(subjects)

# 마지막 요소 꺼내면서 삭제
scores = [70, 80, 90, 100]
scores.pop()
print(scores)