usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "Hello"  and passwordInput == "1234":
    print("Done !")
    print("-------- Welcome --------")
    print("----- Product list -----")
    price1 = 300
    price2 = 150
    price3 = 50
    print("1. Table", price1, "per unit")
    print("2. Chair", price2, "per unit")
    print("3. Towel", price3, "per unit")
    print("What do you want to buy")
    Ta = int(input("Table = "))
    Ch = int(input("Chair = "))
    To = int(input("Towel = "))
    if Ta > 0:
        priceTa = price1 * Ta
    if Ch > 0:
        priceCh = price2 * Ch
    if To > 0:
        priceTo = price3 * To
    else:
        print("Thank you, hope to see you again")
    print("Total = ", (priceTa + priceCh + priceTo), "Bath")
    print("Thank you, hope to see you again")
else:
    print("Username or Password is incorrect")

