import string
alphabet = string.printable[36:62] + string.printable[:10] + '_'
with open("message.txt", "r") as message:
    numbers = message.read().split(" ")[:-1]
adj = [int(num) % 37 for num in numbers]

s = [alphabet[i] for i in adj]

print("".join(s))
