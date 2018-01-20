# -*- coding: utf-8 -*-
try:
    def nameIt(inputName, outputThing):  # if outputThing=0,then output the first name.
        nameInput = inputName  # if outputThing=1,then output the last name.
        firstName = ""  # if outputThing=2,then output dropped.
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
            if outputThing == 0:
                return firstName
            else:
                if outputThing == 1:
                    return lastName
                else:
                    return dropped
        else:
            print"Wrong Input!"
            return -1


    if __name__ == "__main__":
        string = raw_input("Please input the name you want:")
        mode = int(raw_input("Please enter the running mode:"))
        result = nameIt(string, mode)
        print "Result=" + str(result)

except ValueError:
    print "Is that a vaild input?"
