# @Author: Alireza
# CS50 Project
# Sec Tools : FTP (File Transfer Protocol)


import ftplib


def access_check(host):
    result = []
    try:
        result.append("Set ftp server host ...")
        host_ftp = ftplib.FTP(host)
        result.append("Check for login ...")
        connect = host_ftp.login("anonymous", "anonymous")
        result.append("[+] " + str(host) + " Anonymous Login Succeeded ")
        host_ftp.quit()
    except Exception as ex:
        result.append("[-] " + str(host) + " Anonymous Login Fails \n")
        result.append("result : " + str(ex))
    return result