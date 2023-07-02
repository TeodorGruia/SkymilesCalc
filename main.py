"""
Program name: Skymiles Calculator
Date of first writing: 6/25/2023
Author: Sam Goldberg
"""


import functions
def main():
    p, t = functions.menu() # P is the dollar amount, t is the type of purchase
    res = functions.get_miles(float(p), t)
    print(res)
    cont()
def cont():
    print("Do another calculation? ")
    x = input("[Y]es or [N]o? ")
    if x == "y":
        main()
    if x == "n":
        exit()



if __name__ == '__main__': main()