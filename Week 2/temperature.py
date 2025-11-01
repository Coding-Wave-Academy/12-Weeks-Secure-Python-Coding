
try:
    temp = int(input("Enter temperature value between 0 - 100: "))
except ValueError:
    print("An error occurred, value for temperature can only be an integer")
else:
    if type(temp) is int and temp == temp in range(0, 101):
        if temp == temp in range(0, 21):
            print("It's Cold")

        elif temp == temp in range(20, 31):
            print("It's a Nice Day")
        else:
            print("It's very Hot!")
    else:
        print("Invalid Temperature range value")
