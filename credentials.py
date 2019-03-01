
# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Michael Kurre
# Created: 2019-03-01

def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    uname = first + "." + last +"1"
    passwd = input("Create a new password: ")
    while True:
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        if len(passwd) >= 8:
           print("The force is strong in this one...")
           print("Account configured. Your new email address is",
                uname + "@marist.edu")
           break
main()
