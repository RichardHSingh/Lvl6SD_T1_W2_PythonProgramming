#============== STELLA EVENT SCENARIO =====================

#creating a class for the Stellar Events
class ContactBook():

     #constructor to create dictionary with respective keys plus its values
    def __init__(self):
        # initialize the vendor_details attribute to an empty dictionary
        self.vendor_details = {}

        #getting the vendors detail during the input phase
        self.add_vendor()

    
    # going to create a function with parameters that takes details from input and stores is into the dictionary created earlier
    # every detail will be a string to save time from conversion
    # using a similar concept as C# to store all the information
    def add_vendor(self):
        print("Welcome to Stellar Events contact list...")
        name = input("Please enter your name or organization name: ")
        phone = input("Please enter your contact phone number: ")
        email = input("Please enter your email address: ")
        additional_info = input("Please add any additional information: ")

        # parameters to get data  --> key value plus whatever user inputs
        self.vendor_details[name] = {"Phone": phone, "Email": email, "Additional Information": additional_info}

    # creating method to access the vendors details from the contact book
    def access_vendor(self, name):
        # using get keyword to call on details in book
        return self.vendor_details.get(name, None)
    

    # removing vendor from the contact list method
    def remove_vendor(self, name):
        #using if else statements  to find them and return appropriate message with use of del keyword
        if name in self.vendor_details:
            del self.vendor_details[name]
            print(f"\nFollowing vendor {name} has been removed from the contact list")
        else:
            print(f"Following vendor {name} could not be accessed as it does not exist in the list")

    
    # updting any changes to vendor information method
    def update_vendor(self, name, phone = None, email = None, additional_info = None):
        # giving parameters of what can be updated but not limited, at least user wont be forced in having to change every detail
        # phone, email and additional catagories are optional at this point

        if name in self.vendor_details:
            if phone:
                self.vendor_details[name]["Phone"] = phone
            if email:
                self.vendor_details[name]["Email"] = email
            if additional_info:
                self.vendor_details[name]["Addition Information"] = additional_info
            print(f"Following vendor details, {name} has updated successfully.")
        else:
            print(f"ERROR! Vendor {name} could not be located in the contact book.")


    # creating a display method for Menu so that users can traverse as needed
    def show_menu(self):
        #creating simple table of contents
        print("\nMenu:")
        print("Please select from following options..\n")
        print("1. Add New Vendor Information")
        print("2. Access Vendor Information")
        print("3. Delete Vendor Information")
        print("4. Alter Vendor Information")
        print("5. Exit Program\n")


    # last method to having the program running - tried using switch cases like in C# but sadly it cant be done in python
    # execute method will have if else statements so that all the previous methods can now be utilised 
    # rather than using just if else statements, while loops will be implemented
    def execute(self):
        while True:
            self.show_menu()
            option = input("Please use numbers 1-5 to proceed: ")

            if option == "1":
                # this option allows the user to add a new user to the list
                self.add_vendor()

            elif option == "2":
                # entering 2 will allow the user to access any/all of the vendor information saved thus far
                name = input("Enter the vendor's name you wish to access: ")
                vendor_details = self.access_vendor(name)
                if vendor_details:
                    print(f"\nVendor Details Are: \nName: {name}\nPhone: {vendor_details.get('Phone', 'N/A')}\nEmail Address: {vendor_details.get('Email', 'N/A')}\nAdditional Information: {vendor_details.get('Additional Information', 'N/A')}")
                else: 
                    print(f"OOPS! Entered name {name} could not be found")

            
            elif option == "3":
                # choosing option 3 will allow users delete/remove vendors from a list
                name = input("Enter name of vendor you wish to remove: ")
                self.remove_vendor(name)

            
            elif option == "4":
                # choosing option 4 will allow user to update any or all the pre-existing information on the list
                # \x1B[3m = start of italics ||  \x1B[0m = end of italics
                name = input("Please enter vendor's name to update: ")
                phone = input("Please enter new phone number (\x1B[3m press 'Enter' to keep existing information \x1B[0m): ")
                email = input("Please enter new email address (\x1B[3m press 'Enter' to keep existing information \x1B[0m): ")
                additional_info = input("Please enter new extra details (\x1B[3m press 'Enter' to keep existing information \x1B[0m) : ")
                self.update_vendor(name, phone, email, additional_info)

            
            elif option == "5":
                # hitting 5th option will cause user to exit the program
                # .lower converts input like YES/NO to yes/no
                confirmation = input("Exiting program! Are you sure you want to proceed? (yes/no) ").lower()

                # nested if else statement to re-route user in case 5 was pressed by accident
                if confirmation == "yes":
                    print("Exiting Program... BYE BYE!")
                    break
                elif confirmation == 'no':
                    print("Re-routing to the main menu")
                    continue  # Restart the loop to display the menu again
                else:
                    print("Invalid input.. returning to the main menu")
                    continue  # Restart the loop to display the menu again


contact_book = ContactBook()
contact_book.execute()
   