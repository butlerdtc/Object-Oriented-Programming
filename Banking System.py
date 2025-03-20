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
            print(f"Name: {user.first_name} {user.last_name}")
    edited_balance = count_balance * -1
    print(f"Total number of users with negative balances are {count_users}")
    print(f"Total amount due from these users is ${edited_balance:.2f}")


def missing_emails():
    number_of_users = 0
    for user in userList:
        if user.email != "":
            number_of_users += 1
            print(f"Name: {user.first_name} {user.last_name}")
    if number_of_users == 0:
        print("All users have emails")


def bank_details():
    count = 0
    total_value = 0
    highest_balance = 0
    highest_user = ""
    lowest_balance = 0
    lowest_user = ""
    for user in userList:
        count += 1
        total_value += user.balance
        lowest_balance += user.balance
        if user.balance > highest_balance:
            highest_balance = user.balance
            highest_user = user.first_name + user.last_name
    print(f"{highest_user}: ${highest_balance}")


def transfer_amount(user):
    while True:
        transfer_amount_ = integer_checker("How much would you like to "
                                           "transfer: ")
        if transfer_amount_ <= 0:
            print("Please enter an amount above $0")
            continue
        elif transfer_amount_ <= user.balance:
            break
        else:
            print(f"Please choose an amount from your remaining "
                  f"balance of ${user.balance}")
    return transfer_amount_


def account_to_transfer(original_acc):
    while True:
        account = input("Enter the number of the account to transfer"
                                  " to: ")
        for user in userList:
            if account == original_acc:
                print("You cannot transfer to the same account")
                continue
            elif account == user.account_no:
                return account, user.first_name, user.last_name, user


def transfer():
    account_no_input = input("Enter the number of the account to find: ")
    for user in userList:
        if account_no_input == user.account_no:
            print(f"Name: {user.first_name} {user.last_name}")
            print(f"Account balance: ${user.balance}")
            amount_to_transfer = transfer_amount(user)
            transfer_account, transfer_first, transfer_last, transfer_user = (
                account_to_transfer(user.account_no))
            print(f"Confirm you want to transfer ${amount_to_transfer} to "
                  f"{transfer_first} {transfer_last} with the account number "
                  f"{transfer_account}")
            confirm = input("Type 'Yes' to confirm the transfer: ").lower()
            if confirm == "yes":
                user.balance -= amount_to_transfer
                transfer_user.balance += amount_to_transfer
                print(f"Name: {user.first_name} {user.last_name}\nAccount "
                      f"Number: {user.account_no}\nAccount Balance: ${user.
                      balance}")
                print(f"Name: {transfer_first} {transfer_last}\nAccount "
                      f"Number: {transfer_account}\nAccount Balance: ${
                      transfer_user.balance}")


# Main routine
userList = []          
generate_users()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
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
