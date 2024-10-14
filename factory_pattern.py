from abc import ABC, abstractmethod 

# Step1: Define the Project interface 
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass 

# Step2: Implement Concrete Products 
class Espresso(Coffee):
    def prepare(self):
        return "Preparing Espresso"

class Lattee(Coffee):
    def prepare(self):
        return "Preparing Lattee"

class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing Cappuccino"

# Step3 : Implement the factory 
class CoffeeMachine:
    def make_coffee(self, coffee_type):
        if coffee_type == 'Espresso':
            return Espresso().prepare()
        if coffee_type == 'Lattee':
            return Lattee().prepare()        
        if coffee_type == 'Cappuccino':
            return Cappuccino().prepare()

if __name__ == "__main__":
    machine = CoffeeMachine()
    coffee = machine.make_coffee("Espresso") 
    print(coffee) 
    coffee = machine.make_coffee("Lattee") 
    print(coffee) 
    coffee = machine.make_coffee("Cappuccino") 
    print(coffee) 