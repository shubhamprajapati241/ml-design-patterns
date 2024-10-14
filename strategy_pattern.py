from abc import ABC, abstractmethod 

# Step1 : Define the Strategy interface 
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass 

# Step2 : Implement Concrete Strategies 
class CreditCardPaymeny(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using credit card"

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using Bitcoin"

# Step3 : Impmlement the Context 
class ShoppingCart():
    def __init__(self, payment_method : PaymentMethod):
        self.payment_method = payment_method
    
    def checkout(self, amount):
        return self.payment_method.pay(amount) 

# Step4: Use the Strategy in the context 
if __name__ == "__main__":
    cart = ShoppingCart(BitcoinPayment())
    print(cart.checkout(100))

    cart = ShoppingCart(CreditCardPaymeny())
    print(cart.checkout(200))
