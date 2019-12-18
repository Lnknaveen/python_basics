for x in range(4):
    for y in range(4):
        print(f"({x}, {y})")

numbers = [5, 1, 1, 1, 5]

for item in numbers:
    print("X" * item)

for item in numbers:
    result = ""
    for child in range(item):
        result += "X"
    print(result)
