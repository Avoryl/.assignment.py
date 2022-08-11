
contact: dict = {'name1': 'oral', 'phone1': '(+229)97077184', 'name2': 'Acer', 'phone2': '(+233)0202362416',
                 'name3': 'Danice', 'phone3': '(+233)274976641', 'name4': 'romeo', 'phone4': '(+233)0592284893',
                 'name5': 'Ola', 'phone5': '(+233)266706694', 'name6': 'Madame Felicien', 'phone6': '(+224)620955397', }


def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))


while True:
    choice = int(input("1.Add new contact\n 2.Search contact\n 3.Display contact\n "
                       "4.Edit contact\n 5.Delete contact\n 6.Exit"))
    if choice == 1:
        name = input("enter the contact name")
        phone = input("enter the mobile number")
        contact[name] = phone
    elif choice == 2:
        search_name = input("enter the contact name")
        if search_name in contact:
            print(search_name, "s contact number is", contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited")
        if edit_contact in contact:
            phone = input("enter mobile")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")

    elif choice == 5:
        del_contact = input("enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact yes or no ?")
            if confirm == 'y' or confirm == 'y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break









