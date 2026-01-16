# cacti_bruteforce
Cacti bruteforce made in python.
I know it can be optimized much more and python is not the fastest programming language for doing this type of work, but needed to do a quick password spray and I quickly did this script.

## Usage:
```
cacti_bf.py [-h] [-l LOGIN] [-L LOGIN_LIST] [-p PASSWORD] [-P PASSWORD_LIST] -w WEB
```
- **-l** Uses a single string as a user
- **-L** Uses a text file as a user list
- **-p** Uses a single string as a password
- **-P** Uses a text file as a password list
- **-w** Select cacti login page

Similar syntaxt like hydra

Example:
```
python3 cacti_bf.py -L users.txt -p wonderful1 -w http://cacti.monitorsfour.htb/cacti/index.php
[*] Starting brute force with 20 user(s) and 1 password(s)
[*] Target: http://cacti.monitorsfour.htb/cacti/index.php
[+] Valid: Marcus:wonderful1
```
