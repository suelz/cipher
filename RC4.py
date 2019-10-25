
import numpy

def KSA(key): #key_scheduling_algorithm
    '''
    S entries are set equal to values from 0 - 255 
    byte key is generated and held in T then copied into S as the loop continues 
    each S[i] swap with another byte based on value of T , S will contain values from 0 - 255
    '''
    key_length = len(key)
    S = list(range(256))
    T = 0
    for i in range(256): 
        T = (T + S[i] + key[i % key_length]) % 256
        S[i] , S[T] = S[T], S[i]
    return S

def PRGA(S, n): #pseudo_random_generation_algorithm
    ''' 
    over my head rn gonna reread wikipedia and 
    implemented from pseudo code explanation found online
    '''
    i, j = 0, 0
    key = []

    while n > 0:
        n -= 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i] , S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        key.append(k)

    return key

def key_array(s):
    return [ord(char) for char in s]



key = "APPLES"
key = key_array(key)
plaintext = "add elpaisacompa on snapchat"

S = KSA(key)

stream = numpy.array(PRGA(S, len(plaintext)))
plaintext = numpy.array([ord(i) for i in plaintext])

cipher = stream ^ plaintext

print(cipher.astype(numpy.uint8).data.hex())


