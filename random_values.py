import random
import string

for i in range(3):
    print(random.random())
    print(random.randint(10, 50))

alphabets = string.ascii_lowercase[:26]
print("random", random.choice(alphabets))


class Dice:
    def roll(self):
        f = random.randint(1, 6)
        s = random.randint(1, 6)
        return f, s


dice = Dice()
print(dice.roll())
