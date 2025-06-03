# import logging

# logging.basicConfig(
#     filename="logs.log",
#     level=logging.DEBUG,
#     filemode="a",
#     format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
# )


# logging.info("The script is about to start.")


# def division(a: float, b: float) -> float:
#     """Returns the division of two numbers.

#     Parameters:
#         a (float): The first number.
#         b (float): The second number.

#     Returns:
#         float: The division of the two numbers.
#     """
#     logging.debug(f"Dividing {a} by {b}.")
#     result: float = 0.0
#     try:
#         result: float = a / b
#     except ZeroDivisionError as e:
#         logging.error(f"Error occurred: {e}.")
#         logging.warning("Division by zero is not allowed.")

#     logging.debug(f"Result: {result}.")
#     return result


# result = division(10, 2)

# logging.info("The script has finished.")


import logging

import jdatetime


class JalaliFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        now = jdatetime.datetime.now()
        return now.strftime("%Y/%M/%d %H:%M:%S")


# Example usage
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = JalaliFormatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("This is a test log message.")
