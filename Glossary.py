items = {"rice":50, "brade":40, "pasta":30, "milk":65, "sugar":45, "salt":10, "cooking oil":150}
def glosarry():
    choice = input("Please select the item: ").lower()
    buy = input("Do you want to buy it? (Yes/No): ").lower()
    total = 10

    if buy == "yes" and choice in items:
        total += items[choice]
        print("Thank you for buying", choice)
        print("Price:", items[choice])
        print("total",total)
    elif buy == "no":
        print("Okay! ")
    else:
        print("Item not found. Please select from the list.")
glosarry()
