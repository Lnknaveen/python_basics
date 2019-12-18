def greet_user(f_name, l_name):
    print(f"Hi {l_name}, {f_name}!")
    print("How are you?")


greet_user(l_name="Lokesh", f_name="Naveen")
greet_user("Charvik", "Naveen")
greet_user("Praveen", l_name="Lokesh")


def square(number):
    return number * number


print(f"Square : {square(2)}")


def default_none():
    print("always returns None")


print(default_none())


def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😄",
        ":(": "☹️"
    }
    res = ""
    for word in words:
        res += emojis.get(word, word) + " "

    return res


print(emoji_converter(input("> ")))
