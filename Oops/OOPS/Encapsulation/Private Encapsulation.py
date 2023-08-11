## Private Encapsulation

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        print("Total deposited amount :", self.__balance)

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount

    def show(self):
        print("Total Balance :",self.__balance)

account=BankAccount("James",80000)

account.deposit(30000)

account.withdraw(40000)

account.show()