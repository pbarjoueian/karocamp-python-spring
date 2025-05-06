def get_max(numbers=[]):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


numbers = [3, 45, 8, 4, 2, 5, 60, 1]
maximum = get_max(numbers=numbers)
print(maximum)


def sort_list(numbers=[]):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


print(sort_list(numbers=numbers))
