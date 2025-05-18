# from pprint import pprint

# import cryptocode
# import persiantools

# from .functions_extra import foo


# age = 100
# age_seconds = age * 365 * 24 * 60 * 60

# if age_seconds < 100000000:
#     print("You are less than 100 million seconds old")
# elif age_seconds < 1000000000:
#     print("You are less than 1 billion seconds old")
# elif age_seconds < 2000000000:
#     print("You are less than 2 billion seconds old")
# else:
#     print("You are older than 2 billion seconds")
#     print("Else has been executed")


# print(random.choice([1, 2, 3, 4, 5, 6]))

# names = ["Alice", "Bob", "Charlie", "Peyman", "Golnaz"]
# pprint(names)

# for name in names:
#     print(f"Hello {name}!\n")


# for i in range(1, 10):
#     print(i)


# person = {"first_name": "Ali", "last_name": "Ahmadi"}

# for k, v in person.items():
#     if v == "Ali":
#         print(k)


# a = 1

# while a < 2000:
#     print(a)
#     a = a * 2


# a = 1

# while True:
#     a = a * 2
#     print(a)
#     if a > 1000:
#         break


def average(a, b, name):
    print(name)
    result = (a + b) / 2
    # print(result)
    return result


avg = average(a=2, name="Peyman", b=5)
print(avg)
