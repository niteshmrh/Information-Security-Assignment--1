# Write a program that can encrypt and decrypt using the Affine Cipher
# The gcd function is going to help co-prime function so we need to declare the gcd function
def gcd(a, b):
    # Everything divides 0
    if (a == 0 or b == 0):
        return 0
    # base case
    if (a == b):
        return a
    # a is greater
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)


# Function to check if two numbers are co-prime or not
def coprime(a, b):
    if (gcd(a, b) == 1):
        return True
    else:
        return False


def affine_encrypt(msg, a, b):
    msg = msg.upper()
    # /Cipher Text initially empty
    cipher = ""
    for i in range(len(msg)):
        char = ord(msg[i])
        # Avoid space to be encrypted
        if (msg[i] != ' '):
            # applying encryption formula ( a x + b ) mod m
            cipher = cipher + chr(((((a * (char - 65)) + b) % 26) + 65))
        else:
            # else simply append space character
            cipher += msg[i]
    return cipher.lower()


def affine_decrypt(enc, a, b):
    enc = enc.upper()
    msg = ""
    a_inv = 0
    flag = 0

    # Find a^-1 (the multiplicative inverse of a in the group of integers modulo m.)
    for i in range(26):
        flag = (a * i) % 26
        # Check if (a*i)%26 == 1 ,then i will be the multiplicative inverse of a
        if (flag == 1):
            a_inv = i
    for i in range(len(enc)):
        char = ord(enc[i])
        if (enc[i] != ' '):
            # Applying decryption formula a^-1 ( x - b ) mod m
            msg = msg + chr((((a_inv * ((char + 65 - b)) % 26)) + 65))
        else:
            # else simply append space characte
            msg += enc[i]

    return msg.lower()


if __name__ == "__main__":
    msg = input("Enter message to encrypt: ")
    a, b = map(int, input("Enter key values a and b to encrypt: ").strip().split(" "))
    if (coprime(a, 26)):
        enc = affine_encrypt(msg, a, b)
        print("\nEncrypted Message: " + enc)
    else:
        print("\nSorry the value of a must be co prime of 26" + "\n")

    if (enc != ""):
        print("Decrypted Message : " + affine_decrypt(enc, a, b))
    else:
        print("\nSorry No Encrypted Message to decrypt")


'''
********* OUTPUT *********
Enter message to encrypt: danger
Enter key values a and b to encrypt: 17 20

Encrypted Message: tuhskx

Decrypted Message : danger

'''