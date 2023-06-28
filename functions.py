def menu():
    print("--Delta Skymiles Calculator--")
    print("How much was your total purchase?")
    purch_input = input(":> ")
    print("And what did you spend it on?")
    print("Choose from the following: ")
    print("d|h : Delta or hotel purchase")
    print("r|s : restuarant or groceries")
    print("o : Something else")
    purch_type = input(">: ")
    return purch_input, purch_type


def get_miles(total_purchases, type="d"):
    if type == "d" or type == "h":
        miles_earned = total_purchases * 3
        print(f"You have {miles_earned} miles via Hotels or Delta purchases")
    elif type == "r" or type == "s":
        miles_earned = total_purchases * 2
        print(f"You have {miles_earned} miles via Resturants or Groceries")
    else:
        miles_earned = total_purchases
        print(f"You have {miles_earned} miles via other purchases") 

