# Sec Tools
#### A set of tools used in cybersecurity
####
####
## Description :
the Sec Tools is an application that provides some of tools for simple cybersecurity actions.

### Features
- Caesar Cipher
    * encryption and decryption [Caesar][caesar] cipher based on user input and key

- [Nmap][nmap] Scan
    * running enumeration on the target IP provided by the user

- FTP Scanner
    * the scanner that checks whether one can log in anonymously to the FTP server or not

- Pssword Cracker
    * cracking the hashed password that is given by the user to program

- Find Deleted Files
    * finding names of all removed files

- Zip File Cracker
    * cracking a zip file in brute force way with help of rockyou password list

- Check IP
    * checking the security of an IP with the help of [AbuseIP][abuseip] database

\
\
all of the program sources are coded in python and to make the executable file, I used [auto-py-to-exe][autopytoexe].
\
The list of all used libraries is ready below :
- zipfile
- os
- ftplib
- json
- request
- nmap
- hashlib

and also the AbuseIp API and the [rockyou][rockyou] password wordlist is used in this project
before using the program, put the rockyou password list file in the project file


### Author

- [@Alireza Sadeghi⚡](https://github.com/alireza-sadeghii)

### Feedback

If you have any feedback, please contact me at alireza_sad@yahoo.com

[//]: # (These are reference links used in the body)

   [Caesar]: <https://en.wikipedia.org/wiki/Caesar_cipher>
   [autopytoexe]: <https://github.com/brentvollebregt/auto-py-to-exe>
   [nmap]: <https://nmap.org/>
   [abuseip]: <https://www.abuseipdb.com/>
   [rockyou]: <https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt>
