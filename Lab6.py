# Kobidh


def encode(password):
    encoded_password = ""
    for i in password:
        i = int(i)
        i = i + 3
        i = str(i)
        encoded_password = encoded_password + i
    encoded_list = str(encoded_password)
    print(encoded_list)


def decode(password):
    encoded_password = ""
    for i in password:
        i = int(i)
        i = i - 3
        i = str(i)
        encoded_password = encoded_password + i
    encoded_list = str(encoded_password)
    print(encoded_list)


decode("3355")
