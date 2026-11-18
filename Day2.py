from abc import ABC, abstractmethod 

class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class upi(payment):
    def pay(self, amount):
        print(f"Paid {amount} using upi") 
class Card(payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")

p1 = upi()
p2 = Card()
p1.pay(1000)
p2.pay(2000)   