# -*- coding: utf-8 -*-
try:
    def abs(numberInput):
        numberIn = float(numberInput)
        numberOut = 0.0

        if numberIn < 0.0:
            numberOut = -numberIn
        else:
            numberOut = numberIn

        print numberOut
        return numberOut


    if __name__ == "__main__":
        result = abs(raw_input("Please input a number:"))
        print "Result=" + result
except ValueError:
    print "Is that a vaild input?"
    exit(1)
# TODO:Fix module import problem.
