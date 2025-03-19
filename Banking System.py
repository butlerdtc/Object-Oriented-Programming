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
    # TO COMPLETE
    
    True
    
def missing_emails():
    # TO COMPLETE

    True

def bank_details():
    # TO COMPLETE

    True
    
def transfer():
    # TO COMPLETE

    True

userList = []          
generate_users()

# userChoice = ""
# print("Welcome")
#
# while userChoice != "Q":
#     print("What function would you like to run?")
#     print("Type 1 to find a user")
#     print("Type 2 to print overdraft information")
#     print("Type 3 to print users with missing emails")
#     print("Type 4 to print bank details")
#     print("Type 5 to transfer money")
#     print("Type Q to quit")
#     userChoice = input("Enter choice: ")
#     print()
#
#     if userChoice == "1":
#         findUser()
#     elif userChoice == "2":
#         overdrafts()
#     elif userChoice == "3":
#         missingEmails()
#     elif userChoice == "4":
#         bankDetails()
#     elif userChoice == "5":
#         transfer()
#     print()
# for user in userList:
#     user.display_info()
find_user()
