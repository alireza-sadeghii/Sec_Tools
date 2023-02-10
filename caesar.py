# @Author: Alireza
# CS50 Project
# Sec Tools : Caesar Cipher


# caesar encryption with key = n
def encryption(text, n):
    encrypted = ""
    for letter in text:
        if letter.isalpha():
            encrypted += convert(letter, n)
        else:
            encrypted += letter
    return encrypted


# caesar decryption with key = n
def decryption(text, n):
    decrypted = ""
    for letter in text:
        if letter.isalpha():
            decrypted += convert(letter, int(-1 * n))
        else:
            decrypted += letter
    return decrypted


# convert each letter base on caesar algorithm
# D(x) = (x + n) mod 26
# E(x) = (x - n) mod 26
def convert(letter, n):
    scale = 'A' if letter.isupper() else 'a'
    let_num = ord(letter) - ord(scale)
    return chr((let_num + n) % 26 + ord(scale))