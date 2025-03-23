print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

def priceSize(size):
    if size == "S":
        return 15
    elif size == "M":
        return 20
    else:
        return 25
    
def pricePepperoni(size, add_pepperoni):
    if add_pepperoni == "Y":
        if size == "S":
            return 2
        else:
            return 3

def priceCheese(extra_cheese):
    if extra_cheese == "Y":
        return 1
    else:
        return 0    

bill += priceSize(size)
bill += pricePepperoni(size, add_pepperoni)
bill += priceCheese(extra_cheese)   

print(bill)