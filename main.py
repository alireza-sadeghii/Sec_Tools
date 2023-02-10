# @Author: Alireza
# CS50 Project
# Sec Tool : Main

import os
import subprocess
from caesar import encryption, decryption
from nmapScan import port_scan
from ftp import access_check
from passwordCracker import crack
from restore import find_files
from zipCracker import crack_zip
from ipCheck import check_ip

CENTER_SPACE = 32
#TODO: colorrize text
def main():
    # set terminal size
    set_terminal()

    # print title
    print_title()

    # print tools list
    print_terminal("[1] Caesar Encryption")
    print_terminal("[2] Caesar Decryption")
    print_terminal("[3] Nmap Scan [IP Information Gathering]")
    print_terminal("[4] FTP Scanner [FTP Anonymous Check]")
    print_terminal("[5] Password Cracker [Dictionary Attack]")
    print_terminal("[6] Find Deleted Files")
    print_terminal("[7] Zip file cracker [Crack Zip Password]")
    print_terminal("[8] Check IP [Check Ip In AbuseIpDB]")

    # print divider
    divider()
    read_tool_select()
    wait_exit()


# read user input
def read_tool_select():
    tool_select = input(">" + " " * CENTER_SPACE + "Enter Tool Number : ")
    clear_terminal()
    switch_tools(tool_select)

# clear terminal
def clear_terminal():
    os.system("cls")
    print_title()


# print title of terminal app
def print_title():
    print("\n" * 5)
    with open("title.txt", "r") as title:
        for row in title:
            print(" " * 21 + row, end="")
    divider()
    print()


# print divider line
def divider():
    print(" " * 17 + "_" * 70)
    print()


# print in center of terminal
def print_terminal(input):
    if len(input) > 50:
        print_terminal(input[0:28])
        print_terminal(input[28:])
    else:
        print(" " * CENTER_SPACE + input)


# set desired size of terminal
def set_terminal():
    cols = 100
    rows = 50
    os.system(f'mode con: cols={cols} lines={rows}')


# use caesar encryption/decryption
def caesar_input(type):
    text = input(" " * CENTER_SPACE + "Enter Your Text: ")
    try:
        key = int(input(" " * CENTER_SPACE + "Enter cipher Key: "))
    except:
        print_terminal("Just Enter Number For Key !")
        clear_terminal()
        ceasar_input(type)
    divider()
    result = decryption(text, key) if type == "DEC" else encryption(text, key)
    print_terminal(result + "\n")
    save_to_clip(result)


# use nmap scanner tool
def nmap_scan():
    host = input(" " * CENTER_SPACE + "Enter Target : ")
    scan_result = []
    try:
        print_terminal("Start Scan ...")
        scan_result = port_scan(host)
    except:
        print_terminal("Your target is not valid !")
        clear_terminal()
        main()
        pass
    nmap_result(scan_result)


# print output of nmap scan
def nmap_result(result):
    divider()
    for row in result:
        print_terminal(row)
    divider()

# read ftp host and check or login
def ftp_check():
    host = input(" " * CENTER_SPACE + "Enter FTP ip : ")
    result = access_check(host)
    divider()
    for row in result:
        print_terminal(row)
    divider()

# read password hash and crack to decoded pass
def crack_password():
    hash = input(" " * 22 + "Enter md5 hash of password : ")
    result = crack(hash)
    divider()
    print_terminal("Start cracking ...")
    if len(result) != 0:
        for row in result:
            print_terminal(row)
    else:
        print_terminal("Password Not Found !")

# find list of removed file
def find_removed_files():
    result = find_files()
    if len(result) == 0:
        print_terminal("Nothing Found !")
    for row, index in zip(result, range(10)):
        if index == 9:
            index = 0
            print_terminal("\n")
            input(" " * CENTER_SPACE + "Prees Enter To Continue Show The Files ...")
            clear_terminal()
        print_terminal(row)
    divider()

# read zipfile name and crack file
def crack_zipfile():
    file_path = input(" " * CENTER_SPACE + "Enter Zip file path : ")
    result = crack_zip(file_path)
    divider()
    for row in result:
        print_terminal(row)

# scan ip in abuseIpDB
def scan_ip():
    ip = input(" " * CENTER_SPACE + "Enter Ip : ")
    divider()
    result = check_ip(ip)
    for row in result:
        print_terminal(row)


# switch for tools
def switch_tools(input):
    match input:
        case "1":
            caesar_input("ENC")
        case "2":
            caesar_input("DEC")
        case "3":
            nmap_scan()
        case "4":
            ftp_check()
        case "5":
            crack_password()
        case "6":
            find_removed_files()
        case "7":
            crack_zipfile();
        case "8":
            scan_ip()
        case _:
                clear_terminal()
                print_terminal("Just Enter Number Of Desired Tool !")
                read_tool_select()


# save desired input to clipboard
#TODO: add for mac and linux
def save_to_clip(input):
    subprocess.run("clip", text=True, input=input)


# wait until user request to exit
def wait_exit():
    input(" " * CENTER_SPACE + "enter any key to exit ....")

if __name__ == "__main__":
    main()