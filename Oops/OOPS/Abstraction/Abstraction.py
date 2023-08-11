from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def subject(self):
        pass

class Stats():
    def subject(self):
        print("This is Stats Subject")

class Accounts():
    def subject(self):
        print("This is Accounts Subject")

class Economics():
    def subject(self):
        print("This is Economics Subject")




stats=Stats()
stats.subject()
accounts=Accounts()
accounts.subject()
economics=Economics()
economics.subject()