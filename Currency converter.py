# Currency converter. Dollar, Euro, Pound, Ruble, Franc, Turkish Lira 
print("⚠︎ DISCLAIMER ⚠︎")
print("The value of the currencies are dated to february 2024!")   
print(" ")
def main():
    print("Welcome to the currency converter!")
    print("1. Dollar")
    print("2. Euro")
    print("3. Pound")
    print("4. Ruble")
    print("5. Franc")
    print("6. Turkish Lira")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dollar()
    elif choice == 2:
        euro()
    elif choice == 3:
        pound()
    elif choice == 4:
        ruble()
    elif choice == 5:
        franc()
    elif choice == 6:
        turkish_lira()
    elif choice == 7:
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main()

def dollar():
    amount = float(input("Enter the amount in dollars: "))
    print("1. Euro")
    print("2. Pound")
    print("3. Ruble")
    print("4. Franc")
    print("5. Turkish Lira")
    print("6. Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The amount in euros is", amount * 0.93)
    elif choice == 2:
        print("The amount in pounds is", amount * 0.79)
    elif choice == 3:
        print("The amount in rubles is", amount * 91.38)
    elif choice == 4:
        print("The amount in francs is", amount * 0.87)
    elif choice == 5:
        print("The amount in turkish lira is", amount * 30.68)
    elif choice == 6:
        main()
    else:
        print("Invalid choice. Please try again.")
        dollar()

def euro():
    amount = float(input("Enter the amount in euros: "))
    print("1. Dollar")
    print("2. Pound")
    print("3. Ruble")
    print("4. Franc")
    print("5. Turkish Lira")
    print("6. Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The amount in dollars is", amount * 1.08)
    elif choice == 2:
        print("The amount in pounds is", amount * 0.85)
    elif choice == 3:
        print("The amount in rubles is", amount * 98.66)
    elif choice == 4:
        print("The amount in francs is", amount * 0.94)
    elif choice == 5:
        print("The amount in turkish lira is", amount * 33.12)
    elif choice == 6:
        main()
    else:
        print("Invalid choice. Please try again.")
        euro()

def pound():
    amount = float(input("Enter the amount in pounds: "))
    print("1. Dollar")
    print("2. Euro")
    print("3. Ruble")
    print("4. Franc")
    print("5. Turkish Lira")
    print("6. Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The amount in dollars is", amount * 1.26)
    elif choice == 2:
        print("The amount in euros is", amount * 1.17)
    elif choice == 3:
        print("The amount in rubles is", amount * 115.47)
    elif choice == 4:
        print("The amount in francs is", amount * 1.10)
    elif choice == 5:
        print("The amount in turkish lira is", amount * 38.76)
    elif choice == 6:
        main()
    else:
        print("Invalid choice. Please try again.")
        pound()

def ruble():
    amount = float(input("Enter the amount in rubles: "))
    print("1. Dollar")
    print("2. Euro")
    print("3. Pound")
    print("4. Franc")
    print("5. Turkish Lira")
    print("6. Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The amount in dollars is", amount * 0.011)
    elif choice == 2:
        print("The amount in euros is", amount * 0.010)
    elif choice == 3:
        print("The amount in pounds is", amount * 0.0087)
    elif choice == 4:
        print("The amount in francs is", amount * 0.0096)
    elif choice == 5:
        print("The amount in turkish lira is", amount * 0.34)
    elif choice == 6:
        main()
    else:
        print("Invalid choice. Please try again.")
        ruble()

def franc():
    amount = float(input("Enter the amount in francs: "))
    print("1. Dollar")
    print("2. Euro")
    print("3. Pound")
    print("4. Ruble")
    print("5. Turkish Lira")
    print("6. Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The amount in dollars is", amount * 1.14)
    elif choice == 2:
        print("The amount in euros is", amount * 1.06)
    elif choice == 3:
        print("The amount in pounds is", amount * 0.91)
    elif choice == 4:
        print("The amount in rubles is", amount * 104.54)
    elif choice == 5:
        print("The amount in turkish lira is", amount * 35.10)
    elif choice == 6:
        main()
    else:
        print("Invalid choice. Please try again.")
        franc()

def turkish_lira():
    amount = float(input("Enter the amount in turkish lira: "))
    print("1. Dollar")
    print("2. Euro")
    print("3. Pound")
    print("4. Ruble")
    print("5. Franc")
    print("6. Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The amount in dollars is", amount * 0.030)
    elif choice == 2:
        print("The amount in euros is", amount * 0.033)
    elif choice == 3:
        print("The amount in pounds is", amount * 0.026)
    elif choice == 4:
        print("The amount in rubles is", amount * 2.98)
    elif choice == 5:
        print("The amount in francs is", amount * 0.028)
    elif choice == 6:
        main()
    else:
        print("Invalid choice. Please try again.")
        turkish_lira()


main()
