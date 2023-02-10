# @Author: Alireza
# CS50 Project
# Sec Tools : Password Cracker


import hashlib

# crack password base on user hash
# md5 hash function
# check with 10,000 common passwords
def crack(hash):
    result = []
    with open("rockyou.txt", "r") as passwordFile:
        for password in passwordFile:
            encoded_password = password.encode("utf-8")
            hashed_pass = hashlib.md5(encoded_password.strip()).hexdigest()
            if hashed_pass == hash:
                result.append("Password Is Found    :   " + password)
                break
    return result