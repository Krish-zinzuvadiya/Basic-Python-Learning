i = int(input("Enter Number : "))

match i:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:  # catch-all case
        print("Number not in range 0-5")
