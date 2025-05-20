def divide(a: float, b: float) -> float:
    """Divide given numbers

    Args:
        a (float): first number
        b (float): second number

    Returns:
        float: result
    """
    result: float = 0.0
    try:
        result: float = a / b
    except ZeroDivisionError as e:
        print(e)
        print("Wrong parameters!!!!")

    return result


result: float = divide(2, 0)
print("*********")
print(result)
