#Making a menu

import os


class colours:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    PINK = '\033[35m'
    BOLD = '\033[1m'
    END = '\033[0m'

def MeterToYard():
    meter = float(input("Input the amount of meters: "))
    yard = meter*1.093613
    print(meter,"meters is",yard,"yards! ")
    print()

def YardToMeter():
    yard = float(input("Input the amount of yards: "))
    meter = yard/1.093613
    print(yard,"yards is",meter,"meters! ")
    print()

def KiloToLbs():
    kilo = float(input("Input the amount of kilograms: "))
    Lbs = kilo*2.20462
    print(kilo,"kilometers is",Lbs,"pounds! ")
    print()

def LbsToKilo():
    Lbs = float(input("Input the amount of pounds: "))
    Kilo = Lbs/2.20462
    print(Lbs,"pounds is",Kilo,"kilometers! ")
    print()

def CelsiusToFahrenheit():
    Cel = float(input("Input the temperature in celsius: "))
    F = Cel*(9/5)+32
    print(Cel,"celsius is",F,"fahrenheit! ")
    print()

def FarenheitToCelsius():
    F = float(input("Input the temperature in farenheit: "))
    Cel = (F-32)*(5/9)
    print(F,"fahrenheit is",Cel,"celsius! ")
    print()

def KMHToMPH():
    Kilometer = float(input("Input the amount of kilometers per hour: "))
    Mile = Kilometer*0.621371
    print(Kilometer,"kilometers an hour is",Mile,"miles an hour!")
    print()

def MPHToKMH():
    Mile = float(input("Input the amount of miles per hour: "))
    Kilometer = Mile/0.621371
    print(Mile,"miles an hour is",Kilometer,"kilometers an hour")
    print()

clear = lambda: os.system('cls')
userinput = "0"

while userinput != "5":
    print()
    print(colours.BOLD+"==MENU==".center(30)+colours.END)
    print()
    print(colours.BLUE+"1.","Meters and Yards".rjust(19," ")+colours.END)
    print(colours.GREEN+"2.","Kilograms and Pounds".rjust(23," ")+colours.END)
    print(colours.RED+"3.","Celsius and Fahrenheit".rjust(25," ")+colours.END)
    print(colours.PINK+"4.","Km/H and MPH".rjust(15," ")+colours.END)
    print(colours.BOLD+"5.","Quit".rjust(7," ")+colours.END)
    print()
    userinput = str(input("Select an option (1-5): "))
    clear()

    if userinput == "1":
        print(colours.BLUE+"1. ","Convert Meters to Yards".rjust(25, " "))
        print("2.","Convert Yards to Meters".rjust(26," "))
        print("3.","Go back to menu".rjust(18," ")+colours.END)
        check = input("Select an option (1-3): ")

        if check == "1":
            MeterToYard()
            print()
            check2 = input(colours.BOLD+"Would you like to return to the menu? (Y/N): "+colours.END)
            print()
            if check2 == "Y":
                continue
            else:
                break

        elif check == "2":
            YardToMeter()
            print()
            check2 = input(colours.BOLD+"Would you like to return to the menu? (Y/N): "+colours.END)
            print()
            if check2 == "Y":
                continue
            elif check2 =="N":
                break

        elif check == "3":
            continue
    
    elif userinput == "2":
        print(colours.GREEN+"1.","Convert kilograms to pounds".rjust(30," "))
        print("2.","Convert pounds to Kilograms".rjust(30," "))
        print("3.","Go back to menu".rjust(18," ")+colours.END)
        check = input("Select an option (1-3): ")
        if check == "1":
            KiloToLbs()
            print()
            check2 = input(colours.BOLD+"Would you like to return to the menu? (Y/N): "+colours.END)
            print()
            if check2 == "Y":
                continue
            else:
                break

        elif check == "2":
            LbsToKilo()
            print()
            check2 = input(colours.BOLD+"Would you like to return to the menu? (Y/N): "+colours.END)
            print()
            if check2 == "Y":
                continue
            elif check2 =="N":
                break

        elif check == "3":
            continue

    elif userinput == "3":
        print(colours.RED+"1.","Convert celsius to fahrenheit".rjust(32," "))
        print("2.","Convert fahrenheit to celsius".rjust(32," "))
        print("3.","Go back to menu".rjust(18," ")+colours.END)
        check = input("Select an option (1-3): ")
        if check == "1":
            CelsiusToFahrenheit()
            print()
            check2 = input(colours.BOLD+"Would you like to return to the menu? (Y/N): "+colours.END)
            print()
            if check2 == "Y":
                continue
            else:
                break

        elif check == "2":
            FarenheitToCelsius()
            print()
            check2 = input(colours.BOLD+"Would you like to return to the menu? (Y/N): "+colours.END)
            print()
            if check2 == "Y":
                continue
            elif check2 =="N":
                break

        elif check == "3":
            continue

    elif userinput == "4":
        print(colours.PINK+"1.","Convert KMH to MPH ".rjust(22," "))
        print("2.","Convert MPH to KMH".rjust(21," "))
        print("3.","Go back to menu".rjust(18," ")+colours.END)
        check = input("Select an option (1-3): ")
        if check == "1":
            KMHToMPH()
            print()
            check2 = input(colours.BOLD+"Would you like to return to the menu? (Y/N): "+colours.END)
            print()
            if check2 == "Y":
                continue
            else:
                break

        elif check == "2":
            MPHToKMH()
            print()
            check2 = input(colours.BOLD+"Would you like to return to the menu? (Y/N): "+colours.END)
            print()
            if check2 == "Y":
                continue
            elif check2 =="N":
                break

        elif check == "3":
            continue