def checkParity(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


number_to_check = int(input("Enter a number: "))
result = checkParity(number_to_check)
print("This number is ", result)
