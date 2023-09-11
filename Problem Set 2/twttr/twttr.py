vowels = ("a", "e", "i", "o", "u")
output = ""
user_input = input("Input: ")

for char in user_input:
    if char.lower() not in vowels:
        output += char

print(output)