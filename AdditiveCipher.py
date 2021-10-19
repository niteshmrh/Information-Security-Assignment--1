# 1. Write a program that can encrypt  and decrypt using the Additive Cipher.
def Additive_encryption(plaintext, key):  # Function to Encrypt
    encryption_str = ''  # encrypted String can stored here
    for i in plaintext:  # Starting loop for encrypting each character
        if i.isupper():  # check lower Alphabet or Capital
            temp = 65 + ((ord(i) - 65 + key) % 26)  # formula to convert a given plaintext ‘P’ to ciphertext ‘C’
            # using key ‘K’
            encryption_str = encryption_str + chr(temp)  # Concatenation
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        else:
            encryption_str = encryption_str + i

    print("The ciphertext is:", encryption_str)
    return encryption_str


# function to decrypt the the encrypted text basically it works on receiver side
def Additive_decryption(ciphertext, key):
    decryption_str = ''  # decrypted String can stored here
    for i in ciphertext:  # Starting loop for decrypting each character
        if i.isupper():
            if ((ord(i) - 65 - key) < 0):  # formula to convert a given ciphertext ‘C’ to plaintext ‘P’ using key ‘K’
                # is:
                temp = 65 + ((ord(i) - 65 - key + 26) % 26)
            else:
                temp = 65 + ((ord(i) - 65 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        elif i.islower():
            if ((ord(i) - 97 - key) < 0):
                temp = 97 + ((ord(i) - 97 - key + 26) % 26)
            else:
                temp = 97 + ((ord(i) - 97 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        else:
            decryption_str = decryption_str + i

    print("The plaintext is:", decryption_str)


# Driver Code Main
if __name__ == "__main__":
    plaintext = input("Enter the plaintext:")
    key = int(input("Enter the key:"))
    ciphertext = Additive_encryption(plaintext, key)
    Additive_decryption(ciphertext, key)



'''
********** OUTPUT ***********
Enter the plaintext:I love you
Enter the key:9
The ciphertext is: R uxen hxd
The plaintext is: I love you
'''