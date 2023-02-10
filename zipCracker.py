# @Author: Alireza
# CS50 Project
# Sec Tools : Zip File Cracker

import zipfile

# crack zip file pass with help of passwords wordlist
def crack_zip(file_path):
    result = []
    try:
        zip_file = zipfile.ZipFile(file_path)
    except:
        result.append("File Not Found !")
    with open("rockyou.txt", "r", errors='ignore') as passwords:
        for password in passwords:
            password = password.strip('\n')
            cracked = extract(zip_file, bytes(password, 'utf-8'))
            if cracked == "can not":
                result.append("Can not crack this zip file")
                break
            if cracked:
                result.append("File Cracked Successfully")
                result.append("Password : " + password)
                break
    return result


# extract zip file
def extract(zip_file, password):
    try:
        zip_file.extractall(path=".\\extracted_zip", pwd=password)
        return password
    except Exception as e:
        if "That compression method is not supported" in str(e):
            return "can not"
        return