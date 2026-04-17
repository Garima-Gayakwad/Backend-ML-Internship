# banking system using oops concepts
# adding all 4 concepts: encapsulation, abstraction, inheritance, polymorphism

# ABSTRACTION - base class, get_type() is meant to be overridden by child classes
class Account:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.__acc_no = acc_no       # ENCAPSULATION - private, cant access from outside
        self.__balance = balance     # ENCAPSULATION - private attribute
        self.__history = []          # private list to store all transactions

    # only way to read private balance from outside
    def get_balance(self):
        return self.__balance
    def get_acc_no(self):
        return self.__acc_no
    
    def credit(self, amount): # deposit money into account
        self.__balance += amount
        self.__history.append(f"credited Rs.{amount}")
        print(f"Rs. {amount} was credited")
        print(f"total balance = {self.__balance}")

    def debit(self, amount): # withdraw money from account
        if amount > self.__balance:
            print("not enough balance!")
            return
        self.__balance -= amount
        self.__history.append(f"debited Rs.{amount}")
        print(f"Rs. {amount} was debited")
        print(f"total balance = {self.__balance}")

    def show_history(self): # show all transactions
        print(f"\n{self.name}'s transaction history:")
        if not self.__history:
            print("  no transactions yet!")
            return
        for h in self.__history:
            print(f"  - {h}")

    def get_type(self): # abstract method - child classes should override this
        return "Basic Account"

# INHERITANCE - savings account gets everything from Account
class SavingsAccount(Account):
    def __init__(self, name, acc_no, balance):
        super().__init__(name, acc_no, balance)  # calling parent init
        self.interest_rate = 4  # (4% annual interest)

    # POLYMORPHISM - overrides parent's get_type()
    def get_type(self):
        return "Savings Account"

    def add_interest(self): # extra feature only savings account has
        interest = self.get_balance() * self.interest_rate / 100
        print(f"\nAdding {self.interest_rate}% interest = Rs.{interest:.2f}")
        self.credit(interest)

# INHERITANCE - current account also inherits from Account
class CurrentAccount(Account):
    def __init__(self, name, acc_no, balance):
        super().__init__(name, acc_no, balance)
        self.min_balance = 1000  # (must keep min 1000 at all times)

    # POLYMORPHISM - different get_type than savings
    def get_type(self):
        return "Current Account"

    def debit(self, amount): # current account overrides debit - has a minimum balance rule
        if self.get_balance() - amount < self.min_balance:
            print(f"cannot debit! must maintain min balance of Rs.{self.min_balance}")
            return
        super().debit(amount)  # calling parent debit if check passes

#testing-
print("Welcome to Garima's Banking System\n")
# creating two accounts
acc1 = SavingsAccount("Garima", 10001, 10000)
acc2 = CurrentAccount("Neha", 10002, 15000)

# POLYMORPHISM - same get_type() method, different output for each
print("Account Details-")
for acc in [acc1, acc2]:
    print(f"Name: {acc.name} | Type: {acc.get_type()} | Balance: Rs.{acc.get_balance()} | Acc No: {acc.get_acc_no()}")

print("\nGarima's Savings Account-") # testing savings account
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
acc1.add_interest()  # only savings has this feature
acc1.show_history()

# testing current account
print("\nNeha's Current Account-")
acc2.debit(1000)
acc2.credit(500)
acc2.debit(14500)   # this will fail - min balance rule kicks in
acc2.show_history()

# ENCAPSULATION demo
print("\nEncapsulation Demo-")
print(f"Balance using getter method: Rs.{acc1.get_balance()}")
print("Trying acc1.__balance directly gives AttributeError - that is encapsulation.")