class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self, balance):
        print(self.name, "has an account balance of: ", self.balance)

    def withdraw(self, debit):
        self.debit = debit
        self.balance -= self.debit
        print(self.name, "has an account balance of: ", self.balance)

    def deposit(self, deposited):
        self.deposited = deposited
        self.balance += self.deposited
        print(self.name, "has an account balance of: ", self.balance)

    def transfer_money(self, transfer_amt, other_user):
        self.transfer_amt = transfer_amt
        self.other_user = other_user
        print("You are transfering", self.transfer_amt,
              "to", self.other_user.name)
        print("Authentication required")
        pin = int(input("Enter your PIN:"))
        if self.pin == pin:
            print("Transfer authorized")
            print("You are transferring", self.transfer_amt,
                  "to", self.other_user.name)
            self.balance -= self.transfer_amt
            self.withdraw(transfer_amt)
            self.other_user.deposit(self.transfer_amt)
            other_user.balance = +transfer_amt
            other_user.show_balance()
            return True
        else:
            return False

    def request_money(self, request_amt, request_user):
        print("You are requeessting", request_amt, "from", request_user.name)
        print("User authentication is required")
        request_pin = int(input("Enter PIN here:"))
        if request_pin == request_user.pin:
            password = input("Enter password here:")
            if password == self.password:
                print("Request authorized")
                print(request_user.name, "sent", request_amt)
                self.show_balance("balance")
                request_user.show_balance("balance")
                return True
            else:
                print("Invalid passsword...transaction denied")
                self.show_balance("balance")
                request_user.show_balance()
                return False
        else:
            print("Invalid PIN, transaction denied")
            self.show_balance("balance")
            request_user.show_balance("balance")
            return False


""" Driver Code for Task 1 """
#user1 = User("Bob", "1234", "password")
#print(user1.name, user1.pin, user1.password)
""" Driver Code for Task 2 """
#user2 = User("Bob", "1234", "password")
#print(user2.name, user2.pin, user2.password)
# user2.change_name("Bobby")
# user2.change_pin("4321")
# user2.change_password("newpassword")
#print(user2.name, user2.pin,user2.password)
""" Driver Code for Task 3"""
#bankuser1 = BankUser("Bob", "1234", "password")
#print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
""" Driver Code for Task 4"""
#bankuser2 = BankUser("Bob", "1234", "password")
# bankuser2.show_balance("balance")
# bankuser2.deposit(1000.0)
# bankuser2.withdraw(400.0)
""" Driver Code for Task 5"""
bankuser1 = BankUser("Bob", "1234", "password")
bankuser2 = BankUser("Abbey", "0101", "nupassword")
bankuser2.show_balance("balance")
bankuser1.show_balance("balance")
bankuser2.show_balance(5000)
bankuser2.transfer_money(500, bankuser1)
bankuser2.request_money(200, bankuser1)
