for item in 'Python':
    print("+", item)

for item in ['ABC', 'DEF', "GHI"]:
    print("-", item)

for item in [1, 2, 3]:
    print("+", item)

for item in range(10):
    print("-", item)

for item in range(5, 10):
    print("+", item)

for item in range(5, 10, 2):
    print("-", item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print("Total : ", total)
