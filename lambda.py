# multiply = lambda a, b: a * b

# print(multiply(5, 6))


pairs = [("one", 1), ("two", 2), ("four", 4), ("three", 3)]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
