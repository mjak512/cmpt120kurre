
# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Michael Kurre
# Created: 2019-03-01

def inputName():
    global first, last
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
def createUser():
    global uname
    uname = first + "." + last +"1"
    uname = uname.lower()

def createPassword():
    global passwd
    passwd = input("Create a new password: ")

def passwordStrength():
    global passwd
    while True:
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        if len(passwd) >= 8:
           print("The force is strong in this one...")
           print("Account configured. Your new email address is",
                uname + "@marist.edu")
           break
                    
def main():
    inputName()
    createUser()
    createPassword()
    passwordStrength()
main()
