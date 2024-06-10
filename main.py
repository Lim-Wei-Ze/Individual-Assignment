import functions as f

# Displays the main menu of the Malaysian Tax Input Program.
def display_menu():
    print("Welcome to the Malaysian Tax Input Program")
    print("1. Register account")
    print("2. Sign in")
    print("3. Check the tax records")
    print("4. Close")

# Main function to handle user interactions and program flow.

def main():
    registered_users = {}
    running = True
    while running:
        display_menu()
        choice = input("Enter your choice(1/2/3/4): ")

        # Registration process
        if choice == '1':
            id = input("Enter your ID: ")
            ic_number = input("Enter your IC number (without dash): ")
            password = input("Enter the password (last 4 digits of your IC number): ")

            if f.verify_user(ic_number, password):
                registered_users[id] = ic_number
                print("Registration successful!")
            else:
                print("Invalid IC number or password. Please try again.")

        # Sign-in process
        elif choice == '2':
            id = input("Enter your ID: ")
            password = input("Enter the password (last 4 digits of your IC number): ")

            if id in registered_users:
                ic_number = registered_users[id]
                if f.verify_user(ic_number, password):
                    print("Sign in successful!")

                    # User actions after login
                    print("What would you like to do? ")
                    print("1. Calculate tax")
                    print("2. Back to the main menu.")
                    choice_2 = input("Enter your choice(1/2): ")

                    # Tax calculation 
                    if choice_2 == '1':
                        income = float(input("Enter your annual income: RM "))
                        print("")
                        print("""For your information, here is the key tax reliefs available in Malaysia:
-Individual tax relief: RM9,000 for resident individual taxpayers.
-Spouse relief: RM4,000 for a resident spouse who has no income or has an income of up to RM4,000 per year.
-Child relief: RM8,000 for each child up to a maximum of 12 children.
-Medical expenses relief: Up to RM8,000 for serious medical treatment expenses for self, spouse, or child.
-Lifestyle relief: Up to RM2,500 for purchases of reading materials, sports equipment, computer, smartphone, internet subscription, etc.
-Education fees relief: Up to RM7,000 for course fees at recognized institutions.
-Parental care relief: Up to RM5,000 for parents.
                               
Please CHOOSE the tax reliefs that are SUITABLE for you.
                                """)
                        tax_relief = float(input("Enter your tax relief amount: RM "))

                        tax_payable = f.calculate_tax(income, tax_relief)
                        print(f"Your tax payable is: RM {tax_payable:.2f}")

                        data = {'IC Number': ic_number, 'Income': income, 'Tax Relief': tax_relief, 'Tax Payable': tax_payable}
                        f.save_to_csv(data, 'tax_data.csv')

                        print("Data saved successfully!")

                    # Return to the main menu
                    elif choice_2 == '2':
                        print("Got it.")
                    else:
                        print("Invalid choice. Please try again.")

                else:
                    print("Invalid password. Please try again.")
            else:
                print("Invalid ID. Please try again.")
        
        # View tax records
        elif choice == '3':
            records = f.read_from_csv('tax_data.csv')
            if records is not None:
                print(records)
            else:
                print("No tax records found.")
        
        # Exit the program
        elif choice == '4':
            print("Thank you for using the Malaysian Tax Input Program. See you again!")
            running = False
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
