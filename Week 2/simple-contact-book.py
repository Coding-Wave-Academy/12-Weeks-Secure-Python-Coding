contactBook = {}

while True:
    action = input("Enter a action(add/lookup/remove/view/exit): ")

    if action == "add":
        contactName = input("Enter name: ")
        contactPhoneNumber = input("Enter phone number: ")
        int(contactPhoneNumber)
        contactBook.update({contactName: contactPhoneNumber})

    elif action == "remove":
        toDelete = input("Type name to delete: ")
        if toDelete == toDelete in contactBook:
            contactBook.pop(toDelete)
            print("Contact has been deleted")
        else:
            print("Contact not found")

    elif action == "view":
        if len(contactBook) > 0:
            print("#### Your Contact List ####")
            for cn, cpn in contactBook.items():
                print(f"- {cn} ~ {cpn}")
        else:
            print("Contact book is empty, add some first")

    elif action == "lookup":
        toFind = input("Type name to find: ")
        if toFind == toFind in contactBook:
            print(f"Contact found: {toFind} ~ ",contactBook.get(toFind))
        else:
            print("Contact not found")

    elif action == "exit":
        print("Program exited")
        break

    else:
        print("Invalid Command, try again")