

def caesar(plainText, shift): 
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
       	else:
            cipherText += ch
    return cipherText
c = 'Li_Qex_Geiwev'
for i in range(26):	
    print(caesar(c, i))