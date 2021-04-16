import random

def pas(a):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    for i in range(a):
        pass_index = random.randrange(len(alphabet))
        password += alphabet[pass_index]
    return password
