#is ROT13 is a caesar cipher with a key of 13?
#can use algorithm to both encypt and decrypt 


def rot13(message):
    message = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new = ""

    for char in message:
        if char.isspace():
            new += " "
            continue
        #find the char in the alphabet add 13 and mod 26 for the len of alphabet
        new += alphabet[(alphabet.find(char) + 13) % 26]       
    return new


message = "is it just me or is it getting crazier out there"
print(rot13(message))
#double rot13 twice as secure
print(rot13(rot13(message))) 