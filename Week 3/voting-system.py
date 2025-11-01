# --- various options as functions ---

def register():
    print("##### Registration process #####")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You can now vote")
        voters.update({name: age})

    else:
        print("Ineligible to vote, try again when you are older")


def view():
    print("---- Candidate List ----\n")
    for cn, cvc in candidate.items():
        print(f"{cn} --- {cvc}")


def vote():
    print("##### Voting Panel #####")
    name = input("Enter your name: ")
    if voters.get(name):
        candidate_name = input("\nType the name of the candidate you want to vote: ")
        add_vote = candidate.get(candidate_name) + 1
        candidate.update({candidate_name: add_vote})
        print("Vote successfully added!")
    else:
        print("You must be a registered voter before voting\n")
        register()

# --- candidates and voters database ---

candidate = {
    "kandi":0,
    "ribert":0,
    "junior":0,
    "adekunle":0,
    "owoyele":0
}

voters = {
    "jboy":20
}

# --- start of program ---

print("\nSimple Voting System \n")

while True:
    print("1. Registration \n2. Vote for Candidate \n3. View candidate list \n4. Exit")
    option = int(input("Select your option from the menu: "))

    if option == 1:
        register()

    elif option == 2:
        vote()

    elif option == 3:
        view()

    elif option == 4:
        print("Program exited...")
        break

    else:
        print("invalid option, try again")