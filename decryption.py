import string


chars = list(" " + string.punctuation + string.digits + string.ascii_letters)

# Paste the same shuffled key used by your encryption program here.
# Example: key = list("your shuffled characters...")
key = chars.copy()


def decrypt_message(encrypted_message):
    plain_message = []

    for letter in encrypted_message:
        if letter in key:
            index = key.index(letter)
            plain_message.append(chars[index])
        else:
            plain_message.append(letter)

    return "".join(plain_message)


while True:
    try:
        encrypted_message = input("Enter a message to decrypt: ")
    except EOFError:
        break

    print(decrypt_message(encrypted_message))
