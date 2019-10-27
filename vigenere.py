

def generate_key(string, key):
    key = list(key)
    if len(string) is len(key):
        return key
    for i in range(len(string) - len(key)):
        key.append(key[i % len(key)])
    return ("".join(key))

def encrypt(string, key):
    cipher = [] 
    for i in range(len(string)): 
        temp = (ord(string[i]) + ord(key[i])) % 26
        temp += ord('A')   
        cipher.append(chr(temp)) 
    return("" . join(cipher))




message = "Word on the street is"
keyword = "red"

key = generate_key(message, keyword)
cipher = encrypt(message, key)

print(cipher)

