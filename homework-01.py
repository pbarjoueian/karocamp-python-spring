from persiantools.jdatetime import JalaliDate


def average(ages=[]) -> float:
    return sum(ages) / len(ages)


def calculate_age(year_of_birth: int) -> int:
    current_year: int = JalaliDate.today().year
    age: int = current_year - year_of_birth
    return age


def print_full_name(first_name: str, last_name: str) -> None:
    full_name: str = (first_name + " " + last_name).upper()
    print(full_name)


def main() -> None:
    ages = []
    students = []
    while True:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        birth_year = int(input("Enter birth year: "))
        age = calculate_age(birth_year)
        students.append(
            {
                "first_name": first_name,
                "last_name": last_name,
                "birth_year": birth_year
            }
        )
        ages.append(age)
        print("Do you want to add another student? (y/n)")
        if input() == "n":
            break
    print("Students:")
    for student in students:
        print_full_name(student["first_name"], student["last_name"])
    print("Age average would be: " + str(average(ages)))


main()
