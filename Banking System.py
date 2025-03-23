class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    # Static Method to print stars before printing user info
    @staticmethod
    def print_stars():
        return "*" * 40

    def display_info(self):
        print(User.print_stars())
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Street Address: {self.street_address}")
        print(f"City: {self.city}")
        print(f"Email: {self.email}")
        print(f"Credit Card Number: {self.cc_number}")
        print(f"Credit Card Type: {self.cc_type}")
        print(f"Balance: {self.balance}")
        print(f"Account Number: {self.account_no}")

    def add_balance(self, amount_to_add):
        self.balance += amount_to_add

    def remove_balance(self, amount_to_remove):
        self.balance -= amount_to_remove


def integer_checker(question):
    error = "\nPlease enter a number\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def generate_users():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])


def find_user():
    while True:
        user_first = input("Enter the first name of the user to find: ").title()
        user_last = input("Enter the last name of the user to find: ").title()
        user_found = False
        for users in userList:
            if users.first_name == user_first:
                if users.last_name == user_last:
                    users.display_info()
                    user_found = True
                    break
        if user_found:
            break
        else:
            print("User not found")

    
def overdrafts():
    count_users = 0
    count_balance = 0
    for user in userList:
        if user.balance < 0:
            count_users += 1
            count_balance += user.balance
            print(f"Name: {user.first_name} {user.last_name} | Balance: $"
                  f"{user.balance}")
    edited_balance = count_balance * -1
    print(f"Total number of users with negative balances are {count_users}")
    print(f"Total amount due from these users is ${edited_balance:.2f}")


def missing_emails():
    number_of_users = 0
    for user in userList:
        if len(user.email) < 1:
            number_of_users += 1
            print(f"Name: {user.first_name} {user.last_name}")
    if number_of_users == 0:
        print("All users have emails")
    else:
        print(f"There are {number_of_users} users with no emails")


# Function to print total users, total value and highest and lowest users
def bank_details():
    # Tracks number of users
    count = 0
    # Tracks total balance of all users
    total_value = 0
    # Tracks the highest of the user with the most
    highest_balance = 0
    # Tracks the lowest balance of the user with the least
    lowest_balance = 0
    # Initializes variables for highest/lowest users names
    highest_user = ""
    lowest_user = ""
    # Iterates through users in list
    for user in userList:
        # Adds user to the count
        count += 1
        # Adds user balance to the total
        total_value += user.balance
        # If the users balance is higher than the current highest
        if user.balance > highest_balance:
            # Makes this users balance the highest
            highest_balance = user.balance
            # Sets the highest users name to the variable
            highest_user = user.first_name + " " + user.last_name
    # Iterates through users in list
    for user in userList:
        # If users balance is lower than the lowest currently
        if user.balance < lowest_balance:
            # Updates variables for new lowest user
            lowest_balance = user.balance
            lowest_user = user.first_name + " " + user.last_name

    print(f"There are {count} users at this bank")
    print(f"There is a total value of ${total_value}")
    print(f"User with the highest balance is {highest_user} with a balance of "
          f"${highest_balance}")
    print(f"User with the lowest balance is {lowest_user} with a balance of "
          f"${lowest_balance}")


# Function to get the amount to transfer
def transfer_amount(user):
    while True:
        # Checks the amount to transfer is a number
        amount_to_transfer = integer_checker("How much would you like to "
                                           "transfer: ")
        # Resets loop if user tries to transfer 0 or less
        if amount_to_transfer <= 0:
            print("Please enter an amount above $0")
            continue
        # If amount is less (/equal) to balance and greater than 0, breaks loop
        elif amount_to_transfer <= user.balance:
            break
        else:
            print(f"Please choose an amount from your remaining "
                  f"balance of ${user.balance}")
    return amount_to_transfer


# Function to find the account to transfer money to
def account_to_transfer(original_acc):
    while True:
        account = input("Enter the number of the account to transfer to: ")
        found = False  # Add a flag to track if the account was found
        for user in userList:
            if account == original_acc:
                print("You cannot transfer to the same account")
                break  # Exit the loop since the account is invalid
            elif account == user.account_no:
                return account, user.first_name, user.last_name, user
        else: # This else statement is attached to the for loop. It executes
            # when the for loop finishes normally (no break)
            if not found and account != original_acc:
                print("Enter an account in the system")
                continue #continue to the next loop iteration.


# Function to run the transfers
def transfer():
    # Get the number of the account to transfer from
    account_no_input = input("Enter the number of your account to find: ")
    for user in userList:
        # If the account number matches one in the user list
        if account_no_input == user.account_no:
            # Prints details of the account
            print(f"Name: {user.first_name} {user.last_name}")
            print(f"Account balance: ${user.balance}")
            # Runs function to get the amount to transfer
            amount_to_transfer = transfer_amount(user)
            # Runs function to get details of account to transfer to
            transfer_account, transfer_first, transfer_last, transfer_user = (
                account_to_transfer(user.account_no))
            # Prints details of account to transfer to
            print(f"Confirm you want to transfer ${amount_to_transfer} to "
                  f"{transfer_first} {transfer_last} with the account number "
                  f"{transfer_account}")
            # Asks user to confirm transfer
            confirm = input("Type 'Yes' to confirm the transfer: ").lower()
            if confirm == "yes":
                # Gets original balances
                original_balance_from = user.balance
                original_balance_to = transfer_user.balance
                # Updates balances with class method
                user.remove_balance(amount_to_transfer)
                transfer_user.add_balance(amount_to_transfer)
                print()
                # Prints user details
                print(f"Name: {user.first_name} {user.last_name}\nAccount "
                      f"Number: {user.account_no}\nOriginal Account Balance: "
                      f"${original_balance_from}\nUpdated Account Balance: "
                      f"${user.balance}")
                print(f"Name: {transfer_first} {transfer_last}\nAccount "
                      f"Number: {transfer_account}\nOriginal Account Balance: "
                      f"${original_balance_to}\nUpdated Account Balance: "
                      f"${transfer_user.balance}")
            else:
                print("Transfer cancelled")


# Main routine
userList = []          
generate_users()

userChoice = ""
print("Welcome\n")

while userChoice != "Q":
    print("What function would you like to run?\n")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("\nEnter choice: ")
    print()

    if userChoice == "1":
        find_user()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missing_emails()
    elif userChoice == "4":
        bank_details()
    elif userChoice == "5":
        transfer()
    print()
