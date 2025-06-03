from concurrent.futures import ThreadPoolExecutor


def print_multiple(text, n):
    for i in range(n):
        print(text, end="")


with ThreadPoolExecutor() as executor:
    executor.submit(print_multiple, ".", 10000)
    executor.submit(print_multiple, "o", 10000)

print("\ncompleted all tasks")
