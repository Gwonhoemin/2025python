temp = ('bird', 'cat', 'dog')
b,c,d = temp
print(b,c,d) # bird cat dog

fruits = ("사과", "배", "포도", "귤", "딸기")
a, *rest = fruits
print(a)
print(rest)

x, y, *others = fruits
print(x, y)
print(others)