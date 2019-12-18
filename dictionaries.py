customer = {
    "name": "Test 1",
    "age": 25,
    "is_verified": True
}

print(customer["name"])
print(customer.get("name1"))
print(customer.get("name1", "default value"))
customer["name"] = "New Name"
print(customer)
customer["birthdate"] = "18.18.18"
print(customer)

# -----
phone = input("Phone: ")
number_dic = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
out = ""
for ph in phone:
    out += f"{number_dic.get(ph)} "
print(f" {out}!")

message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "😄",
    ":(": "☹️"
}
res = ""
for word in words:
    res += emojis.get(word, word) + " "
print(res)
