
def bikini_bottom_cipher(message, key):
    new = ""
    message = message.lower()
    flag = True
    for i in range(len(message)):
        if message[i].isspace():
            new += " "
            continue
        if flag:
            new += chr((ord(message[i]) + key - 97) % 26 + 97).upper()
            flag = False
        else:
            new += chr((ord(message[i]) + key - 97) % 26 + 97)
            flag = True
    return new

print(bikini_bottom_cipher("spongebob im scared", 14))