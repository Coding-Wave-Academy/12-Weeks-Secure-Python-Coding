def kmTOMiles(km):
    return km * 0.6

def milesToKm(miles):
    return miles / 0.6

def celToFah(cel):
    return  (cel * (9/5)) + 32

def fahToCel(fah):
    return (fah - 32) * 5/9


while True:
    print("\nOur Unit Converter \n")
    print("1. KM to Miles \n2. Miles to KM \n3. Cel to Fah \n4. Fah to Cel \n5. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        km = float(input("Enter distance in km: "))
        print("Distance in miles: ",kmTOMiles(km))

    elif option == 2:
        miles = float(input("Enter distance in mile: "))
        print("Distance in km: ", milesToKm(miles))

    elif option == 3:
        cel = float(input("Enter temperature in cel: "))
        print("Temperature in Fah: ", celToFah(cel))

    elif option == 4:
        fah = float(input("Enter temperature in fah: "))
        print("Temperature in Cel: ", fahToCel(fah))

    elif option == 5:
        print("Exiting program.......")
        break

    else:
        print("Invalid option, try again")



