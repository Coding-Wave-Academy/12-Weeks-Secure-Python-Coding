flag = "learnsecurepython101"
userInput = input("Submit flag: ")
userInput = userInput.lower().replace(" ", "")

if userInput == flag:
    print("Lovely, your flag is: ",flag)
else:
    print("incorrect, try again")