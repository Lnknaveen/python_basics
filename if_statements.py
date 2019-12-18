is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day!")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day!")
    print("Wear warm cloths")
else:
    print("It's a lovely day")

print("Enjoy your day!")

# ------ Logical

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_high_income or not has_good_credit:
    print("Eligible for loan")

# ----- comparision
# ==, !=, >, <
temp = 20

if temp > 30:
    print("hot day")
else:
    print("it's not hot day")
