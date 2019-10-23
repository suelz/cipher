
def caesar(message, key):
    new = ""
    message = message.lower()

    for i in range(len(message)):
        char = message[i]

        new += chr((ord(char) + key - 97) % 26 + 97)

    return new

def decrypt(message, key):
    new = ""
    message = message.lower()

    for i in range(len(message)):
        char = message[i]

        new += chr((ord(char) - key - 97) % 26 + 97)

    return new




