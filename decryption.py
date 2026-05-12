import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
while True:
    rr_msg = input("enter a message to encrypt: ")
    plain_msg =[]

    for letter in rr_msg:
        if letter in key:
            i = key.index(letter)
            plain_msg.append(chars[i])
        else:
            plain_msg.append(letter)

print(''.join(plain_msg))
