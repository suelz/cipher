
def caesar(message, key):
    new = ""
    message = message.lower()

    for i in range(len(message)):
        if message[i].isspace():
            new += " "
            continue
        char = message[i]

        new += chr((ord(char) + key - 97) % 26 + 97)

    return new

def decrypt(message, key):
    new = ""
    message = message.lower()

    for i in range(len(message)):
        if message[i].isspace():
            new += " "
            continue
        char = message[i]

        new += chr((ord(char) - key - 97) % 26 + 97)

    return new


def break_code(message):
    message = message.lower()
    for i in range(26):
        new = ""
        key = i + 1
        for j in range(len(message)):
            if message[j].isspace():
                new += " "
                continue
            char = message[j]
            new += chr((ord(char) - key - 97) % 26 + 97)
    
        print(new)
    


break_code("fyyfhp fy ifbs")




