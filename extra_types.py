from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p = Point(11, y=22)

print(p[0])
print(p.x)

Month = namedtuple("Month", ["jan", "feb", "mar"])

month = Month(1, 2, 3)

print(month.jan)


ingredients = {"flour", "water", "salt", "yeast"}
print(ingredients)
ingredients = set(["flour", "water", "salt", "yeast", "water"])
print(ingredients)
ingredients = frozenset(["flour", "water", "salt", "yeast"])
print(ingredients)
