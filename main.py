"""Skymiles calculator to fing out how many points you'll earn for specific purchases"
    Sam Goldberg
"""
import functions
def main():
    p, t = functions.menu() #P is the dollar amount, t is the type of purchase
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