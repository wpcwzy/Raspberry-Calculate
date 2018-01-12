# -*- coding: utf-8 -*-
def nameIt(inputName):
    nameInput = inputName
    firstName = ""
    lastName = ""
    dropped = ""
    words = []
    words = nameInput.split()

    # for English using country
    if len(words) > 1:
        firstName = words[0]
        lastName = words[1]
        words.pop(0)
        words.pop(0)
        dropped = words
        print "First name is:" + firstName
        print "Last name is:" + lastName
        print "Dropped:" + str(dropped)
    else:
        print"Wrong Input!"


if __name__ == "__main__":
    nameIt(raw_input("Please input the name you want:"))
