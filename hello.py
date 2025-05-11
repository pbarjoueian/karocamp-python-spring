# # print("Peyman Develop")

# full_name = "  Peyman Barjoueian "
# full_name = full_name.rstrip()
# print(full_name)


# city = "Vienna"
# temperature = 23.7

# # rather obsolete
# print("weather in %s: %f°C" % (city, temperature))

# print("weather in {0}: {1}°C".format(city, temperature))
# print("weather in {}: {}°C".format(city, temperature))
# print("weather in {c}: {t}°C".format(c=city, t=temperature))

# print(f"weather in {city}: {temperature}°C")


# import math

# print(f"Pi is {math.pi:.6f}")

# print(f"Pi is {math.pi:.4g}")

# first_name = "Peyman"
# last_name = "Barjoueian"

# print(f"{first_name:^20}")


# menu_item = "Burger"
# price = 11.5

# print(f"{menu_item:<12} {price:>5.2f}$")


# users = ['mike', 'tim', 'theresa']

# for user in users:
#     print(user.upper())

person = {
    "first_name": "John",
    "last_name": "Doe",
    "nationality": "Canada",
    "birth_year": 1980,
}

for k, v in person.items():
    print(k + " " + str(v))
    
