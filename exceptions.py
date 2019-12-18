try:
    age = int(input('Age: '))
    print(age)

    risk = 20000 / age
except ZeroDivisionError:
    print('Invalid age!')
except ValueError:
    print('Invalid Value!')
finally:
    print("I am there")
