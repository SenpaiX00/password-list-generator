import string
from random import *
import sys

passwords = []
filename = 'possible-passwords.txt'

# read keywords from the file
pwlist = open("passwords.txt", "r")
passwords = pwlist.read().splitlines()
pwlist.close()

print("Input number of iterations:\n")
num = input(sys.argv)
i = int(num)

# generate random characters:
        #characters = string.ascii_letters + string.punctuation  + string.digits

#When passwords are used, they shall be complex and shall at least meet the following password construction requirements:
#a. Be a minimum of eight (8) characters in length.
#b  Contain characters from at least three (3) of these groupings: uppercase
#letter, lower case letter, numeric, and special characters.
#c. Not be the same as the User ID with which they are associated.
#d. Not contain repeating or sequential characters or numbers.
#e. Not use personal data such as dates, names, etc.

for p in passwords:
    pw = p
    np = p+string.digits
    nnp = p + string.digits + string.punctuation


while i > 0:
# create banned passwords

    for p in passwords:
        password111 = p
        npassword = password111+choice(string.digits)+choice(string.punctuation)
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password111 = p
        npassword = password111+choice(string.punctuation)+choice(string.digits)
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password11 = p
        npassword = password11+choice(string.digits)+choice(string.digits)+choice(string.digits)
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password20 = p
        npassword = password20+choice(string.digits)+choice(string.digits)+choice(string.digits)+choice(string.digits)+choice(string.digits)+choice(string.digits)
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password12 = p
        npassword = choice(string.digits)+choice(string.digits)+choice(string.digits)+password12
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password13 = p
        npassword = password13+choice(string.digits)+choice(string.digits)+choice(string.digits)+choice(string.punctuation)
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password14 = p
        npassword = password14+choice(string.punctuation)+choice(string.digits)+choice(string.digits)+choice(string.punctuation)
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password15 = p
        npassword = password15+choice(string.punctuation)+choice(string.punctuation)+choice(string.punctuation)+choice(string.punctuation)
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")
#------------------------------------------Reverse order ----------------------------------------------
    for p in passwords:
        password16 = p
        npassword = choice(string.digits)+choice(string.digits)+choice(string.digits)+choice(string.punctuation)+password16
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password18 = p
        npassword = choice(string.punctuation)+choice(string.punctuation)+choice(string.punctuation)+choice(string.punctuation)+password18
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")

    for p in passwords:
        password21 = p
        npassword = choice(string.digits)+choice(string.digits)+choice(string.digits)+choice(string.digits)+choice(string.digits)+choice(string.digits)+password21
        with open(filename, 'a') as file_object:
                file_object.write(repr(npassword).strip("'") + "\n")



    i = i -1
    print("Interations left = ", i)

print("Finished. Exiting program")


# When done, to ensure duplicates are rmeoved, do the following in PowerShell:
# gc banned-passwords.txt | sort | get-unique > banned-passwords-final.txt
