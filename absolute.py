# -*- coding: utf-8 -*-
def abs(numberInput):
    numberIn = float(numberInput)
    numberOut = 0.0

    if numberIn < 0.0:
        numberOut = -numberIn
    else:
        numberOut = numberIn

    print numberOut


if __name__ == "__main__":
    abs(raw_input("Please input a number:"))
