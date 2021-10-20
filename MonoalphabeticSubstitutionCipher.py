'''
4. Write a program that can perform a letter frequency attack on any monoalphabetic substitution cipher without
human intervention. Your software should produce possible plain text in rough order of likelihood. It would be
good if your user interface allows user to specify " Give me top 10 possible plain texts"
'''
# Function to decrypt a monoalphabetic substitution cipher using the letter frequency attack
def printString(S, N):
    # Stores final 10 possible deciphered
    # plaintext
    plaintext = [None] * 10

    # Store the frequency of each letter in
    # cipher text
    freq = [0] * 26

    # Stores the frequency of each letter
    # in cipher text in descending order
    freqSorted = [None] * 26

    # Store which alphabet is used already
    used = [0] * 26

    # Traverse the string S
    for i in range(N):
        if S[i] != ' ':
            freq[ord(S[i]) - 65] += 1

    # Copy the frequency array
    for i in range(26):
        freqSorted[i] = freq[i]

    # Stores the string formed from concatanating the english letters in the decreasing frequency in the
    # english language
    T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # Sort the array in descending order
    freqSorted.sort(reverse=True)

    # Itearate over the range [0, 5]
    for i in range(10):
        ch = -1

        # Iterate over the range [0, 26]
        for j in range(26):
            if freqSorted[i] == freq[j] and used[j] == 0:
                used[j] = 1
                ch = j
                break

        if ch == -1:
            break

        # Store the numerical equivalent of letter
        # at ith index of array letter_frequency
        x = ord(T[i]) - 65

        # Calculate the probable shift used
        # in monoalphabetic cipher
        x = x - ch

        # Temporary string to generate one
        # plaintext at a time
        curr = ""

        # Generate the probable ith plaintext
        # string using the shift calculated above
        for k in range(N):

            # Insert whitespaces as it is
            if S[k] == ' ':
                curr += " "
                continue

            # Shift the kth letter of the
            # cipher by x
            y = ord(S[k]) - 65
            y += x

            if y < 0:
                y += 26
            if y > 25:
                y -= 26

            # Add the kth calculated/shifted
            # letter to temporary string
            curr += chr(y + 65)

        plaintext[i] = curr

    # Print the generated 5 possible plaintexts
    for i in range(10):
        print(plaintext[i])


# Driver code
# Given string
# S = "B TJNQMF NFTTBHF"
S = input("Enter the text :")
N = len(S)

# Function Call
printString(S.upper(), N)


'''
************* OUTPUT ************
Enter the text :give me top ten text
GIVE ME TOP TEN TEXT
GIVE ME TOP TEN TEXT
ACPY GY NIJ NYH NYRN
MOBK SK ZUV ZKT ZKDZ
CERA IA PKL PAJ PATP
GIVE ME TOP TEN TEXT
KMZI QI XST XIR XIBX
YANW EW LGH LWF LWPL
CERA IA PKL PAJ PATP
MOBK SK ZUV ZKT ZKDZ

'''