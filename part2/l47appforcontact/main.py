from contactmanager import ContactManager

def main():

    contactObj = ContactManager()

    while True:
        print("\n Contact Manager App")
        print("1. Create contact ")
        print("2. Read contact ")
        print("3. Update contact ")
        print("4. Delete contact ")
        print("5. Import contact ")
        print("6. Export contact ")
        print("7. exit contact ")

        choice = input("Choose an option: ")
        if choice == 1:
            name = input("Name : ")
            phone = input("Phone : ")
            email = input("Email : ")
            contactObj.createcontact(name, phone, email)

        elif choice == 2:
            contactObj.readcontact()

        elif choice == 3:
            contactid = int(input("Contact ID to edit : "))
            name = input("New name (blank to skip): ")
            phone = input("New phone (blank to skip): ") 
            email = input("New email (blank to skip): ")

            contactObj.updatecontact(contactid,name or None, phone or None, email or None)

        elif choice == 4:
            contactid = int(input("Contact ID to delete : "))
            contactObj.deletecontact(contactid)

        elif choice == 5:
            impjsonfile = input("Import file (JSON) : ")
            contactObj.importcontacts(impjsonfile)

        elif choice == 6:
            expfilename = input("Export file (JSON) : ")
            contactObj.exportcontacts(expfilename)

        elif choice == 7:
            print("Good Bye!")
            break

        else:
            print("Invalid opton.")

if __name__ == "__main__":
    main()




# Contact Manager 
# 1. Create contact (i) Name (ii) Phone (iii) Email
# 2. Read contacts 
# 3. Update contacts 
# 4. Deltet contacts 
# 5. Import contacts 
# 6. Save contacts
# 7. exit (auto save (json))

