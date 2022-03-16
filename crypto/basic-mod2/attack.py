#!/bin/python
import string

alphabet = string.printable[36:62] + string.printable[:10] + '_'

with open("message.txt", "r") as message:
    nums = message.read().split(" ")[:-1]

nums = [int(n) % 41 for n in nums]

mods = [pow(x, -1, 41) - 1 for x in nums]
letters = [alphabet[n] for n in mods]

print("".join(letters))
