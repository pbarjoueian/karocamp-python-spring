def average(a: float, b: float) -> float:
    """
    Returns the average of two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The average of the two numbers.
    """
    return (a + b) / 2


result: float = average(2, 5)
print(result)
