names = ["ABC", "DEF", "GHI"]
print(names)
print(names[1])
print(names[-1])
print(names[1:])
print(names[:1])
print(names[:])
print(names[0:2])

names[0] = "zyx"
print(names)

# -----

values = [1, 2, 4, 5, 8, 23, 8, 234, 7897, 88888, 3242, 989, 2342, 8678]
large_number = values[0]
for value in values:
    if value > large_number:
        large_number = value
print("Large number: ", large_number)

# -----
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
matrix[0][1] = 20
print(matrix)
print(matrix[0][1])
for row in matrix:
    for column in row:
        print(column)
# -----
numbers = [5, 6, 3, 8, 3, 9, 3]
print(numbers)
numbers.append(2)

numbers.insert(0, 23)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(6))

print(3 in numbers)
print(34 in numbers)

print(numbers.count(3))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.copy())

numbers.clear()
print(numbers)

# -----
duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 5, 6, 7, 8, 3, 4, 6]
non_duplicates = []
for num in duplicates:
    if num not in non_duplicates:
        non_duplicates.append(num)
print(non_duplicates)