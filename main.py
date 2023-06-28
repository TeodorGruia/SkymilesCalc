"""Skymiles calculator to fing out how many points you'll earn for specific purchases"
    Sam Goldberg
"""
import functions
def main():
    p, t = functions.menu() #P is the dollar amount, t is the type of purchase
    res = functions.get_miles(p, t)
    print(res)




if __name__ == '__main__': main()