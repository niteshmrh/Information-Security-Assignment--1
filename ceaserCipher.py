'''
3. Write a program that can perform a letter frequency attack on an additive cipher without human intervention.
Your software should produce possible plain text in rough order of likelihood. It would be good if your user
interface allows user to specify " Give me top 10 possible plain texts"
'''
from collections import defaultdict


# importing the default dict from collection framework to count frequency

def FrequencyAttack(S):
    # N= length of plain text, S=Storing the String in captial letter
    N, S = (len(S), S.upper())

    # here plantext is stored as a list
    plaintext = []

    # decreasing order of frequency of alphabet
    english_alphabet_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # dictionary to store cipher text's frequency
    frequency = defaultdict(int)

    # calculating the frequency of above variable
    for c in S: frequency[c] += 1

    # Sorting frequency sfter that stored them into tuple
    sorted_frequency = tuple(sorted(frequency.items(), key=lambda i: i[1], reverse=True))

    for i in range(26):
        # calculating the key to zipping
        key = (26 + ord(sorted_frequency[0][0]) - ord(english_alphabet_frequency[i])) % 26
        similar_txt = ""

        for j in range(len(S)):
            # decrypting word by word
            if (S[j] >= 'A' and S[j] <= 'Z'):
                similar_txt += chr(65 + (ord(S[j]) - 65 + key) % 26)
            else:
                similar_txt += S[j]
        # appending them into plaintext list
        plaintext.append(similar_txt)

    return plaintext


pt = int(input("how many Simillar text you need (max: 26): "))
# input S
S = "Give me top ten possible plain texts"

# Function call and returning value was stored into plaintext
plaintext = FrequencyAttack(S)

print("\n\n DECRYPTING PLAINTEXTS ARE GIVEN BELOW:\n")
# printing the plaintexts
for i in range(pt % 26):
    print(i + 1, end=": ")
    print(plaintext[i], end="\n\n")
