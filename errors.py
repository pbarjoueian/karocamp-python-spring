# def divide(a: float, b: float) -> float:
#     """Divide given numbers

#     Args:
#         a (float): first number
#         b (float): second number

#     Returns:
#         float: result
#     """
#     result: float = 0.0
#     try:
#         result: float = a / b
#     except ZeroDivisionError as e:
#         print(e)
#         print("Wrong parameters!!!!")
#     finally:
#         print("end!")

#     return result


# result: float = divide(2, 1)
# print("*********")
# print(result)


# def divide(a: float, b: float) -> float:
#     """Divide given numbers

#     Args:
#         a (float): first number
#         b (float): second number

#     Returns:
#         float: result
#     """
#     result: float = 0.0
#     result: float = a / b
#     return result


# def runner():
#     result: float = divide(2, 0)
#     return result


# print(runner())


class AgeParseException(Exception):
    pass


age_str = input("Enter your age")
try:
    age = int(age_str)
    if age < 0:
        raise AgeParseException("Age cannot be negative")
except AgeParseException as e:
    print("Wrong age")
    print(e)
    age = -1 * age
    print("Hello " + str(age))

except ValueError as e:
    print("Could not parse input as number")
    print(e)
    print(e.args)

# name: str = "Shima"
# if name == "Ahmad":
#     raise ValueError("Wrong name")
# else:
#     print("Hello " + name)
