from pandas import Series, DataFrame

data = {
    'name': Series(['Mohammad', 'Shawn', 'Mendes', 'Patrick'], index=['a', 'b', 'c', 'd']),
    'age': Series([23, 37, 27, 78], index=['a', 'b', 'c', 'd']),
    'fare': Series([230.8, 111.3, 9.04], index=['a', 'b', 'd']),
    'survived': Series([True, False, False, True], index=['a', 'b', 'c', 'd'])
}

dataFrame = DataFrame(data)

print(dataFrame)