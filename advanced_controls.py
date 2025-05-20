# length: int = 80
# message: str = None

# message = "short" if length <= 80 else "long"
# print(message)


# names = ["Alice", "Bob", "Charlie"]
# uppercase_names = [name.upper() for name in names]
# print(uppercase_names)

# amounts = [10, -7, 8, 19, -2]
# positive_amounts = [amount for amount in amounts if amount > 0]
# print(positive_amounts)


colors = {
    "red": "#ff0000",
    "green": "#008000",
    "blue": "#f000ff",
}

# for key, value in colors.items():
#     print(f"{key} - {value}")

# m_colors = {
#     name: value[1:] for name, value in colors.items()
# }

m_colors = {color: colors[color][1:] for color in colors}

print(m_colors)
