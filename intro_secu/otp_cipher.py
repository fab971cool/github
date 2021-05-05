import sys
import random as rdm
import bitstring as bsg

# !prend 2 liste de bits en entrée
# ?Pour l'instant on travail avec des char
# renvoie le message chiffré entre A et K = C  
def cipherOtp( message, keyMessage):

    cipher = []

    print  (str(message))


    for (mes, key) in zip(message, keyMessage):
        cipher.append( chr(ord(mes) ^ ord(key)))
    

    #cipher = "".join(cipher)

    return cipher

def decipherOtp( message, keyMessage):
    cipher = []

    print  (str(message))


    for (mes, key) in zip(message, keyMessage):
        cipher.append( chr(ord(mes) ^ ord(key)))
    

    #cipher = "".join(cipher)

    return cipher

# genere une cle "aleatoire" de longueur n
# !devrais retourner des bytes
def generateKey(n :int):
    result = []
    
    for i in range(n):
        result.append(rdm.randint(0, 4096))

    result = "".join(result)

    return result

def convertIntoBits(toConvert):
    print (type(toConvert))

    if type(toConvert) is not str:
        return toConvert
    result = bytearray()
    for i in toConvert:
        #result = ''.join(format(ord(i), 'b') )
        result.append(ord(i))
        #result.append(ord(i))

    return result


inputText = "This is street"

#inputText = convertIntoBits(inputText)
autre = "xvhe uw nopzzz"
#autre = convertIntoBits("xvhe uw nopzzz")

#print (inputText)

test = cipherOtp(inputText, autre)
print(test)



#file = open("./file.txt", "wb+")
"""
num = [76, 77, 78, 79]
array = bytearray(num)
print (array)
file.write(array)
file.close()

with open("./file.txt", 'rb') as file:
    num = file.read()
    print (num[0])
    test = num.hex()
    test = convertIntoBits(test)
    print(test[0])
    #test = '\x01' ^ test[0]
file.close()
"""