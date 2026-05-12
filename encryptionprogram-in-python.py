import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
while True:
    plain_message = input("enter a message to encrypt: ")
    rr_msg =[]

    for letter in plain_message:
        if letter in chars:
            i = chars.index(letter)
            rr_msg.append(key[i])
        else:
            rr_msg.append(letter)

print(''.join(rr_msg))
