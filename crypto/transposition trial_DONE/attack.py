with open("message.txt", "r") as message:
    message = message.read()

blocks = [message[i * 3:(i + 1) * 3] for i in range((len(message) + 3 - 1) // 3 )]

final = [ block[-1] + block[:-1] for block in blocks ]

print("".join(final))
